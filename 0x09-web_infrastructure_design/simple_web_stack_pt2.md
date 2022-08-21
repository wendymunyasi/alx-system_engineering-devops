# Web infrastructure design

## 0. Simple Web Stack

### Issues with this infrastructure

- **SPOF (Single Point Of Failure).** <br />
    Failure of the server causes whole network to collapse

- **Downtime when maintenance needed.** <br />
    When the system is not being productive due to required maintenance work (like deploying new code web server needs to be restarted).
- **Cannot scale if too much incoming traffic.** <br />
    It is a bit unwieldy when it comes to scaling your site for higher loads.
