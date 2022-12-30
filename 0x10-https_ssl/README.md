# Project Name.
**0x10. HTTPS SSL**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

### Bash Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   All your bash scripts must be executable.
*   Your Bash script must pass `shellcheck` without any error.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.

## Project Description.
Learn what is localhost/127.0.0.1.
What is 0.0.0.0.
What is `/etc/hosts`.
How to display your machine’s active network interfaces.


* **0. World wide web** - Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains. - `0-world_wide_web`.

	**Example**
	```
	sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
	;; ANSWER SECTION:
	www.holberton.online.   87  IN  A   54.210.47.110
	sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
	;; ANSWER SECTION:
	lb-01.holberton.online. 101 IN  A   54.210.47.110
	sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
	;; ANSWER SECTION:
	web-01.holberton.online. 212    IN  A   34.198.248.145
	sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
	;; ANSWER SECTION:
	web-02.holberton.online. 298    IN  A   54.89.38.100
	sylvain@ubuntu$
	sylvain@ubuntu$
	sylvain@ubuntu$ ./0-world_wide_web holberton.online
	The subdomain www is a A record and points to 54.210.47.110
	The subdomain lb-01 is a A record and points to 54.210.47.110
	The subdomain web-01 is a A record and points to 34.198.248.145
	The subdomain web-02 is a A record and points to 54.89.38.100
	sylvain@ubuntu$
	sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
	The subdomain web-02 is a A record and points to 54.89.38.100
	sylvain@ubuntu$
	```
---

* **1. HAproxy SSL termination** - Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain `www`. - `1-haproxy_ssl_termination`.

	Requirements:
	
	*	HAproxy must be listening on port TCP 443.
	*	HAproxy must be accepting SSL traffic.
	*	HAproxy must serve encrypted traffic that will return the `/` of your web server.
	* When querying the root of your domain name, the page returned must contain `Holberton School`.

	```
	sylvain@ubuntu$ curl -sI https://www.holberton.online
	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Tue, 28 Feb 2017 01:52:04 GMT
	Content-Type: text/html
	Content-Length: 30
	Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
	ETag: "58abea7c-1e"
	X-Served-By: 03-web-01
	Accept-Ranges: bytes
	sylvain@ubuntu$
	sylvain@ubuntu$ curl https://www.holberton.online
	Holberton School for the win!
	sylvain@ubuntu$
  ```
---

* **2. No loophole in your website traffic** -  Configure HAproxy to automatically redirect HTTP traffic to HTTPS. - `100-redirect_http_to_https`.

	```
	sylvain@ubuntu$ curl -sIL http://www.holberton.online
	HTTP/1.1 301 Moved Permanently
	Content-length: 0
	Location: https://www.holberton.online/
	Connection: close

	HTTP/1.1 200 OK
	Server: nginx/1.4.6 (Ubuntu)
	Date: Tue, 28 Feb 2017 02:19:18 GMT
	Content-Type: text/html
	Content-Length: 30
	Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
	ETag: "58abea7c-1e"
	X-Served-By: 03-web-01
	Accept-Ranges: bytes

	sylvain@ubuntu$
	```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
