# Project Name.
**0x00. Shell, basics**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

### Bash Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be tested on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   All your scripts should be exactly two lines long (`$ wc -l file` should print 2).
*   The first line of all your Bash scripts should be exactly `#!/bin/bash`.
*   All your bash scripts must be executable.
*   You are not allowed to use `bc`, `sed` or`awk`.
*   You are not allowed to use `&&`, `||` or `;`.

## Project Description.
Learn shell navigation commands such as `cd`, `pwd` and `ls`.
How to manipulate files/directories using `cp`, `mv`, `rm` and `mkdir`.
What do the commands `ls`, `less`, `file` do.
How do you use options and arguments with commands.
What is a symbolic link.
What is a hard link.
What is the difference between a hard link and a symbolic link.

* **0. Where am I?** - Write a script that prints the absolute path name of the current working directory. - `0-current_working_directory`.
* **1. What’s in there?** - Write a script that displays the contents list of your current directory. - `1-listit`.
* **2. There is no place like home** - Write a script that changes the working directory to the user’s home directory. - `2-hellofile`.
* **3. The long format** - Write a script that displays current directory contents in a long format. - `3-listfiles`.
* **4. Hidden files** - Write a script that displays current directory contents, including hidden files (starting with `.`). Use the long format. - `4-listmorefiles`.
* **5. I love numbers** - Write a script that displays current directory contents using long format with user and group IDs displayed numerically and hidden files (starting with `.`). - `5-listfilesdigitonly`.
* **6. Welcome** - Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory. - `6-firstdirectory`.
* **7. Betty in my first directory** - Write a script that moves the file `betty` from `/tmp/` to   `/tmp/my_first_directory`. - `7-movethatfile`.
* **8. Bye bye Betty** - Write a script that deletes the file `betty` from `/tmp/my_first_directory`. - `8-firstdelete`.
* **9. Bye bye My first directory** - Write a script that deletes the directory `my_first_directory` that is in the `/tmp` directory. - `9-firstdirdeletion`.
* **10. Back to the future** - Write a script that changes the working directory to the previous one. - `10-back`.
* **11. Lists** - Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format. - `11-lists`.
* **12. File type** - Write a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script. - `12-file_type`.
* **13. We are symbols, and inhabit symbols** - Write a script that creates a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory. - `13-symbolic_link`.
* **14. Copy HTML files** - Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. - `14-copy_html`.
* **15. Let’s move** - Create a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`. You can assume that the directory `/tmp/u` will exist when we will run your script. - `100-lets_move`.
* **16. Clean Emacs** - Create a script that deletes all files in the current working directory that end with the character `~`. - `101-clean_emacs`.
* **17. Tree** - Create a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory. - `102-tree`.
---
* **18. Life is a series of commas, not periods** - Write a script that lists all the files and directories of the current directory, separated by commas (`,`). - `103-commas`.
    *   Directory names should end with a slash (`/`).
    *   Files and directories starting with a dot (`.`) should be listed.
    *   The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning.
    *   Only digits and letters are used to sort; Digits should come first.
    *   You can assume that all the files we will test with will have at least one letter or one digit.
    *   The listing should end with a new line.
---
* **19. File type: School** - Create a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. - `School` data files always contain the string `SCHOOL` at offset 0. - `school.mgc`.
    ```
    ubuntu@ip-172-31-63-244:/tmp/magic$ cp /bin/ls .
    ubuntu@ip-172-31-63-244:/tmp/magic$ ls -la
    total 268
    drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
    drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
    -rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 school.mgc
    -rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
    -rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisaschoolfile
    -rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
    ubuntu@ip-172-31-63-244:/tmp/magic$ file --mime-type -m school.mgc *
    school.mgc:         application/octet-stream
    ls:                    application/octet-stream
    thisisaschoolfile: School
    thisisatextfile:       text/plain
    ubuntu@ip-172-31-63-244:/tmp/magic$ file -m school.mgc *
    school.mgc:         data
    ls:                    data
    thisisaschoolfile: School data
    thisisatextfile:       ASCII text
    ubuntu@ip-172-31-63-244:/tmp/magic$
    ```


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
