# Web infrastructure design

## 1. Distributed web infrastructure

### Specifics About This Infrastructure

- **The distribution algorithm the load balancer is configured with and how it works.** <br />
    The HAProxy load balancer is configured with the Round Robin distribution algorithm. A client request is forwarded to each server in turn. The algorithm instructs the load balancer to go back to the top of the list and repeats again.

- **The setup enabled by the load-balancer.** <br />
    The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. This is because it consists of at least two nodes and not all nodes are going to be active. The passive (failover) server serves as a backup that's ready to take over as soon as the active (primary) server gets disconnected or is unable to serve. Different from an Active-Active setup which is made up of at least two nodes, both actively running the same kind of service simultaneously.

- **How a database Primary-Replica (Master-Slave) cluster works.** <br />
    A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

- **What is the difference between the Primary node and the Replica node in regard to the application.** <br />
    The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.
