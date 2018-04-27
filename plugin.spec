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
                  component-path:
                      type: Value
                      help: 'Full path where the componet (cinder, nova, etc) is located'
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
                      help: 'SSH key for the user <username>'
                      required: False
                  extra-components:
                      type: Value
                      help: |
                          Comma,delimited names of additional components. This param may
                          be used to specify additional components required to build
                          the main component's distribution and/or RPM.
                          Use case example: OpenDaylight consists of multiple components
                          and sometimes a feature from component A is required for the
                          feature from component B to work. In this case all prerequisite
                          components has to be listed in extra-components param.
                          NOTE: This feature is currently supporting only OpenDaylight
                          components.
                      required: False
