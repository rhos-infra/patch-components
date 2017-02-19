## Patch-components

Allows to repackage RPMs with source code directly from Gerrit or local repo.

### How to use this projet

Create virtual environment:

    virtualenv venv
    source venv/bin/activate
    pip install ansible 

Clone the component and cherry-pick the patch:

    git clone https://<<gerrit url>>/gerrit/cinder
    git fetch https://<<gerrit url>>/gerrit/cinder refs/changes/62/89862/2 && git checkout FETCH_HEAD

Run:

    ansible-playbook -i hosts main.yml --extra-vars @params.yml -vvvv

## Result

The project will generate one or more RPMs in the following path: dist-git/<component_name>

   ./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/openstack-cinder-8.1.1-6.el7ost.noarch.rpm
   ./dist-git/openstack-cinder/results_openstack-cinder/8.1.1/6.el7ost/python-cinder-8.1.1-6.el7ost.noarch.rpm

### InfraRed Support

This project is supported by Infrared.
