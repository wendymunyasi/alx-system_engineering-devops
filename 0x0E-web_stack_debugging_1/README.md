# Project Name.
**0x0E. Web stack debugging #1**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   Your Puppet manifests must pass `Shellcheck` version 0.3.7 without any errors.
*   All your Bash script files must be executable.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.
*   You can’t use `systemctl` for restarting a process.
*   You are not allowed to use `wget`.

## Project Description.
Learn what is the main role of a web server.
What is a child process.
Why web servers usually have a parent process and child processes.
What are the main HTTP requests.
What DNS stands for and its main role.


* **0. Nginx likes port 80** - Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix. - `0-nginx_likes_port_80`.

  Requirements:

  * Nginx must be running, and listening on port `80` of all the server’s active IPv4 IPs.
  * Write a Bash script that configures a server to the above requirements.

  ```
  root@966c5664b21f:/# curl 0:80
	curl: (7) Failed to connect to 0 port 80: Connection refused
	root@966c5664b21f:/#
	root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
	root@966c5664b21f:/#
	root@966c5664b21f:/# curl 0:80
	<!DOCTYPE html>
	<html>
	<head>
	<title>Welcome to nginx!</title>
	<style>
			body {
					width: 35em;
					margin: 0 auto;
					font-family: Tahoma, Verdana, Arial, sans-serif;
			}
	</style>
	</head>
	<body>
	<h1>Welcome to nginx!</h1>
	<p>If you see this page, the nginx web server is successfully installed and
	working. Further configuration is required.</p>

	<p>For online documentation and support please refer to
	<a href="http://nginx.org/">nginx.org</a>.<br/>
	Commercial support is available at
	<a href="http://nginx.com/">nginx.com</a>.</p>

	<p><em>Thank you for using nginx.</em></p>
	</body>
	</html>
	root@966c5664b21f:/#
  ```
---

* **1. Make it sweet and short** - Using what you did for task #0, make your fix short and sweet. - `1-debugging_made_short`.

  Requirements:

  * Your Bash script must be 5 lines long or less.
  * There must be a new line at the end of the file.
  * You must respect usual Bash script requirements.
  * You cannot use `;`.
	* You cannot use `&&`.
	* You cannot execute your previous answer file (Do not include the name of the previous script in this one).
	* `service` (init) must say that `nginx` is not running ← for real.

  ```
  root@966c5664b21f:/# curl 0:80
	curl: (7) Failed to connect to 0 port 80: Connection refused
	root@966c5664b21f:/#
	root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
	5
	root@966c5664b21f:/# ./1-debugging_made_short
	root@966c5664b21f:/# curl 0:80
	<!DOCTYPE html>
	<html>
	<head>
	<title>Welcome to nginx!</title>
	<style>
			body {
					width: 35em;
					margin: 0 auto;
					font-family: Tahoma, Verdana, Arial, sans-serif;
			}
	</style>
	</head>
	<body>
	<h1>Welcome to nginx!</h1>
	<p>If you see this page, the nginx web server is successfully installed and
	working. Further configuration is required.</p>

	<p>For online documentation and support please refer to
	<a href="http://nginx.org/">nginx.org</a>.<br/>
	Commercial support is available at
	<a href="http://nginx.com/">nginx.com</a>.</p>

	<p><em>Thank you for using nginx.</em></p>
	</body>
	</html>
	root@966c5664b21f:/#
	root@966c5664b21f:/# service nginx status
	* nginx is not running
	root@966c5664b21f:/#
  ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
