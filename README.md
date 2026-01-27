# CCI_LMI_Project
Notes and Preparation with the CCI Project Base Learning Program with partnership with LMI


## ZigBee Protocol

Information regarding ZigBee is here: [ZigBee](ZigBee/README_ZigBee.md)


## Mist Protocol

Information regarding Mist is here: [Mist](Mist/README_Mist.md)

## Comparison Notes

Availability: ZigBee suffers from Coordinator Loss that can collapse the whole network. Mist is more resilient to system-wide collapse because it lacks a "dedicated network manager," but it is more vulnerable to localized parent-branch failures.

Energy Exhaustion: In ZigBee, routers must be "always on," making them easy targets for battery-draining attacks. Mist nodes (both clients and servers) use synchronization to sleep, meaning an attacker must first "break" the synchronization to successfully perform a battery-exhaustion attack.

**Security Similarities: The Shared IoT Surface**
Despite their different designs, both protocols share risks inherent to low-power wireless networking:

- Dependency on Key Nodes: Both protocols rely on specific nodes for network stability. In ZigBee, it is the Coordinator (the "keeper" of address and key tables); in Mist, it is the Server/Parent node that negotiates schedules.

- Symmetric Key Risks: Both protocols utilize AES-128 for encryption and integrity. This means both are vulnerable if an attacker can extract the symmetric keys from a compromised device's memory or intercept them during a weak commissioning phase.

# Proposed Course

1. Resilience to Coordinator/ Manager Failure
2. Battery Exhaustion via "Listen Mode" Manipulation

#### Objective
To quantify the operational resilience and security-depth of Mist compared to Zigbee Pro by simulating high-impact failure and attack scenarios.

### Test 1 Architectural Resilience (Availability)
**Thesis:** Zigbee is "brittle" due to its Centralized State Model (Trust Center dependency). Mist is "resilient" due to its Decentralized Synchronization (Local State management).

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