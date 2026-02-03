# Proposed Course

1. ACK Replay via Gateway Proxy Manipulation 
2. Battery Exhaustion via Replay Flooding (Alternative Test)

#### Objective
To quantify the security posture and operational resilience of NB-IoT (vs. Mist) by simulating replay-style attack scenarios.

This plan evaluates “Operational Security” to test how easily NB-IoT's system can be disrupted or compromised without breaking encryption?

### Test 1: ACK Replay Attack (Integrity + Availability + Resource Exhaustion)
- **Thesis:** Confirmation logic failure in NB-IoT can be compromised by gateway-level ACK replay. This test quantifies whether integrity and delivery guarantees remain valid during relay spoofing.

- **The Scenario:** Target a single NB-IoT end device (“UE”) that sends confirmed uplink messages to a server through a gateway/relay path you control.
Simulate a vulnerable point of access safely by inserting a Gateway Proxy in the IP path that can do the following:
  - drop uplinks
  - delay downlinks
  - record ACK messages
  - relay previously recorded ACKs

A control comparison test on MIST will be run to determine its security posture and confirmation logic strength.

- **The Attack:**
1. Baseline: Configure the UE to send a "confirmed uplink" message every x seconds. Log timestamps, received messages and ACKs, and pcap data.
2. Recon: Capture traffic on the first 10 ACKs and extract dnctr from payload using Wireshark. Identify the ACK message pattern and sequential dnctr values.
3. ACK Pause: Configure the Gateway Proxy to drop or blackhole server ACKs temporarily: Block downlink packets from Server → UE for a fixed window.
4. Attack: Allow UE to replay old ACK by sending previously captured ACK back to the UE. Observe whether UE confirms the ACK even though the server never received it.
5. Result: UE accepts confirmation --> Server missing message --> Silent integrity failutre + state divergence

Goal: Prove you can create false confirmation or silent message loss via replayed ACKs in NB-IoT, while Mist remains resistant because devices only accept authenticated, session-validated communications and cannot be directly addressed or tricked by replayed messages.


### Test 2: Replay Flood for Battery Exhaustion (Availability + Denial of Service + Cost-of-Failure)
- **Thesis:** Replay attacks can drain NB-IoT device battery by repeatedly retransmitting previously captured messages to the original receiver, whereas Mist’s identity-verified, non-IP communication model prevents unsolicited interactions and inherently blocks replayed messages.

- **The Scenario:** Capture a legitimate downlink or “poll” message and then replay it repeatedly at a controlled rate from the Gateway Proxy to the UE.

- **The Attack:**
1. Capture a legitimate downlink packet that triggers device processing.
2. Replay it at intervals (e.g., every 100–500 ms, tune to avoid immediate rate limiting).
3. Measure: device wake time, retry behavior, power draw increase (USB power meter), loss of normal reporting cadence
 
The Goal: Demonstrate the operational cost of replay exposure: increased battery drain → increased maintenance → lower resilience.




## Equipment List

**Devices**
- NB-IoT Development Kit
  - [Nordic nRF9160 DK (recommended)](https://www.newark.com/nordic-semiconductor/nrf9160-dk/dev-kit-32bit-arm-cortex-m33/dp/84AC2295?&CMP=KNC-GUSA-GEN-SKU-OPTMYZR-ONBOARD-COMP&gad_source=1&gad_campaignid=22986376236&gbraid=0AAAAAD5U_g0Uyb2Ir5j3ksK9uRmFpIiUE&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xq1ldrmNJ_5IrvFfNfEnjhyNFgNrL3Pv8d1EqbJSsioiW_EDF1EUzkaAri9EALw_wcB)
- SIM with NB-IoT/LTE-M support
- Raspberry Pi 5 or any Linux laptop
- LTE hotspot / USB cellular modem (optional)
- USB inline power meter


**Company Provided**
- 1 Mist Gateway 
- 1 Mist Extender
- 2-3 Mist Tags


**Software/Logger Tools**
- Wireshark
- tcpdump
- tcprelay
- Python
- Linux
- Python CSV logger
- Serial logs from dev kit


### References
[Vulnerability Assessment Reference](https://cora.ucc.ie/bitstreams/74b32367-7e66-4c4b-9669-f16362f2234d/download)

[NB-IoT Energy Consumption Characteristics](https://arxiv.org/pdf/2005.13648)

[Energy Consumption Analysis of LPWAN Technologies](https://pmc.ncbi.nlm.nih.gov/articles/PMC7506725/?utm_source=chatgpt.com)

[NB-IoT vs Alternatives in Mobility and Delay](https://www.zipitwireless.com/blog/nb-iot-explained-is-it-right-for-your-iot-solution?

[ACK Replay attack](https://www.researchgate.net/publication/399082774_An_Efficient_Risk_Impact_and_Vulnerability_Assessment_Framework_for_NB-IoT_Networks_Risk_Impact_and_Vulnerability_Assessment_Framework_for_NB-IoT_Networks)

[Battery depletion/resource exhaustion attacks in NB-IoT](https://cora.ucc.ie/server/api/core/bitstreams/b6ee4e8d-7fbd-4b13-946e-b0829a4fd5a8/content)

[Replay protection via counters/nonces](https://rp.os3.nl/2019-2020/p68/report.pdf?)


utm_source=chatgpt.com)
