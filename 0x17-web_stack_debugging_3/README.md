# Project Name.
**0x17. Web stack debugging #3**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04LTS.
*   All your files should end with a new line.
*   Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
*   Your Puppet manifests must run without error.
*   Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
*   Your Puppet manifests files must end with the extension `.pp`.
*   Files will be checked with Puppet v3.4.


## Install puppet-lint
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Project Description.

* **0. Strace is your friend** - Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing). - `0-subs.py`.

  Hint:

  * `strac`e can attach to a current running process.
  * You can use `tmux` to run `strace` in one window and `curl` in another one.

  Requirements:

  * Your `0-strace_is_your_friend.pp` file must contain Puppet code.
  * You can use whatever Puppet resource type you want for you fix.
  
  Example:
  ```
  root@e514b399d69d:~# curl -sI 127.0.0.1
  HTTP/1.0 500 Internal Server Error
  Date: Fri, 24 Mar 2017 07:32:16 GMT
  Server: Apache/2.4.7 (Ubuntu)
  X-Powered-By: PHP/5.5.9-1ubuntu4.21
  Connection: close
  Content-Type: text/html

  root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
  Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
  Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
  Notice: Finished catalog run in 0.08 seconds
  root@e514b399d69d:~# curl -sI 127.0.0.1:80
  root@e514b399d69d:~#
  HTTP/1.1 200 OK
  Date: Fri, 24 Mar 2017 07:11:52 GMT
  Server: Apache/2.4.7 (Ubuntu)
  X-Powered-By: PHP/5.5.9-1ubuntu4.21
  Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
  Content-Type: text/html; charset=UTF-8

  root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
  <title>Holberton &#8211; Just another WordPress site</title>
  <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
  <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
          <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                              <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
          <p>Yet another bug by a Holberton student</p>
  root@e514b399d69d:~#
  ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
