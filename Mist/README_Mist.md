# Mist Background

**Nothing is every 100% secure when it comes to IoT and Security**

Hierarchical, server-client model

![Network Topology of Mist Protocol](/assets/images/mist_network.png)


### 1. Synchronization methodology
local synchronization

**Vulnerabilites**
- De-syncrhonization Attacks: target specific neighbor-link timing to drift a node away from parent schedule
- Schedule Negotiation Spoofting: negotiation phase unencrypted or weak, a rouge node could intercept to predict when the target node will wake up to listen

### 2. Hierarchical 
Optimized for one-to-many or many-to-one data flows 

Parent node will slow down scheme to force children to slow search for a better parent to prevent network churn

data flows are straightfoward

**Vulnerabilites**
- Parent-Link Churn Manipulation: compromization of a parent node could "slow down" children pinning to low-quality or compromised link 
- Bottleneck Targeting: Parent nodes are higher-value targets for DoS

### 3. "Don't Talk Unless Spoken To"

Sounds like a request-response or another might be passive mode
client server relationship

**Vulnerabilites**
- Server Impersonation: attacker spoof the servers request, have command to silent clients


## Mist Protocol Vulnerability Mapping (STRIDE)

| STRIDE Category  | Mist Vulnerability | Technical Impact |
| ------------- | ------------- | ------------- |
| Spoofing | Server Node Impersonation  | Rogue nodes spoofing the "parent" could trigger responses from otherwise silent "don't talk unless spoken to" clients. |
| Tampering  | Schedule Negotiation Interference  | Interfering with the negotiation of the 128 hardcoded schedules to force a collision or drop in communication. |
| Information Disclosure  | Schedule Prediction  | Identifying which of the 128 hardcoded schedules is active allows an attacker to time their sniffing or injection attempts precisely. |
| Denial of Service (DoS)  | Local Sync Disruption | Desynchronizing neighbor nodes to break the local timing required for TSCH communication. |
| Elevation of Privilege | "Slow-Down" Abuse | Forcing children to remain attached to a compromised parent node by maliciously increasing the "slow-down" rate. |


How we plan to apprach the RSAE Mist refer to [Mist Approach](README_mistApproach.md)

### References
