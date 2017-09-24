#!/bin/sh -x
# description    : This script creates rpm for the component specified by the TARGET
#                  argument. The assumption is that dist-git and component (e.g. cinder)
#                  repos are located under TARGET_DIR. PRE_RELEASE argument specifies
#                  whether TARGET was released or not.
# usage example	 : patch.sh TARGET="cinder" TARGET_DIR="~/cinder" PRE_RELEASE="true"
#========================================================================================

for ARGUMENT in "$@"
do
    KEY=$(echo $ARGUMENT | cut -f1 -d=)
    VALUE=$(echo $ARGUMENT | cut -f2 -d=)

    case "$KEY" in
            TARGET)              TARGET=${VALUE} ;;
            TARGET_DIR)          TARGET_DIR=${VALUE} ;;
            PRE_RELEASE)         PRE_RELEASE=${VALUE} ;;
            *)
    esac
done

echo "TARGET = $TARGET"
echo "TARGET_DIR = $TARGET_DIR"
echo "PRE_RELEASE = $PRE_RELEASE"

#sleep 3600

git config --global user.name `whoami` || { echo "failed git config user.name"; exit 1;}
git config --global user.email `whoami`@redhat.com || { echo "failed git config user.email"; exit 1;}

if [ "$PRE_RELEASE" == 'true' ]; then
    SHA=$(egrep Source0 *spec|egrep -o '[0-9a-f]*\.t'|sed -e 's!\.t$!!')
    if [[ -z "$SHA" ]]; then
        echo "MISSING SHA1 PARAMETER"
        exit 1;
    fi
fi

if ! grep -q "patches_ignore=DROP-IN-RPM" *spec; then
        echo "MISSING RDOPKG HINT IN THE SPEC:"
        perl -pi -e '$_ = "
# patches_ignore=DROP-IN-RPM
# patches_base='$SHA'
\n$_" if /BuildArch:\s*noarch/' *spec
        cat <<EOF
EOF

git commit -a -m "Add patches_ignore and patches_base"  || { echo "failed git commit"; exit 1;}
fi

echo ">> Adding remotes:"
git remote add upstream https://github.com/openstack/$TARGET || { echo "failed git remote add upstream"; exit 1;}
git remote add -f patches $TARGET_DIR/$TARGET || { echo "failed git remote add patches"; exit 1;}
git fetch --all --tags || { echo "failed git fetch"; exit 1;}


# actual work:
if [ "$PRE_RELEASE" == 'true' ]; then
    BRANCH=$(git branch |grep '*'|cut -f 2 -d\ )
    PATCH_BRANCH=${BRANCH/rhel?*/patches}

    echo ">> Retrieving patches from $PATCH_BRANCH:"
    git checkout $PATCH_BRANCH || { echo "failed git checkout " $PATCH_BRANCH; exit 1;}
    git rebase $SHA &> rebase_log
    if [  $? -ne 0 ]; then
       echo "rebase conflict"
       grep -q "Applying: RHOS:  use internal gerrit - DROP-IN-RPM" rebase_log
       if [ $? -eq 0 ]; then
             echo "try to resolve rebase conflict"
             git rebase --abort || { echo "failed git rebase abort"; exit 1;}
             git rebase $SHA -s ours  $PATCH_BRANCH || { echo "failed git rebase"; exit 1;}
       else
             # display the error
             cat rebase_log
       fi
    else
        echo "rebase sucess"
    fi
    git push --set-upstream patches --force || { echo "failed git push"; exit 1;}
    git checkout $BRANCH || { echo "failed git checkout " $BRANCH; exit 1;}
else
    git branch $PATCH_BRANCH patches/gerrit-patch;
fi


rdopkg patch &> rdopkg_log
if [  $? -ne 0 ]; then
   grep -q "No patches changed" rdopkg_log
   if [ $? -ne 0 ]; then
      echo "rdopkg patch failed"
      exit 1;
   fi
fi

