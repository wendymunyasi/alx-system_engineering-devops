# Project Name.
**0x08. Networking basics #1**

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


* **0. Change your home IP** - Write a Bash script that configures an Ubuntu server with the below requirements. - `0-change_your_home_IP`.
    *   `localhost` resolves to `127.0.0.2`.
    *   `facebook.com` resolves `to 8.8.8.8`.
    *   The checker is running on Docker.
    ```
    sylvain@ubuntu$ ping localhost
    PING localhost (127.0.0.1) 56(84) bytes of data.
    64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
    ^C
    --- localhost ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
    sylvain@ubuntu$
    sylvain@ubuntu$ ping facebook.com
    PING facebook.com (157.240.11.35) 56(84) bytes of data.
    64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
    ^C
    --- facebook.com ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
    sylvain@ubuntu$
    sylvain@ubuntu$ sudo ./0-change_your_home_IP
    sylvain@ubuntu$
    sylvain@ubuntu$ ping localhost
    PING localhost (127.0.0.2) 56(84) bytes of data.
    64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
    64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
    ^C
    --- localhost ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1000ms
    rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
    sylvain@ubuntu$
    sylvain@ubuntu$ ping facebook.com
    PING facebook.com (8.8.8.8) 56(84) bytes of data.
    64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
    ^C
    --- facebook.com ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
    ```
---

* **1. Show attached IPs** - Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on. - `1-show_attached_IPs`.
    ```
    sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
    10.0.2.15$
    127.0.0.1$
    sylvain@ubuntu$
    ```
---

* **2. Port listening on localhost** - Write a Bash script that listens on port `98` on `localhost`. - `100-port_listening_on_localhost`.

    **Terminal 0 - starting my script.**
    ```
    sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
    ```

    **Terminal 1 - Connecting to localhost on port `98` using `telnet` and typing some text.**
    ```
    sylvain@ubuntu$ telnet localhost 98
    Trying 127.0.0.2...
    Connected to localhost.
    Escape character is '^]'.
    Hello world
    test
    ```

    **Terminal 0 - Receiving the text on the other side.**
    ```
    sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
    Hello world
    test
    ```
---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
