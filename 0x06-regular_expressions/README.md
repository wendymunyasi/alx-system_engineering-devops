# Project Name.
**0x06. Regular expression**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

### Shell Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be tested on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   All your bash scripts must be executable.
*   Your Bash script must pass `shellcheck` without any error.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.
*   All your regex must be built for the **Oniguruma** library.
*   Each script accepts one argument and pass it to a regular expression matching method.

## Project Description.
Learn about regular expressions and building them using **Oniguruma** library which uses **Ruby** by default.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

* **0. Simply matching School** - The regular expression must match `School`. - `0-simply_match_school.rb`.
* **1. Repetition Token #0** - The regular expression must match the given cases. - `1-repetition_token_0.rb`.
* **2. Repetition Token #1** - The regular expression must match the given cases. - `2-repetition_token_1.rb`.
* **3. Repetition Token #2** - The regular expression must match the given cases. - `3-repetition_token_2.rb`.
* **4. Repetition Token #3** - The regular expression must match the given cases. - `4-repetition_token_3.rb`.
---

* **5. Not quite HBTN yet** - The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between. - `5-beginning_and_end.rb`.
    ```
    sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
    $
    sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
    hbn$
    sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
    $
    sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
    h8n$
    sylvain@ubuntu$
    $
    ```
---

* **6. Call me maybe** - The regular expression must match a 10 digit phone number. - `6-phone_number.rb`.
    ```
    sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
    4155049898$
    sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
    $
    sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
    $
    sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
    $
    sylvain@ubuntu$
    ```
---

* **7. OMG WHY ARE YOU SHOUTING?** - TThe regular expression must be only matching: capital letters. - `7-OMG_WHY_ARE_YOU_SHOUTING.rb`.
    ```
    sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
    ILOVESYSADMIN$
    sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
    WHATSAY$
    sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
    $
    sylvain@ubuntu$
    ```
---

* **8. Textme** - Your script should output: `[SENDER],[RECEIVER],[FLAGS]`. -`100-textme.rb`.
    *   The sender phone number or name (including country code if present).
    *   The receiver phone number or name (including country code if present).
    *   The flags that were used.
    ```
    $ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
    Google,+16474951758,-1:0:-1:0:-1
    $
    $
    $ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
    +17272713208,+19172319348,-1:0:-1:0:-1
    $
    $ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
    18572406905,14022180266,-1:0:-1:-1:-1
    $
    $
    $ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
    12392190384,19148265919,-1:0:-1:-1:-1
    $
    ```

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
