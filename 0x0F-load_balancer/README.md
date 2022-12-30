# Project Name.
**0x0F. Load balancer**

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


* **0. Double the number of webservers** - Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks. - `0-custom_http_response_header`.

	Requirements:

	*	Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02):
		*	The name of the custom HTTP header must be X-Served-By.
		*	The value of the custom HTTP header must be the hostname of the server Nginx is running on.
	*	Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task.
		*	Ignore SC2154 for shellcheck.

	Example
  ```
  sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
	X-Served-By: 03-web-01
	sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
	X-Served-By: 03-web-02
	sylvain@ubuntu$
  ```
---

* **1. Install your load balancer** - Install and configure HAproxy on your lb-01 server. - `1-install_load_balancer`.

	Requirements:

	*	Configure HAproxy so that it send traffic to web-01 and web-02.
	*	Distribute requests using a roundrobin algorithm.
	*	Make sure that HAproxy can be managed via an init script.
	*	Make sure that your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02. If not, follow this [tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html).
	*	For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements.

	Example:
	```
  sylvain@ubuntu$ curl -Is 54.210.47.110
	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Mon, 27 Feb 2017 06:12:17 GMT
	Content-Type: text/html
	Content-Length: 30
	Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
	Connection: keep-alive
	ETag: "58abea7c-1e"
	X-Served-By: 03-web-01
	Accept-Ranges: bytes

	sylvain@ubuntu$ curl -Is 54.210.47.110
	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Mon, 27 Feb 2017 06:12:19 GMT
	Content-Type: text/html
	Content-Length: 612
	Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
	Connection: keep-alive
	ETag: "5315bd25-264"
	X-Served-By: 03-web-02
	Accept-Ranges: bytes

	sylvain@ubuntu$
  ```
---

* **2. Add a custom HTTP header with Puppet** - Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet. - `2-puppet_custom_http_response_header.pp`.

	Requirements:

	*	The name of the custom HTTP header must be X-Served-By.
	*	The value of the custom HTTP header must be the hostname of the server Nginx is running on.
	*	Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task.

---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
