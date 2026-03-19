# ZigBee Security Evaluation

### Overview
This project evaluates the security and resilience of ZigBee networks by simulating real-world attack scenarios against a coordinator-based architecture. The goal is to analyze how centralized trust models in ZigBee compare to more decentralized architectures (e.g., Mist) under adversarial conditions.

1. Application-Level Attack
2. Denial of Service Attacks

### Objective
The primary objective is to quantify the operational resilience and security depth of ZigBee networks by simulating high-impact failure and attack scenarios. [^4]

Specifically, this project investigates:
- The impact of centralized trust (ZigBee Trust Center) on network stability
- The feasibility of network takeover and device eviction attacks
- The risk of key compromise and command injection

## Test 1: Architectural Resilience (Availability + Denial of Service)
**Thesis:** Zigbee is "brittle" due to its Centralized State Model; Mist is "resilient" due to Decentralized Synchronization. A single spoofed management frame from a rogue coordinator can force nodes to abandon the legitimate network.

**The Scenario:** Network Realignment Attack

**Target:** A specific Router with several child End Devices

**The Attack:** 
    1. Recon: Identify the 16-bit Short Address and PAN ID of the legitimate network. 
    2. The Spoof: Use an nRF52840 Dongle (Sniffer/Attacker) to send a spoofed Coordinator Realignment (0x07) command. 
    3. The Payload: The frame contains a new, rogue PAN ID

**Goal:** Prove that Zigbee’s centralized logic allows an attacker to "evict" the legitimate owner and take control of the topology, whereas Mist’s Local Survival Mode prevents such shifts because "Trust" is not tied to a single, spoofable PAN ID. The Router follows the spoofed command to the new PAN ID, orphaning its child devices and causing a localized Denial of Service (DoS)

## Test 2: Trust Center Compromise (Confidentiality + Integrity)
**Thesis:** ZigBee security depends on shared keys that may be exposed during device joining, whereas stronger systems use per-device identity-based keys.[^5]

### **Scenario:** Key Extraction & Command Injection

**Part 1 Packet Capture (Recon):** Use the nRF Sniffer to capture the Transport Key during a device join or reconnection event.

#### Setup:
Using the nRF52840 dongle and Wireshark or with the WHAD device either works:
1. Capture traffic during a device join event

![Screenshot of the Wireshark screen with sniffer](/assets/images/zigbee/progress_zigbee/wireshark_screenshot_nrf52_dongle.png)

![Nordic Sniffing device in action](/assets/images/zigbee/progress_zigbee/sniffer_device_inAction.jpg)

Example using the WHAD device to sniff the network

Run the command:
```bash
wsniff -i uart0 -w dot15d4 -c 11
```
![WHAD_device_capture_inforamtion](/assets/images/zigbee/progress_zigbee/WHAD_device_capture_before.png)

2. Observe encrypted packets

![Wireshark capture of the Zigbee Network](/assets/images/zigbee/progress_zigbee/wireshark_capture_deviceJoin.png)

3. Filter in Wireshark to find the Transport Key ```zbee.sec.decryption_key```

![Wireshark capture of transport key](/assets/images/zigbee/progress_zigbee/first_capture_of_transport_keys_with_nrf52.png)

Example using the WHAD configuration on the nRF52840 dongle device:

![Capture of Commerical grade router 3](/assets/images/zigbee/progress_zigbee/WHAD_device_action_capture3Router.png)

**Part 2 Exploit:** Attempt to decrypt the Transport Key using the default "ZigBeeAlliance09" Link Key or with the WHAD device.

1. Once the keys are obtained add them in the Wireshark Settings via 

``` preferences > Protocols > Zigbee > Pre-configured Keys [click Edit] > add the keys captured```

![Wireshark Setting shows of adding the key](/assets/images/zigbee/progress_zigbee/wireshark_adding_keys.png)

2. From there you will have successful decryption, packet types and readable application commands will be visible, such as Link Status or on/off cluster commands

![Information is Decrypted](/assets/images/zigbee/progress_zigbee/wireshark_keysObtained_InfoUnlocked.png)

![Information on end device Door sensor](/assets/images/zigbee/progress_zigbee/commerical_endDevice_info.png)


Information using WHAD device able to see the packets information (no longer encrypted):

![Information gathering](/assets/images/zigbee/progress_zigbee/WHAD_device_after_decryption.png)

**Part 3 Payload:** Once the Network Key is obtained, use a laptop and Scapy/Python to inject unauthorized application-level commands.

#### Setup:
Using the nRF52840 dongle configured with the wireless hacking tool [WHAD](https://whad.readthedocs.io/en/latest/intro.html)

1. Winject allows you to To inject packets into the 802.15.4 network run this command:
```bash
winject -i uart0 dot15d4 -c 11 [HEX STREAM VALUES]
```
![command to run the packet injection](/assets/images/zigbee/progress_zigbee/packet_injection_cmd_terminal.png)

2. Run the wireshark sniffer and you will see the packet injected into the network towards a specific zigbee device by looking for key properties. Example is its seqence number

Command for looking in wireshark the sequence number: ```wpan.seq_no == ```

![Packet Injection into Commerical Grade component (router 3)](/assets/images/zigbee/progress_zigbee/packet_injection_confirmed.png)

3. Running the python file allows you to continuously inject packets into the network

**Note:** Must have WHAD configured and setup and might need to end up adjusting some parameters such as the 'Visible' Hex

```bash
python test_both_capture_and_inject.py
```

![packet injection via running python script towards router 3](/assets/images/zigbee/progress_zigbee/confirmation_of_packet_injection_whad.png)

The Goal: Prove that compromised integrity allows an attacker to "Spoof" sensor data or control commands across the entire network






## Notes
Qualitative methods involve observing and interpreting the impact of attacks through direct observation and network scans. Quantitative methods measure the effect of attacks numerically, such as the number of packets received or dropped during DoS attacks.

- [PAN ID](https://docs.digi.com//resources/documentation/digidocs/90002002/concepts/c_zb_pan_id.htm?tocpath=Zigbee%20networks%7CZigbee%20networking%20concepts%7CPAN%20ID%7C_____0)
- [Joining Zigbee Networks](https://docs.digi.com/resources/documentation/digidocs/90001399-13/references/r-create-join-zigbee-network.htm)

- [Network Realignment Attack](https://pmc.ncbi.nlm.nih.gov/articles/PMC12349651/#B9-sensors-25-04606)
- Spoofing or compromising TC 
[Home Assistant](https://www.home-assistant.io/integrations/sensor/)


### References
[^1]:[Security Assesesment Reference](https://securelist.com/zigbee-protocol-security-assessment/118373/)
[^2]: [Setup Dongle Tutorial](https://youtu.be/ptY3lrboV-c?si=IevqJVBHtRSsnEBb)
[^3]:[Setup for another ZigBee Coordinator slzb06](https://smlight.tech/global/slzb06)
[^4]: [Setup for ZigBee network](https://smarthomescene.com/guides/how-to-build-a-stable-and-robust-zigbee-network/)
[^5]: [ZigBee Vulnerabilites](https://payatu.com/blog/zigbee-security-101-architecture-and-security-issues/#ZigBee_Vulnerabilities)

[ZigBee 4.0 news](https://www.silabs.com/blog/zigbee-4-0-improves-security-commissioning-and-efficiency)

[ZigBee 4.0](https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/)

[DigiMesh vs Zigbee Mesh](https://www.digi.com/blog/post/what-are-the-differences-between-digimesh-and-zigb)