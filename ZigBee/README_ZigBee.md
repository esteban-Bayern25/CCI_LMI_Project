# Zigbee Background
Zigbee is a low-power alternative to Wi-Fi for IoT devices, focusing on low-power mesh networking. [^1]

IEEE 802.15.4-2003

A low-power, low-bandwidth mesh protocol designed for ad-hoc, self-forming networks. It utilizes a hop-based architecture where mains-powered devices act as routers, extending range beyond a central hub by passing data through neighboring nodes. This makes it ideal for low-latency communication in battery-constrained environments like building and home automation. [^1]

![Network Topology of ZigBee Protocol](/assets/images/zigBee_network.png)

Access Method: Uses CSMA-CA (Carrier Sense Multiple Access with Collision Avoidance).

## Security
Zigbee provides authentication, encryption, freshness (using frame counters), and message integrity using symmetric keys based on AES-128. [^2]


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
| Spoofing | Trust Center Spoofing  |  An attacker can impersonate the Trust Center node to distribute malicious active or secondary Network Keys to joining devices. |
| Tampering  | Route Table Manipulation  | Attackers can inject malicious route request/reply frames |
| Information Disclosure  | Clear-Text Key Interception  | Loss of data confidentiality |
| Denial of Service (DoS)  | Network Collapse (Coordinator Loss) & Hop Limit Exhaustion| Network unavailability, ZigBee Coordinator is lost and the replacement lacks the required address and key tables, the entire network must be restarted, leading to a total loss of availability. Flood the mesh network with packets |
| Elevation of Privilege | Trust Center Exploitation | Unauthorized administrative access, where attacker gains administrative control over key distribution and device associations across the entire network. |

## MITRE ATT&CK for ICS/IoT Mapping: ZigBee Pro

| Vulnerability | MITRE Tactic | MITRE Technique ID & Name |
| --- | --- | --- |
| Clear-Text Key Interception | Credential Access | T0831: Network Sniffing |
| Trust Center Exploitation| Impact | T0827: Loss of Control |
| Network Collapse (Coordinator Loss) | Impact | T0840: Inhibit Response Function |
| Hop - Limit Limitations | Impact | T0814: Denial of Service |

## Failure Scenario: Loss of Key Devices
Upon the loss of a Zigbee Coordinator, another device may nominate itself as the new coordinator. However, if the original coordinator was the sole "keeper" of critical network tables (address mappings, key assignments, routes, etc.), the network must be taken down and rebuilt from scratch.

**Defining "Loss"**
"Loss" refers to the physical or functional failure of the hardware device (Zigbee Coordinator).

Reasons for loss: DoS attacks, hardware failure, or connectivity loss (e.g., signal jamming).

### Potential Tools
1. Software [KillerBee](https://github.com/riverloopsec/killerbee)
2. Hardware: ZigBee stick/ usb?

### Questions
1. Should we propose specific remedies for these attacks, or is the primary focus on qualitative analysis?
2. 

### References

[^1]: [ZigBee Intro](https://www.geeksforgeeks.org/computer-networks/introduction-of-zigbee/)
[^2]: [NIH ZigBee3.0](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349651/#sec3-sensors-25-04606)
[^3]: [ZigBee Pro vs ZigBee 3.0](https://www.cdebyte.com/news/542)
[^4]: [korewireless](https://www.korewireless.com/blog/iot-protocols/)