## Patch-components

Allows to repackage RPMs with source code directly from Gerrit or local repo.

### How to use this project as an ansible playbook

Create virtual environment:

    virtualenv venv
    source venv/bin/activate
    pip install ansible

Clone the component <component-name> from <gerrit url> to ~/ and cherry-pick the patch:

    git clone https://<gerrit url>/gerrit/<component-name> ~/<component-name>
    cd ~/<component-name>
    git fetch https://<gerrit url>/gerrit/<component-name> refs/changes/xy/abcde/x && git checkout FETCH_HEAD

Run:

    ansible-playbook -i hosts main.yml --extra-vars @params.yml -vvvv


### Pre-release version patching

Creation of rpm is allowed with per-released version as well. Make sure to increment the pre_rel_version
variable located in roles/patch_rpm/vars/main.yml when version is released to avoid failure in patching.


### Result

The project will generate one or more RPMs in the following path: dist-git/<component_name>


### How to use this as an InfraRed plugin

Clone the component <component-name> from <gerrit url> to ~/ and cherry-pick the patch as described in the section
"How to use this project as an ansible playbook". Create virtual environmenti and install infrared:

    git clone https://github.com/redhat-openstack/infrared.git
    cd infrared
    virtualenv venv
    source venv/bin/activate
    pip install -e .

Add patch-components as a plugin:

    infrared plugin add https://github.com/rhos-infra/patch-components.git

Run:
    infrared patch-components --host-ip A.B.C.D --host-username <user-name> --component-name <component-name>  --host-key_file ~/.ssh/id_rsa  --component-version <rhos version>
