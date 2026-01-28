# Proposed Course

1. Resilience to Coordinator/ Manager Failure
2. Battery Exhaustion via "Listen Mode" Manipulation

#### Objective
To quantify the operational resilience and security-depth of Mist compared to Zigbee Pro by simulating high-impact failure and attack scenarios.[^1]

This refined plan focuses on the Centralized vs. Decentralized core of your thesis. Instead of battery drain, we are now testing the "Total Network Surrender" that occurs when a Zigbee Trust Center is compromised or lost, versus the Mist architecture's resilience.[^4]

### Test 1: Architectural Resilience (Availability + Denial of Service)
- **Thesis:** Zigbee is "brittle" due to its Centralized State Model; Mist is "resilient" due to Decentralized Synchronization.

- **The Scenario:** You will hard-kill the Zigbee Coordinator and the Mist Gateway simultaneously.

The "Spoofing" Twist: After killing the real Zigbee Coordinator, you will use your nRF52840 Dongle to broadcast a "Fake" Beacon with the same PAN ID but an incremented Update ID. This will trick the routers into trying to rejoin a non-existent/malicious brain, preventing them from self-healing.

### Test 2: Trust Center Compromise (Confidentiality + Integrity)
- **Thesis:** Zigbee’s security relies on a single "Master Key" (Link Key) that is often a well-known default; Mist uses identity-based unique keys.

- **The Attack:** You will use the nRF52840 Sniffer to capture the "Transport Key" during a device join. You will exploit the "ZigBeeAlliance09" default Link Key to decrypt that Transport Key, giving you the Network Key.

The Goal: Prove that once you have the Network Key, you can "Spoof" any command (e.g., turning a sensor off) because you now have the "Keys to the Kingdom."

### Test Optional Defensive Longevity (Battery Exhaustion) - MAYBE??
**Thesis:** Zigbee’s CSMA-CA (Always-Listening) routers are vulnerable to "Energy Depletion" attacks. Mist’s Request-Response (Scheduled-Sleep) model provides a "Temporal Firewall" against RF noise.

- Experiment: Introduce "Rogue Node" noise—high-volume, non-network traffic meant to trigger the radio's "Listen" state.
- Key Metrics:
    - Radio Duty Cycle: Ratio of active RX/TX time vs. deep sleep.
    - Estimated Battery Lifespan Delta: Calculated reduction in years of life when under a 50% RF-interference load.


## Equipement list

- ZigBee coordinator ([SONOFF ZigBee 3.0 USB DonglePlus](https://sonoff.tech/en-us/products/sonoff-zigbee-3-0-usb-dongle-plus-zbdongle-p?srsltid=AfmBOoq05n5bl2pB1xAz3aOx3RIwYfIqM_I8NbOEmXzF3O2efw0Ij0s7))[^3]
    - [RaspberryPi 5](https://www.digikey.com/en/products/detail/raspberry-pi/SC1432/21658257)
    - [Another option for Coordinator](https://www.amazon.com/SMLIGHT-SLZB-07-Coordinator-Zigbee2MQTT-Assistant/dp/B0D737SJ5G?dib=eyJ2IjoiMSJ9.ppEgVhHKzbBp2a7RAhwpKX6zOrDh5UNGyvyNEn3H8PcEgEU3sqjH5ArnFaR6rVdX.pkkkl2FxHrIR1luYNXO4iFdPaTO-r5mrSv_TGE252qA&dib_tag=se&keywords=SLZB-07&qid=1741067435&s=electronics&sr=1-1&linkCode=sl1&tag=smarthomescen-20&linkId=2d3a69d903fbd973ba5ec0f5371f7774&language=en_US&ref_=as_li_ss_tl&th=1)
- ZigBee routers x2-4 (IoT smart Plug/ [Sonoff S31 Lite zb](https://sonoff.tech/en-us/products/sonoff-s31-lite-zb-smart-plug-us-type-zigbee-version?srsltid=AfmBOoouOWD-7qDYsYzVtx6ROJP727KxYbj710cNZLtBlKKkP0D6Rc7Z) or [ZBBridge-P](https://sonoff.tech/en-us/products/sonoff-zigbee-bridge-pro?pr_prod_strat=pinned&pr_rec_id=67b491ac0&pr_rec_pid=8812959826161&pr_ref_pid=8812958646513&pr_seq=uniform))
- ZigBee End Devices (tags/ sensors) -> are Mist Tags
- nRF Sniffer for 802.15.4 [^2]
    - [nRF52840 Dongle](https://www.digikey.com/en/products/detail/nordic-semiconductor-asa/NRF52840-DONGLE/9491124?utm_source=oemsecrets&utm_medium=aggregator&utm_campaign=buynow) 

- 

**Company Provided**
- 1 Mist Gateway (Maybe not we provide our own gateway)
- 1 Mist Extender
- 2-3x Mist Tags


**software/ logger tools**
- python
- wireshark
- scapy
- Zephyr RTOS
- [API](https://docs.zephyrproject.org/apidoc/latest/structieee802154__radio__api.html) 
- nRF Connect for Desktop
- zperf (Zephyr Utility)
- Pyserial
- Zigbee2MQTT or Home Assistant (ZHA)


### References
[^1]:[Security Assesesment Reference](https://securelist.com/zigbee-protocol-security-assessment/118373/)
[^2]: [Setup Dongle Tutorial](https://youtu.be/ptY3lrboV-c?si=IevqJVBHtRSsnEBb)
[^3]:[Setup for another ZigBee Coordinator slzb06](https://smlight.tech/global/slzb06)
[^4]: [Setup for ZigBee network](https://smarthomescene.com/guides/how-to-build-a-stable-and-robust-zigbee-network/)
[^5]: [ZigBee 4.0 news](https://www.silabs.com/blog/zigbee-4-0-improves-security-commissioning-and-efficiency)

[ZigBee 4.0](https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/)
