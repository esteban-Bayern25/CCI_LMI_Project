# Proposed Course

1. Resilience to Coordinator/ Manager Failure
2. Battery Exhaustion via "Listen Mode" Manipulation

#### Objective
To quantify the operational resilience and security-depth of Mist compared to Zigbee Pro by simulating high-impact failure and attack scenarios.

### Test 1 Architectural Resilience (Availability)
**Thesis:** Zigbee is "brittle" due to its Centralized State Model (Trust Center dependency). Mist is "resilient" due to its Decentralized Synchronization (Local State management). [^1]

 - Experiment: Establish a stable multi-node mesh for both protocols. Simulate a "Critical Failure" by hard-powering off the Central Coordinator (Zigbee) and the Network Manager (Mist).
 - Key Metrics:
    - Blast Radius: % of the network that remains operational for local peer-to-peer tasks.
    - Recovery Time Objective (RTO): Time required to restore full network functionality after replacing the central node.

### Test 2 Defensive Longevity (Battery Exhaustion)
**Thesis:** Zigbee’s CSMA-CA (Always-Listening) routers are vulnerable to "Energy Depletion" attacks. Mist’s Request-Response (Scheduled-Sleep) model provides a "Temporal Firewall" against RF noise.

- Experiment: Introduce "Rogue Node" noise—high-volume, non-network traffic meant to trigger the radio's "Listen" state.
- Key Metrics:
    - Radio Duty Cycle: Ratio of active RX/TX time vs. deep sleep.
    - Estimated Battery Lifespan Delta: Calculated reduction in years of life when under a 50% RF-interference load.

## Equipement list

- ZigBee coordinator ()
- ZigBee routers
- ZigBee End Devices (tags/ sensors)
- nRF Sniffer for 802.15.4 [^2]
    - [nRF52840 Dongle](https://www.digikey.com/en/products/detail/nordic-semiconductor-asa/NRF52840-DONGLE/9491124?utm_source=oemsecrets&utm_medium=aggregator&utm_campaign=buynow) 
- IoT smart Plug


**software/ logger tools**
- python
- wireshark
- scapy
- Zephyr RTOS
- [API](https://docs.zephyrproject.org/apidoc/latest/structieee802154__radio__api.html) 
- nRF Connect for Desktop
- zperf (Zephyr Utility)
- Pyserial

[^1][Security Assesesment Reference](https://securelist.com/zigbee-protocol-security-assessment/118373/)
[^2][Setup Dongle Tutorial](https://youtu.be/ptY3lrboV-c?si=IevqJVBHtRSsnEBb)
