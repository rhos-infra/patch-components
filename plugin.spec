---
plugin_type: install
description: Patch components source code and repackage the RPM
subparsers:
    patch:
        help: Patch the components source code
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: Patch the component source code
              options:
                  url:
                      type: Value
                      help: 'The url of the component'
                      required: True
                  branch:
                      type: Value
                      help: 'The branch of the component'
                      required: True
                  dist-git:
                      type: Value
                      help: 'The url of the dist-git repo'
                      required: True
