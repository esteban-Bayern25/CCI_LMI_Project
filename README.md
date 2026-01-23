# CCI_LMI_Project
Notes and Preparation with the CCI Project Base Learning Program with partnership with LMI


## ZigBee Protocol

Information regarding ZigBee is here: [ZigBee](ZigBee/README_ZigBee.md)


## Mist Protocol

Information regarding mist (RSAE mist) is here: [Mist](Mist/README_Mist.md)

## Comparison Notes

Availability: ZigBee suffers from Coordinator Loss that can collapse the whole network. Mist is more resilient to system-wide collapse because it lacks a "dedicated network manager," but it is more vulnerable to localized parent-branch failures.

Energy Exhaustion: In ZigBee, routers must be "always on," making them easy targets for battery-draining attacks. Mist nodes (both clients and servers) use synchronization to sleep, meaning an attacker must first "break" the synchronization to successfully perform a battery-exhaustion attack.

**Security Similarities: The Shared IoT Surface**
Despite their different designs, both protocols share risks inherent to low-power wireless networking:

- Jamming Susceptibility: Both operate in the 2.4 GHz band. ZigBee uses CSMA/CA while Mist uses TSCH (Time-Slotted Channel Hopping). While Mist's channel hopping makes it more resilient, both can still be disrupted by wide-band noise or targeted interference at the physical layer.

- Dependency on Key Nodes: Both protocols rely on specific nodes for network stability. In ZigBee, it is the Coordinator (the "keeper" of address and key tables); in Mist, it is the Server/Parent node that negotiates schedules.

- Symmetric Key Risks: Both protocols utilize AES-128 for encryption and integrity. This means both are vulnerable if an attacker can extract the symmetric keys from a compromised device's memory or intercept them during a weak commissioning phase.

# Proposed Course

1. Resilience to Coordinator/ Manager Failure
2. Battery Exhaustion via "Listen Mode" Manipulation
