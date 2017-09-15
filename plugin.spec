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
                      help: 'branch of the component (5,6,7,8,9,10,11)'
                      required: True
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
                      help: 'SSH key for the user <username>'
                      required: False
                  testmode-enabled:
                      type: Value
                      help: 'patch component if testmode is enabled'
                      default: False
                      required: False
                  testmode-gerrit-url:
                      type: Value
                      help: 'in testmode this plugin requires gerrit url to fetch component from'
                      required: False
                  testmode-gerrit-group:
                      type: Value
                      help: 'in testmode this plugin requires gerrit group to fetch component from'
                      required: False
