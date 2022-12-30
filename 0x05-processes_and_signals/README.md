# Project Name.
**0x05. Processes and signals**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

### Bash Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be tested on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   All your bash scripts must be executable.
*   Your Bash script must pass `shellcheck` without any error.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.

## Project Description.
Learn what is a PID.
What is a process.
How to find a process’ PID.
How to kill a process.
What is a signal.
What are the 2 signals that cannot be ignored.


* **0. What is my PID** - Write a Bash script that displays its own PID. - `0-what-is-my-pid`.
* **1. List your processes** - Write a Bash script that displays a list of currently running processes with the given requirements. - `1-list_your_processes`.
* **2. Show your Bash PID** - Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process. - `2-show_your_bash_pid`.
* **3. Show your Bash PID made easy** - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`. - `3-show_your_bash_pid_made_easy`.
* **4. To infinity and beyond** - Write a Bash script that displays To infinity and beyond indefinitely with the given requirements. - `4-to_infinity_and_beyond`.
* **5. Don't stop me now!** - Write a Bash script that stops `4-to_infinity_and_beyond` process. -`5-dont_stop_me_now`.
* **6. Stop me if you can** - Write a Bash script that stops `4-to_infinity_and_beyond` process. - `6-stop_me_if_you_can`.
* **7. Highlander** - Write a Bash script that displays `To infinity and beyond` indefinitely, `I am invincible!!!` when receiving a SIGTERM signal with the given requirements. - `7-highlander`.
* **8. Beheaded process** - Write a Bash script that kills the process `7-highlander`. - `8-beheaded_process`.
---
* **9. Process and PID file** - Write a Bash script that does the following:

    *   Creates the file `/var/run/myscript.pid` containing its PID.
    *   Displays `To infinity and beyond` indefinitely.
    *   Displays `I hate the kill command` when receiving a SIGTERM signal.
    *   Displays `Y U no love me?!` when receiving a SIGINT signal.
    *   Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal.

    File: `100-process_and_pid_file`
---
* **10. Manage my process** - Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. - `101-manage_my_process`, `manage_my_process`.
    ```
    sylvain@ubuntu$ sudo ./101-manage_my_process
    Usage: manage_my_process {start|stop|restart}
    sylvain@ubuntu$ sudo ./101-manage_my_process start
    manage_my_process started
    sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
    I am alive!
    I am alive!
    I am alive!
    I am alive!
    ^C
    sylvain@ubuntu$ sudo ./101-manage_my_process stop
    manage_my_process stopped
    sylvain@ubuntu$ cat /var/run/my_process.pid 
    cat: /var/run/my_process.pid: No such file or directory
    sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
    ^C
    sylvain@ubuntu$ sudo ./101-manage_my_process start
    manage_my_process started
    sylvain@ubuntu$ cat /var/run/my_process.pid 
    11864
    sylvain@ubuntu$ sudo ./101-manage_my_process restart
    manage_my_process restarted
    sylvain@ubuntu$ cat /var/run/my_process.pid 
    11918
    sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
    I am alive!
    I am alive!
    I am alive!
    ^C
    sylvain@ubuntu$
    ```
---

* **11. Zombie** - Write a C program that creates 5 zombie processes. - `102-zombie.c`.
    *   For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`.
    *   When your code is done creating the parent process and the zombies, use the function below:
    ```
    int infinite_while(void)
    {
        while (1)
        {
            sleep(1);
        }
        return (0);
    }
    ```
---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
