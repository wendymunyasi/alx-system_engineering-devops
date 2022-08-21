# Web infrastructure design

## 2. Secured and monitored web infrastructure

### Issues with this infrastructure

- **Terminating SSL at the load balancer level is an issue.** <br />
    The traffic between the load-balancer and the server is unencrypted and, therefore, is vulnerable to data theft, session hijacking, and man-in-the-middle (MitM) attacks

- **Having only one MySQL server capable of accepting writes is an issue.** <br />
    Some transactions committed on the master may not be available on the slave if the master fails.
- **Having servers with all the same components (database, web server and application server) might be a problem.** <br />
    Your web site and database will share the same server resources (disk usage, memory, CPU). As a result, your database and web site will run slower than they would if they did not share resources with each other.
