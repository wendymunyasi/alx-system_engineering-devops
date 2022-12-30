# Project Name.
**0x0C. Web server**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   Your bash scripts must pass `Shellcheck` version 0.3.7 without any errors.
*   All your Bash script files must be executable.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.
*   You can’t use `systemctl` for restarting a process.

## Project Description.
Learn what is the main role of a web server.
What is a child process.
Why web servers usually have a parent process and child processes.
What are the main HTTP requests.
What DNS stands for and its main role.


* **0. Transfer a file to your server** - Write a Bash script that transfers a file from our client to a server. - `0-transfer_file`.

  Requirements:

  * Accepts 4 parameters:
    * The path to the file to be transferred.
    * The IP of the server we want to transfer the file to.
    * The username `scp` connects with.
    * The path to the SSH private key that `scp` uses.
  * Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed.
  * `scp` must transfer the file to the user home directory `~/`.
  * Strict host key checking must be disabled when using `scp`.
  ```
  sylvain@ubuntu$ ./0-transfer_file
  Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
  sylvain@ubuntu$
  sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
  afile
  sylvain@ubuntu$ 
  sylvain@ubuntu$ touch some_page.html
  sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
  some_page.html                                     100%   12     0.1KB/s   00:00
  sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
  afile
  some_page.html
  sylvain@ubuntu$
  ```
  In this example, I:

  * remotely execute the `ls ~/` command via `ssh` to see what `~/` contains.
  * create a file named `some_page.html`.
  * execute my `0-transfer_file` script.
  * remotely execute the `ls ~/` command via `ssh` to see that the file `some_page.html` has been successfully transferred.
  
  That is one way of publishing your website pages to your server.

---

* **1. Install nginx web server** - Install `nginx` on your `web-01` server. - `1-install_nginx_web_server`.

  Requirements:

  * Install `nginx` on your `web-01` server.
  * Nginx should be listening on port `80`.
  * When querying Nginx at its root `/` with a `GET` request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`.
  * You can’t use `systemctl` for restarting `nginx`.

  **Server terminal**:
  ```
  root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
  root@sy-web-01$ 
  root@sy-web-01$ curl localhost
  Hello World!
  root@sy-web-01$ 
  ```

  **Local terminal:**:
  ```
  sylvain@ubuntu$ curl 34.198.248.145/
  Hello World!
  sylvain@ubuntu$ curl -sI 34.198.248.145/
  HTTP/1.1 200 OK
  Server: nginx/1.4.6 (Ubuntu)
  Date: Tue, 21 Feb 2017 23:43:22 GMT
  Content-Type: text/html
  Content-Length: 30
  Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
  Connection: keep-alive
  ETag: "58abea7c-1e"
  Accept-Ranges: bytes
  ```
---

* **2. Setup a domain name** - Create your domain name and configure your DNS records with an A entry so that your root domain points to your web-01 IP address.  `2-setup_a_domain_name`.

  ```
  sylvain@ubuntu$ cat 2-setup_a_domain_name
  myschool.tech
  sylvain@ubuntu$
  sylvain@ubuntu$ dig myschool.tech

  ; <<>> DiG 9.10.6 <<>> myschool.tech
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 512
  ;; QUESTION SECTION:
  ;myschool.tech.     IN  A

  ;; ANSWER SECTION:
  myschool.tech.  7199    IN  A   184.72.193.201

  ;; Query time: 65 msec
  ;; SERVER: 8.8.8.8#53(8.8.8.8)
  ;; WHEN: Fri Aug 02 09:44:36 PDT 2019
  ;; MSG SIZE  rcvd: 65

  sylvain@ubuntu$
  ```
---

* **3. Redirection** - Configure your Nginx server so that `/redirect_me` is redirecting to another page. - `3-redirection`.

  Requirements:

  * The redirection must be a “301 Moved Permanently”.
  * You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements.
  * Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task.

  ```
  sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
  HTTP/1.1 301 Moved Permanently
  Server: nginx/1.4.6 (Ubuntu)
  Date: Tue, 21 Feb 2017 21:36:04 GMT
  Content-Type: text/html
  Content-Length: 193
  Connection: keep-alive
  Location: https://www.youtube.com/watch?v=QH2-TGUlwu4
  ```
---

* **4. Not found page 404** - Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`. - `100-puppet_ssh_config.pp`.

  Requirements:

  * The page must return an HTTP `404` error code.
  * The page must contain the string `Ceci n'est pas une page`.
  * Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task.
  ```
  sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
  HTTP/1.1 404 Not Found
  Server: nginx/1.4.6 (Ubuntu)
  Date: Tue, 21 Feb 2017 21:46:43 GMT
  Content-Type: text/html
  Content-Length: 26
  Connection: keep-alive
  ETag: "58acb50e-1a"

  sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
  Ceci n'est pas une page

  sylvain@ubuntu$
  ```
---

* **5. Install Nginx web server (w/ Puppet)** - Time to practice configuring your server with Puppet!. Install and configure an Nginx server using Puppet instead of Bash. - `7-puppet_install_nginx_web_server.pp`.

  Requirements:

  * Nginx should be listening on port `80`.
  * When querying Nginx at its root `/` with a `GET` request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`.
  * The redirection must be a "301 Moved Permanently".
---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
