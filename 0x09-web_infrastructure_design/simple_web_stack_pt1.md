# Web infrastructure design

## 0. Simple Web Stack

### Specifics About This Infrastructure

- **What a server is.** <br />
    A server is a piece of computer hardware or software that provides functionality for other programs or devices, called "clients".

- **The role of the domain name.** <br />
    Helps users find their way around the Internet.
    Domain name - a string of text that maps to a numeric IP address, used to access a website from client software.
- **The type of DNS record ```www``` is in ```www.foobar.com```.**
    ```www.foobar.com``` uses an A record. This can be checked by running ```dig www.foobar.com```.
    Note: the results might be different but for the infrastructure in this design, an A record is used.
    Address Mapping record (A Record) - also known as a DNS host record, stores a hostname and its corresponding IPv4 address.
- **The role of the web server.** <br />
    Serves web pages to clients upon their request, it does this over the protocol HTTP.
- **The role of the application server.** <br />
    Provides its clients with access to what is commonly called business logic, which generates dynamic content;that is, it’s code that transforms data to provide the specialized functionality offered by a business, service, or application.
- **The role of the database.** <br />
    To maintain a collection of organized information that can easily be accessed, updated and managed.
- **What the server uses to communicate with the client (computer of the user requesting the website).** <br />
    Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.
