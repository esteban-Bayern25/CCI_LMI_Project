# Progress Updates for LMI

## 02/23/2024
Setting up the ZigBee network with a raspberry pi 5 device, ZigBee MQTT mosquito, and a ZigBee Dongle P

![Image of the Zigbee Setup with Commerical Products](/assets/images/zigbee/progress_zigbee/zigbee_setup_commerical.png)
![Zigbee2MQTT logs](/assets/images/zigbee/progress_zigbee//Zigbee2MQTT_logs.png)
![Zigbee2MQTT logs diconnect](/assets/images/zigbee/progress_zigbee/Zigbee2MQTT_disconnect_log.png)
![Zigbee2MQTT logs end device](/assets/images/zigbee/progress_zigbee/Zigbee1MQTT_log_endDevice.png)
![Zigbee2MQTT gateway dashboard](/assets/images/zigbee/progress_zigbee/Zigbee2MQTT_gatewayDashboard.png)

Next part was the sniffing of the zigbee network of the commerical products which is shown in the image below
Capture was done with the nRF52480 nordic dongle device
![Nordic Sniffing device in action](/assets/images/zigbee/progress_zigbee/sniffer_device_inAction.jpg)

This was able to capture the information of the network in which it was able to capture information regarding when a deivce was joining the zigbee network (paring)
![Wireshark capture of the Zigbee Network](/assets/images/zigbee/progress_zigbee/wireshark_capture_deviceJoin.png)

In Wireshark you are able to apply filters to get the information you are looking for with these key words:
- ``` zbee.sec.key_id ```
- ``` zbee.sec.decryption_key ``` Allows you to find the Transport Key
- ``` zbee_nwk.addr == ADDRESS ``` Allows you to narrow the primary device

With these filters able to narrow down to which specific packet has the transport key (pkt 31) contains the standard network key transmitted at transport key

![Wireshark capture of transport key](/assets/images/zigbee/progress_zigbee/wireshark_capture_transportKey.png)

## 02/24/2026
With the zigbee2MQTT able to see a visualization of the mesh network IRL

![Zigbee Mesh Network IRL](/assets/images/zigbee/progress_zigbee/zigbee_meshNetwork_IRL.png)

## 02/25/2026
Able to see futher information in wireshark to see who is the communication with and how long they communicated for along with bytes payload 

Note to see further information ``` Statistical → conversations ```

![Wireshark capture information](/assets/images/zigbee/progress_zigbee/wireshark_statistical_capture.png)

## 02/26/2026
Once keys are obtain you are able to enter them in wireshark (in preference setting, go to protocol, search for zigbee, enter keys)

Here are a list of steps you can take:
1. Open the capture in Wireshark.
2. Go to Edit -> Preferences -> Protocols -> Zigbee.
3. Add the network key and any link keys in our possession.
4. Wireshark will then show decrypted APS payloads and higher-level Zigbee packets.

After successful decryption, packet types and readable application commands will be visible, such as Link Status or on/off cluster commands

![Information is Decrypted](/assets/images/zigbee/progress_zigbee/wireshark_keysObtained_InfoUnlocked.png)
![Information on end device Door sensor](/assets/images/zigbee/progress_zigbee/commerical_endDevice_info.png)

Went about setting up the Digi Xbee Zigbee Mesh Kit. For more information regarding the setup please refer to [DigiXbee Mesh Kit Setup](https://docs.digi.com//resources/documentation/digidocs/90001942-13/#containers/cont_zigbee_mesh_network_setup.htm?TocPath=Zigbee%2520Mesh%2520Network%2520Setup%257C_____0)

![Digi Xbee setup on XCTU](/assets/images/zigbee/progress_zigbee/DigiXbee_setup_XCTU.png)

## 02/27/2026
Able to configure the device to the end device to join the router
Following [guide line](https://forums.digi.com/t/force-the-end-device-connect-to-one-of-the-router/16661/5) helped

![End device to router](/assets/images/zigbee/progress_zigbee/DigiXbee_enddevice_to_router.png)

An import note is to be able to get the network view as shown above its import to put into API mode meaning set AP to [1]

Remeber to close the connection in order to send packets from end device to coordinator (refer to Digi Xbee Mesh Kit Documentaiton)

Able to craft packets and send them to coordinator
![ABle to see packets from coordinator](/assets/images/zigbee/progress_zigbee/DigXbee_packet_crafted.png)

![Able to see the interaction via end device](/assets/images/zigbee/progress_zigbee/DigiXbee_packet_sentRecieved_endDevice.png)

Side task: Note when working with pycharm to do the Digi Xbee MicroPython configuration cannot run both at the same time with XCTU and PyCharm since serial usb is occupied. Need to convert the end device to be remote to send the router to then coordinator. 

![Testing for microPython](/assets/images/zigbee/progress_zigbee/DigiXbee_microPython_example.png)

## 02/28/2026
More messing around in the XCTU via sending packets

![End device perspective](/assets/images/zigbee/progress_zigbee/DigiXbee_XCTU_messingAround1.png)
![Coordinator perspective](/assets/images/zigbee/progress_zigbee/DigiXbee_XCTU_messingAround2.png)
![Router perspective](/assets/images/zigbee/progress_zigbee/DigiXbee_XCTU_messingAround3.png)

## 03/02/2026
Tried getting the Xbee module to join the Zigbee2MQTT and it was a success, and it sees it as a router, however having difficulty getting logs or information

Commands to get the Digi Xbee module to join again from the console log are shown below

![Console log commands](/assets/images/zigbee/progress_zigbee/DigiXbee_console_log_info.png)

![Log confirmation of Xbee device joining](/assets/images/zigbee/progress_zigbee/Zigbee2MQTT_log_XbeeDevice_Join.png)
![Updated visual network](/assets/images/zigbee/progress_zigbee/zigbee2MQTT_visual_IRL.png)

## 03/03/2026

#### Sending spoofed packets via nRR52480
Setting up the nRF5280 Dongle to perform a WHAD (Wireless Hacking Device) to be able to spoof the end device with butterfly tool
**Note** would strongly recommend doing in a virtual enviornment
steps to setup virtual enviornment can be referenced [here](https://docs.python.org/3/tutorial/venv.html)
For more information and setup with the dongle and WHAD [please refer to here](https://whad.readthedocs.io/en/latest/install.html)
![WHAD setup on other device](/assets/images/zigbee/progress_zigbee/buttefly_WHAD.png)

[Investigate futher](https://whad.readthedocs.io/en/latest/cli/generic/wsniff.html)
https://medium.com/@biero-llagas/poc-modified-replay-attack-on-zigbee-in-2026-how-hard-can-it-be-2da75901fc7d

## 03/04/2026

Is there a way to get the Xbee module communicting with the Zigbee2MQTT, I have it on the network but there is a communication issue
Some sites to point the way:
 - [Xbee Guide from other members in community](https://community.hubitat.com/t/everything-xbee/2328)
 - [Hackday project look into more depth](https://hackaday.io/project/178435-mr-miffy-rgb-led-module/log/190831-communicating-with-zigbee2mqtt)
 - [Might prove useful for the configuration](https://www.zigbee2mqtt.io/guide/configuration/)

 [This (adding zigbee to zigbee2MQTT)](https://www.digi.com/support/knowledge-base/zigbee-home-automation) is imporant as it allows you to configure the Zigbee 3.0 Xbee module to be added to the network

Extra steps to help
Because you deleted the device from the Z2M dashboard, the Coordinator has "forgotten" the XBee. You must force a fresh association:

Open the Window: In your Zigbee2MQTT dashboard, click "Permit join (All)".

Reset the Network: In the XCTU console (after typing +++), type ATNR0.

Note: If ATNR is still missing from your view, use the physical reset button or type ATFR to reboot the radio.

Watch the Logs: As soon as the XBee reboots, look at the Z2M logs. You should see:

info: z2m: Device '0x0013a200425e914e' joined.

info: z2m: Successfully interviewed 'Xbee_router1'.

https://www.youtube.com/watch?v=BJ-jw_O3YF8

## 03/05/2026

Getting the other Xbee Modules configured to be routers for the mesh network topology

Xbee Module configued with the Zigbee2MQTT
CE 0
ZS 2
EE 1
E0 2
KY zigbeealliance
AP 1
AO 3

Able to configure all Digi Xbee Device to create the ZigBee Mesh Network as shown below

![Digi XBee ZigBee Network](/assets/images/zigbee/progress_zigbee/DigiXbee_ZigBee_MeshNetwork.png)

A test to confirm if the sniffer will be able to pick up the Digi Xbee Mesh network (yes maybe, need further investigation into pcap)

## 03/06/2026
Further investigation into the pcap file 

So far what you are able to see is the devices that are communcating with the mesh network
In the pcap file capture we have MAC address of the Xbee Modules as well as the DST PAN IDs
![Pcap Capture of Digi Xbee Mesh Network](/assets/images/zigbee/progress_zigbee/Wireshark_DigiXbee_captureTest1.png)

What this also means in the pcap analysis is that 
1. **Mesh Logic:** Even though the final target is the End Device (0xFF8E), the Coordinator is physically sending this packet to ROUTER_1. This proves that your configuration worked—the Coordinator is using the Router as a "next hop" rather than talking to the End Device directly.
2. **APS Layer vs. MAC Layer ACKs:**
    - MAC ACKs (Rows 12-20): These are "hop-by-hop" confirmations. They only prove the radio signal made it to the next immediate neighbor.
    - APS ACKs (Row 11): These are "end-to-end" confirmations. This is the Coordinator telling the End Device, "I received your data and processed it at the application level."

You are able to see the Address of the Xbee Modules being used in the Mesh network
- 0x0000 = Coordinator
- 0x3c1c = Router 1
- 0x621b = Router 2
- 0xFF8E = End device

commands to narrow down what you are looking for 
``` zbee_nwk.addr == ADDRESS ```

Need to enable encryption to be able to read transport keys, key parameters
- EE = 1
- EO = 1
- KY = 0x59 (KeyAlliance09 "standard")

These allow you to be able to from an encrupted mesh network that can then be sniffed with the dongle device then you can narrow down with the previous commands
An image of the keys captured:

![Key Captured via the Digi Xbee Zigbee Mesh network](/assets/images/zigbee/progress_zigbee/Wireshark_DigiXbee_Key_captured.png)
