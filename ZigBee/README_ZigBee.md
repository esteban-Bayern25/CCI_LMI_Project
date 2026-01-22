# ZigBee Background

Zigbee is a low power alternative to WiFi for IoT devices. (low power mesh netowrking)

IEEE
802.15.4-2003

Low power protocol that’s handy for battery powered devices. Zigbee also handily works as a mesh network where by any mains powered zigbee devices are usually “routers”. So devices out of reach of the HA server can still talk back via other devices that are

Zigbee is a low power, low-latency, low-bandwidth mesh networking protocol. With WiFi, every device has to be within range of the router. With mesh networking each device only has to be in range of the nearest device.

Uses CSMA - CA


## Security 

Authentication and Encryption, Freshness (frame counters), and Message Integrity using symmetric keys based upon AES-128


## Vulnerabilities

1. Key Management and Commissioning Vulnerabilities
    - Clear-Text Key Interception: In High Security mode, the Master Key can be provided "in the clear" from the Trust Center. An attacker capturing traffic during the joining process could intercept this key to compromise the entire device's communication.
    - Trust Center Exploitation: Since the Trust Center node is responsible for creating and distributing Network Keys, it represents a single point of failure. If an attacker can compromise or spoof the Trust Center, they can control the distribution of active and secondary Network Keys.
2. Operataional and Physical Layer Vulnerabilites
    - Network Collapse (Coordinator Loss): The security of the network relies on the ZigBee Coordinator to maintain tables for address assignments and key management. If a coordinator is lost and its replacement does not have access to these tables, the entire network must be taken down and restarted, creating a significant availability risk.
    - Hop-Limit Limitations: Since the maximum depth is 15 and the maximum number of hops is less than 30, an attacker could potentially flood the mesh with packets that exhaust the hop limit, preventing legitimate traffic from reaching the destination.


## STRIDE Threat Model: ZigBee Pro Protocol

| STRIDE Category  | ZigBee Vulnerability | Technical Impact |
| ------------- | ------------- | ------------- |
| Spoofing | Trust Center Spoofing  | |
| Tampering  | Route Table Manipulation  | |
| Information Disclosure  | Clear-Text Key Interception  | |
| Denial of Service (DoS)  | Network Collapse (Coordinator Loss) & Hop Limit Exhaustion| |
| Elevation of Privilege | Trust Center Exploitation | |

## Bad Scenario (Loss of Key devices)

Upon the loss of ZigBee coordinator another coordinator will nominate itself the Zigee coordinator. If the “lost” ZigBee Coordinator was the “keeper” of
the tables used in the ZigBee network such as extended to short address, key
assignments, routes, etc. then the network would have to be taken down and restarted.

1. What does it mean my loss?
-> Loss of the physical or functionla failure of a hardware device (ZigBee Coordinator)
Reasonds for these loss: DoS, Hardware Failure, Connectivity Loss (jamming)



### References

[ [1] NIH ZigBee 3.0](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349651/#sec3-sensors-25-04606)