# Project Name.
**0x03. Shell, init files, variables and expansions**

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
Practicing usage of shell variables, initialization files and arithmetic and various shell commands. What is expansion and how to use them.
What is the difference between single and double quotes and how to use them properly.
How to do command substitution with `$()` and backticks.
The `alias` Command.
How to create an alias.
How to list aliases.
How to temporarily disable an alias.


* **0. <o>** - Create a script that creates an alias.`0-alias`.
* **1. Hello you** - Create a script that prints `hello user`, where user is the current Linux user. - `1-hello_you`.
* **2. The path to success is to take massive, determined action** - Add `/action` to the `PATH. /action` should be the last directory the shell looks into when looking for a program.`2-path`.
* **3. If the path be beautiful, let us not ask where it leads** - Create a script that counts the number of directories in the `PATH`. - `3-paths`.
* **4. Global variables** - Create a script that lists environment variables. - `4-global_variables`.
* **5. Local variables** - Create a script that lists all local variables and environment variables, and functions. - `5-local_variables`.
* **6. Local variable** - Create a script that creates a new local variable. - `6-create_local_variable`.
* **7. Global variable** - Create a script that creates a new global variable. - `7-create_global_variable`.
* **8. Every addition to true knowledge is an addition to human power** - Write a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line. - `8-true_knowledge`.
* **9. Divide and rule** - Write a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line. - `9-divide_and_rule`.
* **10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath** - Write a script that displays the result of `BREATH` to the power `LOVE`. - `10-love_exponent_breath`.
* **11. There are 10 types of people in the world -- Those who understand binary, and those who don't** - Write a script that converts a number from base 2 to base 10. - `11-binary_to_decimal`.
* **12. Combination** - Create a script that prints all possible combinations of two letters, except `oo`. - `12-combinations`.
* **13. Floats** - Write a script that prints a number with two decimal places, followed by a new line. - `13-print_float`.
* **14. Decimal to Hexadecimal** - Write a script that displays the result of `BREATH` to the power `LOVE`. - `10-love_exponent_breath`.
---
* **15. Everyone is a proponent of strong encryption** - Write a script that converts a number from base 10 to base 16. - `100-decimal_to_hexadecimal`.
    ```
    julien@production-503e7013:~/shell/fun_with_the_shell$ cat quote
    "Everyone is a proponent of strong encryption."
    - Dorothy E. Denning
    julien@production-503e7013:~/shell/fun_with_the_shell$ ./101-rot13 < quote
    "Rirelbar vf n cebcbarag bs fgebat rapelcgvba."
    - Qbebgul R. Qraavat
    julien@production-503e7013:~/shell/fun_with_the_shell$
    ```
    ---
* **16. The eggs of the brood need to be an odd number** - Write a script that prints every other line from the input, starting with the first line. - `102-odd`.
    ```
    ubuntu@ip-172-31-63-244:/$ \ls -1
    bin
    boot
    dev
    etc
    home
    initrd.img
    lib
    lib32
    lib64
    libx32
    lost+found
    media
    mnt
    opt
    proc
    root
    run
    sbin
    srv
    sys
    t
    #t#
    t~
    tmp
    usr
    var
    vmlinuz
    whoareyou
    ubuntu@ip-172-31-63-244:/$ \ls -1 | ./102-odd
    bin
    dev
    home
    lib
    lib64
    lost+found
    mnt
    proc
    run
    srv
    t
    t~
    usr
    vmlinuz
    ubuntu@ip-172-31-63-244:/$
    ```
---
* **17. I'm an instant star. Just add water and stir.** - Write a shell script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result. - `WATER` is in base `water`. - `STIR` is in base `stir`. The result should be in base `bestchol`. - `103-water_and_stir`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
