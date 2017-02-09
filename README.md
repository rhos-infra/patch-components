
#HOWTO checkout latest ref from gerrit and build RMP with this change on top of the repo

##Steps
```
virtualenv venv
source venv/bin/activate
pip install ansible 
git clone https://<<gerrit url>>/gerrit/cinder
git fetch https://<<gerrit url>>/gerrit/cinder refs/changes/62/89862/2 && git checkout FETCH_HEAD
ansible-playbook -i hosts main.yml --extra-vars @params.yml -vvvv
```
 

##Generated RPMs

```
./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/openstack-cinder-8.1.1-6.el7ost.noarch.rpm
./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/python-cinder-8.1.1-6.el7ost.noarch.rpm
./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/python-cinder-tests-8.1.1-6.el7ost.noarch.rpm
./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/openstack-cinder-doc-8.1.1-6.el7ost.noarch.rpm
./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/openstack-cinder-8.1.1-6.el7ost.src.rpm
```

#HOWTO using IR

