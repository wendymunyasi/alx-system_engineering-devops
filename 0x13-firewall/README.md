# Project Name.
**0x13. Firewall**

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
Learn about firewalls.


* **0. Block all incoming traffic but** - Configure `ufw` so that it blocks all incoming traffic, except the TCP ports `22` (SSH), `443` (HTTPS SSL), `80` (HTTP). - `0-block_all_incoming_traffic_but`.
---

* **1. Port forwarding** - Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP` and paste ufw config settings in answer file. - `100-port_forwarding`.

    Terminal in `web-01`:
	```
	root@03-web-01:~# netstat -lpn
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2473/nginx
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      978/sshd
    tcp6       0      0 :::80                   :::*                    LISTEN      2473/nginx
    tcp6       0      0 :::22                   :::*                    LISTEN      978/sshd
    udp        0      0 0.0.0.0:68              0.0.0.0:*                           594/dhclient
    udp        0      0 0.0.0.0:54432           0.0.0.0:*                           594/dhclient
    udp6       0      0 :::32563                :::*                                594/dhclient
    Active UNIX domain sockets (only servers)
    Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
    unix  2      [ ACC ]     SEQPACKET  LISTENING     7175     433/systemd-udevd   /run/udev/control
    unix  2      [ ACC ]     STREAM     LISTENING     6505     1/init              @/com/ubuntu/upstart
    unix  2      [ ACC ]     STREAM     LISTENING     8048     741/dbus-daemon     /var/run/dbus/system_bus_socket
    unix  2      [ ACC ]     STREAM     LISTENING     8419     987/acpid           /var/run/acpid.socket
    root@03-web-01:~#
    root@03-web-01:~# grep listen /etc/nginx/sites-enabled/default
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;
        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #   listen 8000;
    #   listen somename:8080;
    #   listen 443;
    root@03-web-01:~#
    ```

    Terminal in `web-02`:

    ```
    ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:80
    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Tue, 07 Mar 2017 02:14:41 GMT
    Content-Type: text/html
    Content-Length: 612
    Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
    Connection: keep-alive
    ETag: "5315bd25-264"
    Accept-Ranges: bytes

    ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:8080
    HTTP/1.1 200 OK
    Server: nginx/1.4.6 (Ubuntu)
    Date: Tue, 07 Mar 2017 02:14:43 GMT
    Content-Type: text/html
    Content-Length: 612
    Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
    Connection: keep-alive
    ETag: "5315bd25-264"
    Accept-Ranges: bytes

    ubuntu@03-web-02:~$
    ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
