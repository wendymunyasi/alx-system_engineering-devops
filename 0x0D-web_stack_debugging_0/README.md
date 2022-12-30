# Project Name.
**0x0D. Web stack debugging #0**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
*   All your Bash script files must be executable.
*   Your Bash scripts must pass `Shellcheck` without any error.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.


## Project Description.
Learn **DOCKER**.


* **0. Give me a page!** - In this first debugging project, you will need to get `Apache` to run on the container and to return a page containing `Hello Holberton` when querying the root of it. - `0-use_a_private_key`.

  Example:
  ```
  vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
  47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
  vagrant@vagrant:~$ docker ps
  CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
  47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
  vagrant@vagrant:~$ curl 0:8080
  curl: (52) Empty reply from server
  vagrant@vagrant:~$
  ```

  Here we can see that after starting my Docker container, I `curl` the port `8080` mapped to the Docker container port `80`, it does not return a page but an error message. Note that you might also get the error message `curl: (52) Empty reply from server`.

  ```
  vagrant@vagrant:~$ curl 0:8080
  Hello Holberton
  vagrant@vagrant:~$
  ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
