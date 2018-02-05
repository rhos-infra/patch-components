---
plugin_type: install
description: Patch components source code and repackage the RPM
subparsers:
    patch-components:
        help: Patch the components source code
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: Patch the component source code
              options:
                  component-name:
                      type: Value
                      help: 'name of the component (cinder, neutron, nova, etc)'
                      required: True
                  component-version:
                      type: Value
                      help: 'branch of the component (5,6,7,8,9,10,11,12,13)'
                      required: True
                  component-path:
                      type: Value
                      help: 'Full path where the component (cinder, nova, etc) is located'
                      required: False
                  host-ip:
                      type: Value
                      help: 'ip of the machine that rpm will be built on'
                      required: False
                  host-username:
                      type: Value
                      help: 'username on the machine that rpm will be built on'
                      required: False
                  host-key_file:
                      type: Value
                      help: 'SSH key for the <host-username>'
                      required: False
                  branch:
                      type: Value
                      help: |
                          This parameter can be used to checkout and patching of branch
                          of a component and its dist-git repository that is not
                          a default one (rhos-XY...). This parameter is a name of branch
                          to use for component and dist-git repositories to be patched.
                          'rhos-<component-version>.0-patches' and
                          'rhos-<component-version>-rhel-<rhel_version>.0' will be added
                          to this variable for component and dist-git git repositories
                          respectively.
                          Example:
                                '--branch private-wznoinsk-62'
                          The above example will cause component's git repository to be
                          checked out with private-wznoinsk-62-rhos-12.0-patches branch
                          as well as branch private-wznoinsk-62-rhos-12.0-rhel-7 of
                          dist-git repo.
                      required: False
