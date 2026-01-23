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


The Thesis: ZigBee Pro is fragile because it relies on a central "keeper" of tables; Mist is more reliable because its decentralized schedules prevent a total network collapse.

The Experiment: Establish a stable network for both protocols. 2. Simulate a "Loss of Coordinator/Manager" by powering off the central node. 3. Data to Collect: Measure "Time to Recovery" and "Network Availability %."

Why this proves Mist is better: In ZigBee, if the Coordinator with the tables is "lost," the network must be taken down and restarted from scratch. In Mist, because there is no dedicated network manager and nodes use local synchronization, you can demonstrate that a single node failure doesn't result in a total system blackout.

Experiment: Battery Exhaustion via "Listen Mode" Manipulation
The Thesis: ZigBee’s "always-on" routers are a liability for logistics/tracking; Mist’s "don't talk unless spoken to" model protects device longevity.

The Experiment:

Use your protocol analysis harness to measure the "duty cycle" (time spent in active receive/transmit vs. sleep).

Introduce "rogue node" noise—traffic that isn't part of the network but forces nodes to listen or process headers.

Data to Collect: Calculate "Projected Battery Life" based on energy consumption in the "Listen Mode" vs. Mist's "Sleep" states.

Why this proves Mist is better: ZigBee routers must stay active to forward indeterminate messages. Mist clients only respond to their specific server/parent. You can show that in a high-noise environment (like a busy logistics hub), ZigBee devices will die significantly faster than Mist devices due to "unnecessary listening".