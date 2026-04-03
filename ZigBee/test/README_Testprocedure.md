# ZigBee Security Evaluation

### Overview
This project evaluates the security and resilience of ZigBee networks by simulating real-world attack scenarios against a coordinator-based architecture. The goal is to analyze how centralized trust models in ZigBee compare to more decentralized architectures (e.g., Mist) under adversarial conditions.[^1-5]

1. Application-Level Attack
2. Denial of Service Attacks

### Objective
The primary objective is to quantify the operational resilience and security depth of ZigBee networks by simulating high-impact failure and attack scenarios. [^4]

Specifically, this project investigates:
- The impact of centralized trust (ZigBee Trust Center) on network stability
- The feasibility of network takeover and device eviction attacks
- The risk of key compromise and command injection

## Test 1: Trust Center Compromise (Confidentiality + Integrity)
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

2. From there you will have successful decryption, packet types and readable application commands will be visible, such as Link Status or on/off cluster commands. You can carry out some actions on the device (e.g., if the device is a light, turn it on/off, change the brightness, etc.) and you should see decrypted Zigbee messages in the capture window.

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

3. Running the python file allows you to continuously inject packets into the network and observe, best run the ```.py``` in the WHAD virtual environment

**Note:** Must have WHAD configured and setup and might need to end up adjusting some parameters such as the 'Visible' Hex

```bash
python test_both_capture_and_inject.py
```

With the captured information via the sniffer able to find those packets that were injected 

![packet injection via running python script towards router 3](/assets/images/zigbee/progress_zigbee/confirmation_of_packet_injection_whad.png)

Another example for packet injection on the commerical grade of the [Third Reality](https://thirdreality.com/) door contact sensor and with the nRF52 dongle sniffer able to see the packets being sent

```bash
python packet_injection_on_end_device_door_contact_sensor.py
```

**Note:** The image below shows the python file run under a different name in testing, but the function is the same. The name changed to give a better description

![Python file running in command line terminal](/assets/images/zigbee/cmd_line_run_end_device_packet_injection.png)

![Wireshark capture of the end contact device sensor](/assets/images/zigbee/progress_zigbee/wireshark_capture_end_device_door_contact_spoof.png)

Above [pcap shows](/assets/images/zigbee/zigbee_pcap_captures/end_device_packet_injection_door_contact_test2_see_ack.pcap)the packets being sent from packets 101-109, in which demonstrates  a probabilistic resilience. While the MAC layer is "brittle" (it accepted the spoofed command), the higher-layer firmware is "resilient" because it detects the loss of a parent and automatically recovers.

The Goal: Prove that compromised integrity allows an attacker to "Spoof" sensor data or control commands across the entire network


## Test 2: Architectural Resilience (Availability + Denial of Service)
**Thesis:** Zigbee is "brittle" due to its Centralized State Model; Mist is "resilient" due to Decentralized Synchronization. A single spoofed management frame from a rogue coordinator can force nodes to abandon the legitimate network.

### Scenario: Network Realignment Attack

**Part 1 Recon:** Identify the 16-bit Short Address and PAN ID of the legitimate network. 

#### Setup:
Using the nRF52840 dongle and Wireshark or with the WHAD device either works:

1. Capture traffic (Similar to Test 1 examples)

[Observe Test 1 Part 1 Recon, very similar steps](#Setup)

2. For setting up the Xbee Module to act as a router and connect to the Zigbee2MQTT network please refer to [Configuration of the Digi Xbee Router Module for Test 2](/ZigBee/Setup_Procedure.md)

3. The Spoof: Use an nRF52840 Dongle (Sniffer/Attacker) with WHAD configured to send a spoofed Coordinator Realignment (0x07) command. 

**Note:** Important parameters to have are
| Parameter | Description |
| :--- | :--- |
| Target NWK Address | The 16-bit address of the router being targeted. |
| Target IEEE | The unique 64-bit MAC address of the target device. |
| Legitimate PAN ID | The ID of the network the device currently belongs to. |
| Coordinator IEEE | The MAC address of the legitimate Trust Center. |
| Rogue PAN ID | The destination ID (e.g., 0xDEAD) to which the node will be "evicted." |

Then you get edit/ make adjustments to the [python script](/ZigBee/test/python_scripts/packet_injection_on_xbee_router.py)

Running the script:

```bash
python packet_injection_on_xbee_router.py
```

![Running the python file](/assets/images/zigbee/progress_zigbee/cmd_line_running_script_inject_xbee_router.png)

4. The Payload: The frame contains a new, rogue PAN ID

![Xbee Router packet injection](/assets/images/zigbee/progress_zigbee/wireshark_capture_xbee_router_leaving_network.png)

Immediately following the injection, the sniffer captured an IEEE 802.15.4 Beacon Request. A router only sends a Beacon Request when it is "orphaned" or searching for a network. This proves the XBee accepted the rogue command, moved to the Rogue PAN ID (0xdead), and—finding no legitimate hub there—began searching for a new parent.

To observe the pcap capture look [here](/assets/images/zigbee/zigbee_pcap_captures/test_2_packet_injection_on_xbee_router.pcap)

**Goal:** Prove that Zigbee’s centralized logic allows an attacker to "evict" the legitimate owner and take control of the topology, whereas Mist’s Local Survival Mode prevents such shifts because "Trust" is not tied to a single, spoofable PAN ID. The Router follows the spoofed command to the new PAN ID, orphaning its child devices and causing a localized Denial of Service (DoS)


## Test 3: Resource Exhaustion (Availability)

**Thesis:** Zigbee networks are inherently vulnerable to Protocol Flooding due to the Coordinator’s role as a 
centralized data sink. This experiment demonstrates that a single rogue router can exhaust the Coordinator's processing buffers and 
saturate the IEEE 802.15.4 bandwidth. The result is the catastrophic dropping or delaying of critical, legitimate sensor data (e.g., GPS telemetry).

### Scenario: Malicious Traffic Saturation

**Part 1 Baseline (Recon):** Establish the "Normal" state of the network. Identify the average latency and throughput of a legitimate device while the network is quiet.

![Normal State Network](/assets/images/zigbee/progress_zigbee/baseline_state_zigbee_network_test3.png)

#### Setup:

1. Run or Configure one of the Xbee routers to acts a legitimate GPS simulation (sending 58-byte packets every millisecond).

![Configure payload with GPS simulation](/assets/images/zigbee/progress_zigbee/configuration_of_router_to_coordinator.png)

![Coord receiving the payload](/assets/images/zigbee/progress_zigbee/payload_sent_to_coordinator.png)

2. Use the Xbee Studio Throughput Test tool to monitor the "Average transfer ratio"

![Recording of data of Kbps with GPS](/assets/images/zigbee/progress_zigbee/recording_kbps_with_gps_router.png)

- The black dotted line (Average) is very flat, which means your link is stable and there is very little interference in your current environment.

- pushing about 368 bytes per second ( approx. 6.3 GPS packets per second). This perfectly simulates a high-frequency GPS tracker (5Hz–10Hz).

- At 2.94 Kbps, =only using about 5% to 10% of a typical Zigbee link's actual capacity. This gives you plenty of "headroom" to observe the impact of an attack.

Another test in which both routers are transmitting GPS data to the coordinator simultaneosuly for about 60 seconds

![Throughput Test Router 1](/assets/images/zigbee/progress_zigbee/router1_throughput_test.png)

![Throughput Test Router 2](/assets/images/zigbee/progress_zigbee/router2_throughput_test.png)

**Part 2 The Attack (Exploit):** Introduce a Rogue Router (Attacker) designed to "Flood" the Coordinator with high-frequency, maximum-payload traffic.

#### Setup:
Using a second XBee module connected and integrated into the Xbee Zigbee Network:

1. Configure the Rogue Router to send Unidirectional traffic to the Coordinator's 64-bit address.

In this case Router 2 is configured to send random max payloads of 255 bytes, with a transmit timeout of 200 ms, and to loop infinitely to be able to see the the impact on the legitimate router (router1)

**Part 3 Impact Analysis (Payload):** Observe the failure of legitimate network services under the pressure of the flood.

#### Setup:
1. While the Rogue Router (router 2) is flooding, attempt to view the legitimate GPS data in the Coordinator’s serial console.

![Protocol Flooding the Coordinator](/assets/images/zigbee/progress_zigbee/coord_viewpoint_from_protocol_flooding.png)

2. Monitor the Xbee Studio Throughput graph for the legitimate device.

![Decrease in the average transfer ratio](/assets/images/zigbee/progress_zigbee/router1_throughput_test_with_protocol_flooding.png)

Able to see that the Average transfer ratio decreases when a rouge router floods the network with random bytes of information 

**Goal:** Prove that ZigBee’s lack of per-node rate limiting allows a single malicious or malfunctioning device to "crowd out" critical traffic.


### References
[^1]:[Security Assesesment Reference](https://securelist.com/zigbee-protocol-security-assessment/118373/)
[^2]: [Setup Dongle Tutorial](https://youtu.be/ptY3lrboV-c?si=IevqJVBHtRSsnEBb)
[^3]:[Setup for another ZigBee Coordinator slzb06](https://smlight.tech/global/slzb06)
[^4]: [Setup for ZigBee network](https://smarthomescene.com/guides/how-to-build-a-stable-and-robust-zigbee-network/)
[^5]: [ZigBee Vulnerabilites](https://payatu.com/blog/zigbee-security-101-architecture-and-security-issues/#ZigBee_Vulnerabilities)