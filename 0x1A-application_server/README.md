# Project Name.
**0x1A. Application server**

## Author's Details.
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel:*+254707240068.*

##  Requirements

*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   All your Bash script files must be executable.
*   Your Bash scripts must pass `Shellcheck` without any error.
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
*   The second line of all your Bash scripts should be a comment explaining what is the script doing.


## Project Description.

* **0. Set up development with Python** - Serve what you built for `AirBnB clone v2 - Web framework` on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

	Requirements:

	*	Make sure that `task #3` of your `SSH project`[(https://github.com/wendymunyasi/alx-system_engineering-devops/tree/master/0x0B-ssh)] is completed for `web-01`. The checker will connect to your servers.
	*	Git clone your `AirBnB_clone_v2` on your `web-01` server.
	*	Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`.

	Example:

  **Window 1:**
  ```
  ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
  * Serving Flask app "0-hello_route" (lazy loading)
  * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
  * Debug mode: off
  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
  35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
  ```

  **Window 2:**
  ```
  ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
  Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
  ```
---

* **1. Set up production with Gunicorn** - Get your production application server set up with `Gunicorn` on `web-01`, port `5000`.

---

* **2. Serve a page with Nginx** - Building on your work in the previous tasks, configure `Nginx` to serve your page from the route `/airbnb-onepage/`.

	Requirements:

	*	`Nginx` must serve this page both locally and on its public IP on port `80`.
	*	`Nginx` should proxy requests to the process listening on port `5000`.
	*	Include your `Nginx` config file as `2-app_server-nginx_config`.

---

* **3. Add a route with query parameters** - In `AirBnB_clone_v2/web_flask/6-number_odd_or_even`, the route `/number_odd_or_even/<int:n>` should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure `Nginx` to proxy HTTP requests to the route` /airbnb-dynamic/number_odd_or_even/`(any integer) to a Gunicorn instance listening on port `5001`. Include your `Nginx` config file as `3-app_server-nginx_config`.

---

* **4. Let's do this for your API** - Serve what you built for `AirBnB clone v3` - RESTful API on `web-01`. Upload your Nginx config file as `4-app_server-nginx_config`.

---

* **5. Serve your AirBnB clone** - Serve what you built for `AirBnB clone - Web dynamic` on `web-01`. Upload your Nginx config file as `5-app_server-nginx_config`.

---


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
