# Project Name.
**0x16. API advanced**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   You must use the Requests module for sending HTTP requests to the Reddit API.


## Project Description.
Learn how to read API documentation to find the endpoints you’re looking for
How to use an API with pagination. 
How to parse JSON results from an API.
How to make a recursive API call.
How to sort a dictionary by value.


* **0. How many subs?** - Write a function that queries the Reddit API[(https://www.reddit.com/dev/api/)] and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0. - `0-subs.py`.

  Requirements:

  * Prototype: `def number_of_subscribers(subreddit)`.
  * If not a valid subreddit, return 0.
  * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
  
  Example:
  ```
  wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
  756024
  wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
  0
  ```
---

* **1. Top Ten** - Write a function that queries the Reddit API[(https://www.reddit.com/dev/api/)] and prints the titles of the first 10 hot posts listed for a given subreddit. - `1-top_ten.py`.

  Requirements:

  * Prototype: `def top_ten(subreddit)`.
  * If not a valid subreddit, print None.
  * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

  Example:
  ```
  wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
  756024
  wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
  0
  ```
---

* **2. Recurse it!** - Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None. - `2-recurse.py`.

  Requirements:

  * Prototype: `def recurse(subreddit, hot_list=[])`.
  * Follow previous tasks requirements.

  Example:
  ```
  wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py programming
  932
  wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit
  None
  ```
---

* **3. Count it!** - Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. `Javascript` should count as `javascript`, but `java` should not). - `100-count.py`.

  Requirements:

  * Prototype: `def count_words(subreddit, word_list)`.
  * Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
  * If `word_list` contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with `java`).
  * Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
  * Results are based on the number of times a keyword appears, not titles it appears in. `java java java` counts as 3 separate occurrences of `java`.
  * To make life easier, `java.` or `java!` or `java_` should not count as `java`
  * If no posts match or the subreddit is invalid, print nothing.
  * Follow previous tasks requirements.

  Example:
  ```
  bob@dylan $ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
  java: 27
  javascript: 20
  python: 17
  react: 17
  scala: 4
  bob@dylan $ python3 100-main.py programming 'JavA java'
  java: 54
  bob@dylan $ python3 100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
  bob@dylan $ python3 100-main.py not_a_valid_subreddit 'python java'
  bob@dylan $ 
  ```
---

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
