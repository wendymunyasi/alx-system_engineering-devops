# Project Name.
**0x0B. SSH**

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
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.

## Project Description.
Learn what is a server.
Where servers usually live.
What is SSH.
How to create an SSH RSA key pair.
How to connect to a remote host using an SSH RSA key pair.
The advantage of using `#!/usr/bin/env` bash instead of `/bin/bash`.


* **0. Use a private key** - Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user ubuntu. - `0-use_a_private_key`.

  Requirements:

  * Only use ssh single-character flags.
  * You cannot use `-l`.
  * You do not need to handle the case of a private key protected by a passphrase.
  ```
  sylvain@ubuntu$ ./0-use_a_private_key
  ubuntu@server01:~$ exit
  Connection to 8.8.8.8 closed.
  sylvain@ubuntu$
  ```
---

* **1. Create an SSH key pair** - Write a Bash script that creates an RSA key pair. - `1-create_ssh_key_pair`.
  ```
  sylvain@ubuntu$ ls
  1-create_ssh_key_pair
  sylvain@ubuntu$ ./1-create_ssh_key_pair
  Generating public/private rsa key pair.
  Your identification has been saved in school.
  Your public key has been saved in school.pub.
  The key fingerprint is:
  5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
  The key's randomart image is:
  +--[ RSA 4096]----+
  |      oo...      |
  |      .+.o =     |
  |     o  + B +    |
  |      o. = O     |
  |     .. S = .    |
  |      .. .       |
  |      E.  .      |
  |        ..       |
  |         ..      |
  +-----------------+
  sylvain@ubuntu$ ls
  1-create_ssh_key_pair school  school.pub
  sylvain@ubuntu$ 
  ```
---

* **2. Client configuration file** - Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file. - `2-ssh_config`.

  ```
  sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
  OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
  debug1: Reading configuration data /etc/ssh/ssh_config
  debug1: /etc/ssh/ssh_config line 47: Applying options for *
  debug1: Connecting to 98.98.98.98 port 22.
  debug1: Connection established.
  debug1: identity file /home/sylvain/.ssh/school type -1
  debug1: identity file /home/sylvain/.ssh/school-cert type -1
  debug1: Enabling compatibility mode for protocol 2.0
  debug1: Local version string SSH-2.0-OpenSSH_8.1
  debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
  debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
  debug1: SSH2_MSG_KEXINIT sent
  debug1: SSH2_MSG_KEXINIT received
  debug1: kex: server->client aes128-ctr hmac-sha1-etm@openssh.com none
  debug1: kex: client->server aes128-ctr hmac-sha1-etm@openssh.com none
  debug1: sending SSH2_MSG_KEX_ECDH_INIT
  debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
  debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
  debug1: Host '98.98.98.98' is known and matches the ECDSA host key.
  debug1: Found key in /home/sylvain/.ssh/known_hosts:1
  debug1: ssh_ecdsa_verify: signature correct
  debug1: SSH2_MSG_NEWKEYS sent
  debug1: expecting SSH2_MSG_NEWKEYS
  debug1: SSH2_MSG_NEWKEYS received
  debug1: SSH2_MSG_SERVICE_REQUEST sent
  debug1: SSH2_MSG_SERVICE_ACCEPT received
  debug1: Authentications that can continue: publickey,password
  debug1: Next authentication method: publickey
  debug1: Trying private key: /home/sylvain/.ssh/school
  debug1: key_parse_private2: missing begin marker
  debug1: read PEM private key done: type RSA
  debug1: Authentication succeeded (publickey).
  Authenticated to 98.98.98.98 ([98.98.98.98]:22).
  debug1: channel 0: new [client-session]
  debug1: Requesting no-more-sessions@openssh.com
  debug1: Entering interactive session.
  debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
  debug1: Sending environment.
  debug1: Sending env LANG = en_US.UTF-8
  ubuntu@magic-server:~$
  ```
---

* **3. Let me in!** - Add the given SSH public key below to your server so that we can connect using the `ubuntu` user.
---

* **4. Client configuration file (w/ Puppet)** - Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password. - `100-puppet_ssh_config.pp`.

  Requirements:

  * Your SSH client configuration must be configured to use the private key `~/.ssh/school`.
  * Your SSH client configuration must be configured to refuse to authenticate using a password.
  ```
  vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
  Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
  Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
  Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
  Notice: Finished catalog run in 0.03 seconds
  vagrant@ubuntu:~$
  ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
