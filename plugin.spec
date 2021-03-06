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
                      help: 'component RHOSP release'
                      required: True
                  component-path:
                      type: Value
                      help: 'Full path where the componet (cinder, nova, etc) is located'
                      required: False
                  branch-trunk:
                      type: Bool
                      help: 'Should trunk branch be used instead of regular branch'
                      required: False
                      default: False
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
                  pattern:
                      type: Value
                      help: 'A pattern of a node or group as appears in ansible inventory'
                      required: False
                  tester-node:
                      type: Value
                      help: The name of the node from where to run the patching
