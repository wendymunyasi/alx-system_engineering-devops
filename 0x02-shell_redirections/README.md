# Project Name.
**0x02. Shell, I/O Redirections and filters**

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
Learn what do the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr` do.
How to redirect standard output to a file.
How to get standard input from a file instead of the keyboard.
How to send the output from one program to the input of another program.
How to combine commands and filters with redirections.
What are special characters.
What is the `/etc/passwd` file and what is its format.
What is the `/etc/shadow` file and what is its format.

* **0. Hello World** - Write a script that prints “Hello, World”, followed by a new line to the standard output. - `0-hello_world`.
* **1. Confused smiley** - Write a script that displays a confused smiley `"(Ôo)'`. - `1-confused_smiley`.
* **2. Let's display a file** - Write a script that displays the content of the `/etc/passwd` file. - `2-hellofile`.
* **3. What about 2?** - Display the content of `/etc/passwd` and `/etc/hosts`. - `3-twofiles`.
* **4. Last lines of a file** - Write a script that displays the last 10 lines of `/etc/passwd`. - `4-lastlines`.
* **5. I'd prefer the first ones actually** - Write a script that displays the first 10 lines of `/etc/passwd`. - `5. I'd prefer the first ones actually`.
* **6. Line #2** - Write a script that displays the third line of the file `iacta`. - `6. Line #2`.
* **7. It is a good file that cuts iron without making a noise** - Write a shell script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line. - `7-file`.
* **8. Save current state of directory** - Write a script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it. - `8-cwd_state`.
* **9. Duplicate last line** - Write a script that duplicates the last line of the file `iacta`. - `9-duplicate_last_line`.
* **10. No more javascript** - Write a script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders. - `10-no_more_js`.
* **11. Don't just count your directories, make your directories count** - Write a script that counts the number of directories and sub-directories in the current directory. - `11-directories`.
* **12. What’s new** - Create a script that displays the 10 newest files in the current directory. - `12-newest_files`.
* **13. Being unique is better than being perfect** - Create a script that takes a list of words as input and prints only words that appear exactly once. - `13-unique`.
* **14. It must be in that file** - Write a script that displays lines containing the pattern “root” from the file `/etc/passwd`. - `14-findthatword`.
* **15. Count that word** - Write a script that displays the number of lines that contain the pattern “bin” in the file `/etc/passwd`. - `15-countthatword`.
* **16. What's next?** - Write a script that displays lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`. - `16-whatsnext`.
* **17. I hate bins** - Write a script that displays all the lines in the file `/etc/passwd` that do not contain the pattern “bin”. - `17-hidethisword`.
* **18. Letters only please** - Write a script that displays all lines of the file `/etc/ssh/sshd_config` starting with a letter. - `18-letteronly`.
* **19. A to Z** - Write a script that replaces all characters `A` and `c` from input to `Z` and `e` respectively. - `19-AZ`.
---
* **20. Without C, you would live in hiago** - Create a script that removes all letters `c` and `C` from input. - `20-hiago`.
    ```
    julien@ubuntu:/tmp/0x02$ echo Chicago | ./20-hiago 
    hiago
    julien@ubuntu:/tmp/0x02$ 
    ```
---
* **21. esreveR** - Write a script that reverse its input. - `21-reverse`.
* **22. DJ Cut Killer** - Write a script that displays all users and their home directories, sorted by users. Based on the the `/etc/passwd` file. - `22-users_and_homes`.
---
* **23. Empty casks make the most noise** - Write a command that finds all empty files and directories in the current directory and all sub-directories with the given conditions. - `100-empty_casks`.
    ```
    ubuntu@ip-172-31-63-244:~/0x02-shell_redirections$ ls -laR
    .:
    total 64
    drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 .
    drwxrwxr-x 7 ubuntu ubuntu 4096 Sep 29 21:36 ..
    -rwxrwxr-x 1 ubuntu ubuntu   56 Feb  8  2016 0-commas
    drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 0-commas-checks
    -rwxrwxr-x 1 ubuntu ubuntu   48 Feb  8  2016 1-empty_casks
    -rwxrwxr-x 1 ubuntu ubuntu   68 Feb  8  2016 2-gifs
    -rwxrwxr-x 1 ubuntu ubuntu   47 Feb  8  2016 3-directories
    -rwxrwxr-x 1 ubuntu ubuntu   41 Feb  8  2016 4-zeros
    -rwxrwxr-x 1 ubuntu ubuntu   43 Feb  8  2016 5-rot13
    -rwxrwxr-x 1 ubuntu ubuntu   25 Feb  8  2016 6-odd
    -rwxrwxr-x 1 ubuntu ubuntu   73 Feb  8  2016 7-sort_rot13
    -rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:46 ........gif
    -rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:47 ..hello.gif
    drwxrwxr-x 2 ubuntu ubuntu 4096 Oct  7 00:41 javascript
    -rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:48 Kris_is_awesome :)
    -rw-rw-r-- 1 ubuntu ubuntu   14 Feb  8  2016 Makefile
    -rw-rw-r-- 1 ubuntu ubuntu   69 Feb  8  2016 quote
    -rw-rw-r-- 1 ubuntu ubuntu    0 Oct  7 00:24 Rona_napping.gif
    -rw-rw-r-- 1 ubuntu ubuntu    0 Oct  6 23:59 root.gif
    -rw-rw-r-- 1 ubuntu ubuntu    0 Mar 24  2016 ..something
    drwxrwxr-x 3 ubuntu ubuntu 4096 Feb  8  2016 test_dir
    -rwxrwxr-x 1 ubuntu ubuntu   54 Feb  8  2016 test.var

    ./0-commas-checks:
    total 16
    drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 .
    drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 ..
    -rw-rw-r-- 1 ubuntu ubuntu 1361 Feb  8  2016 28-check.php
    -rw-rw-r-- 1 ubuntu ubuntu  481 Feb  8  2016 28-check.php~

    ./javascript:
    total 8
    drwxrwxr-x 2 ubuntu ubuntu 4096 Oct  7 00:41 .
    drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 ..

    ./test_dir:
    total 12
    drwxrwxr-x 3 ubuntu ubuntu 4096 Feb  8  2016 .
    drwxrwxr-x 5 ubuntu ubuntu 4096 Oct  7 00:48 ..
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 docker.gif
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 file.sh
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 .horrible_selfie.gif
    drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 photos
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 README.md

    ./test_dir/photos:
    total 8
    drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  8  2016 .
    drwxrwxr-x 3 ubuntu ubuntu 4096 Feb  8  2016 ..
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 cat.gif
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 index.html
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 main.gif
    -rw-rw-r-- 1 ubuntu ubuntu    0 Feb  8  2016 rudy_rigot.gif
    ubuntu@ip-172-31-63-244:~/0x02-shell_redirections$ ./100-empty_casks
    Rona_napping.gif
    javascript
    root.gif
    ..something
    Kris_is_awesome :)
    ..hello.gif
    file.sh
    docker.gif
    README.md
    index.html
    main.gif
    cat.gif
    rudy_rigot.gif
    .horrible_selfie.gif
    ........gif
    ubuntu@ip-172-31-63-244:~/0x02-shell_redirections$
    ```
---
* **24. A gif is worth ten thousand words** - Write a script that lists all the files with a `.gif` extension in the current directory and all its sub-directories with the given conditions. - `101-gifs`.
    ```
    julien@production-503e7013:~/shell/fun_with_the_shell$ ls -Rla
    .:
    total 28
    drwxrwxr-x 3 julien julien 4096 Jan 20 03:35 .
    drwxrwxr-x 3 julien julien 4096 Jan 20 02:58 ..
    -rwxr--r-- 1 julien julien 43 Jan 20 02:59 0-commas
    -rwxr--r-- 1 julien julien 47 Jan 20 02:50 1-empty_casks
    -rwxrw-r-- 1 julien julien 68 Jan 20 03:35 2-gifs
    -rw-rw-r-- 1 julien julien 14 Jan 20 03:35 Makefile
    drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 test_dir

    ./test_dir:
    total 16
    drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 .
    drwxrwxr-x 3 julien julien 4096 Jan 20 03:35 ..
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:40 .horrible_selfie.gif
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:23 README.md
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:17 docker.gif
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:17 file.sh
    drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 photos
    drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 rep.gif

    ./test_dir/photos:
    total 8
    drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 .
    drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 ..
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:23 cat.gif
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:22 index.html
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:23 main.gif
    -rw-rw-r-- 1 julien julien 0 Jan 20 03:23 Electra_napping.gif

    ./test_dir/rep.gif:
    total 8
    drwxrwxr-x 2 julien julien 4096 Jan 20 03:23 .
    drwxrwxr-x 4 julien julien 4096 Jan 20 03:42 ..
    julien@production-503e7013:~/shell/fun_with_the_shell$ ./101-gifs
    .horrible_selfie
    cat
    docker
    Electra_napping
    main
    julien@production-503e7013:~/shell/fun_with_the_shell$
    ```
---
* **25. Acrostic** - Create a script that decodes acrostics that use the first letter of each line. - `102-acrostic`.
    ```
    julien@ubuntu:/tmp/0x02$ cat An\ Acrostic 
    Elizabeth it is in vain you say
    Love not"—thou sayest it in so sweet a way:
    In vain those words from thee or L.E.L.
    Zantippe's talents had enforced so well:
    Ah! if that language from thy heart arise,
    Breath it less gently forth—and veil thine eyes.
    Endymion, recollect, when Luna tried
    To cure his love—was cured of all beside—
    His follie—pride—and passion—for he died.
    julien@ubuntu:/tmp/0x02$ ./102-acrostic < An\ Acrostic 
    ELIZABETH
    julien@ubuntu:/tmp/0x02$ 
    ```
---
* **26. The biggest fan** - Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests. Order by number of requests, most active host or IP at the top. - `103-the_biggest_fan`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
