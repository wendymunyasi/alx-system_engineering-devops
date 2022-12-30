# Project Name.
**0x0A. Configuration management**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

### Bash Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
*   Your Puppet manifests must run without error.
*   Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
*   Your Puppet manifests files must end with the extension `.pp`.
*   Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

## Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://puppet.com/docs/puppet/5.5/puppet_index.html)

## Install puppet-lint
```
$ gem install puppet-lint
```


* **0. Create a file** - Using Puppet, create a file in `/tmp`. - `0-create_a_file.pp`.

  Requirements:

  * File path is `/tmp/school`
  * File permission is `0744`
  * File owner is `www-data`
  * File group is `www-data`
  * File contains `I love Puppet`
  ```
  root@6712bef7a528:~# puppet-lint --version
  puppet-lint 2.5.2
  root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
  root@6712bef7a528:~# 
  root@6712bef7a528:~# puppet apply 0-create_a_file.pp
  Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
  Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
  Notice: Finished catalog run in 0.03 seconds
  root@6712bef7a528:~#
  root@6712bef7a528:~# ls -l /tmp/school
  -rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
  root@6712bef7a528:~# cat /tmp/school
  I love Puppetroot@6712bef7a528:~#
  ```
---

* **1. Install a package** - Using Puppet, install `flask` from `pip3`. Version must be `2.1.0`. - `1-install_a_package.pp`.
  ```
  root@9665f0a47391:/# puppet apply 1-install_a_package.pp
  Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
  Notice: /Stage[main]/Main/Package[Flask]/ensure: created
  Notice: Applied catalog in 0.20 seconds
  root@9665f0a47391:/# flask --version
  Python 3.8.10
  Flask 2.1.0
  Werkzeug 2.1.1
  ```
---

* **2. Execute a command** - Using Puppet, create a manifest that kills a process named `killmenow`. Must use the `exec` Puppet resource. Must use `pkill` .`2-execute_a_command.pp`.

    **Terminal 0 - starting my process.**
    ```
    root@d391259bf577:/# cat killmenow
    #!/bin/bash
    while [[ true ]]
    do
        sleep 2
    done

    root@d391259bf577:/# ./killmenow
    ```

    **Terminal 1 - executing my manifest.**
    ```
    root@d391259bf577:/# puppet apply 2-execute_a_command.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
    Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
    Notice: Finished catalog run in 0.10 seconds
    root@d391259bf577:/# 
    ```

    **Terminal 0 - process has been terminated.**
    ```
    root@d391259bf577:/# ./killmenow
    Terminated
    root@d391259bf577:/#
    ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
