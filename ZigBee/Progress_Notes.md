# Progress Updates for LMI

## 02/23/2024
Setting up the ZigBee network with a raspberry pi 5 device, ZigBee MQTT mosquito, and a ZigBee Dongle P

![Image of the Zigbee Setup with Commerical Products](/assets/images/zigbee/progress_zigbee/zigbee_setup_commerical.png)

```bash
ssh hostname@IPaddress
```
you will have to enter a password

Once in need to cd into the zigbee2mqtt directory:

```bash
cd /opt/zigbee2mqtt
```
To start the process for the zigbee network

```bash
sudo npm start
```

Open a brower and go to the following link to open the Zigbee2MQTT dashboard 

```bash
http://X.X.X.X:8080/#/
```

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

END_DEVICE1 Configurations parameters:
- CE = 0
- ID 2015
- JV = 1
- EE = 1
- EO = 1
- SM = Cyclic Sleep [4]
- SP = 1F4

Able to configure the end device to broadcast GPS coordinates via MicroPython
[GPRMC Strucutre](https://docs.novatel.com/OEM7/Content/Logs/GPRMC.htm)

## 03/07/2026

Had to reset all the devices and try again
All devices now connceted to the mesh network

## 03/09/2026

All devices are communicating with one another

| Line Color  | Meaning | 
| ------------- | ------------- |
| Solid Green  | Active, high-quality routing path. |
| Dashed Grey  | Known neighbor, but no recent data.  |
| Inactive     | Device was seen but is now unreachable. |

![Setup Configurations](/assets/images/zigbee/progress_zigbee/DigiXbee_representation_configWCoord.png)

End device to connect to the router 

## 03/10/2026

For sniffing packets via the WHAD 
```bash
wsniff -i uart0 -w dot15d4 --channel 11 
```

Looking into for packet injection 
[Packet Injection](https://whad.readthedocs.io/en/latest/cli/generic/winject.html)
[Insightfull](https://www.youtube.com/watch?v=TZb6WDAmbnE)

## 03/11/2026

Network visualizer issue
Wanting to reset the network issue an AT Command NR
Allows device to retry and join the Coord Zigbee network
[Another experiment with sniffer](https://www.zigbee2mqtt.io/advanced/zigbee/04_sniff_zigbee_traffic.html#using-zsmart-systems-sniffer)

![New version of Xbee Studio](/assets/images/zigbee/progress_zigbee/DigiXbee_Studio_Zigbee_topology_better.png)

So far the packet sniffer allows for capture offline 

## 03/12/2026

analysis of the packet caputre from the Digi Xbee mesh network reset
[Useful Zigbee Analysus Wireshark link](https://www.exploitsecurity.io/post/zigbee-protocol)

- To see only Data Frames: ``` wpan.frame_type == 0x01 ```
- To see only Beacon Requests: ``` wpan.cmd.id == 0x07 ```

[Investigate into more](https://www.digi.com/support/knowledge-base/can-digi-s-xbee-zb-modules-communicate-with-other)
look into more: https://community.hubitat.com/t/everything-xbee/2328

Trying the WHAD device on the commerical zigbee network (it works with capturing the commerical grade equipment ZigBee Mesh Network)
Does work for capturing commerical grade routers via WHAD device and open source information

## 03/13/2025

Using the WHAD device we are able to use if as a sniffer for when the commerical grade equipment joins 

Before capture shows the device encrypted and not able to see the in detail information

![WHAD_device_capture_inforamtion](/assets/images/zigbee/progress_zigbee/WHAD_device_capture_before.png)

filter using the ``` zbee.sec.description_key ```

Then observing the info column you see a transport key and inspect the packet

![Capture of Commerical grade router 3](/assets/images/zigbee/progress_zigbee/WHAD_device_action_capture3Router.png)

Able to use the Key to then decrypt the traffic and information
![Information gathering](/assets/images/zigbee/progress_zigbee/WHAD_device_after_decryption.png)

Starting to test packet injection to perform the spoof disconnect

## 03/16/2026

When getting an xbee module device to connect to the zigbee2MQTT its imporant to set AO = 0 in which it allows it to be sucessfully connected to the zigbee network

Here you can see the device join the network 
- [Setup advice](https://www.digi.com/support/knowledge-base/can-digi-s-xbee-zb-modules-communicate-with-other)
- [Configration advice](https://www.digi.com/support/knowledge-base/zigbee-home-automation)

![Digi XBee joins Zigbee2MQTT network](/assets/images/zigbee/progress_zigbee/Xbee_router_join_Zigbee2MQTT.png)

Log informaiton sayings its sucessfully

![Log information confirming it joins](/assets/images/zigbee/progress_zigbee/Xbee_router_join_log_info.png)

From the packet injection the network is acknowledgeing it however the thirdreality plug did not turn off, something involving the frame counter
- Extended Nonce
- MIC verificaiton (security mechanism used to ensure that data packets have not been altered or corrupted during transmission)
- Frame Counter (The counter field used to provide frame freshness and to prevent the processing of duplicate frames.)

[try to see if you can from command line](https://www.youtube.com/watch?v=xTNpUBiBfNY)

## 03/17/2026

The ThirdReality plug sent an ACK! This confirms that winject command successfully hit the radio of the smart plug. The hardware "heard", but the reason it didn't turn off is that it hit the Zigbee Network Layer Security wall.

```bash
winject -i uart0 dot15d4 -c 11 [HEX STREAM VALUE]
```

![command to run the packet injection](/assets/images/zigbee/progress_zigbee/packet_injection_cmd_terminal.png)

![Packet Injection into Commerical Grade component (router 3)](/assets/images/zigbee/progress_zigbee/packet_injection_confirmed.png)

The MIC (Message Integrity Code) tied to the Frame Counter (ZigBee Encryption) is preventing the actural command to turn off

## 03/18/2026

Pivoted from the router to end device to foce it to leave the zigbee2mqtt network

for filter sequnce numbers ``` wpan.seq_no == # ```

Successful MAC-layer injection was verified using a dual-dongle setup. A spoofed frame (Source 0xEDFE, Seq 170) was transmitted via the ButteRFly dongle. A secondary sniffer captured immediate IEEE 802.15.4 Acknowledgement (ACK) frames from the target ThirdReality smart plug (0xE702). This confirms that the target device radio accepted the spoofed frame as a valid physical-layer transmission.

python file, while having both the sniffer dongle device and running in wireshark and the WHAD dongle device plugged in and already configured then run the following python file

```bash
python test_both_capture_and_inject.py
```

Then based on the [PCAP file capture of the injection](/assets/images/zigbee/zigbee_pcap_captures/packet_injection_capture_with_sniffer__dongle_test1.pcap)

able to see the packet injeciton that was performed on the Third Reality 3RSP02028BZ (router3_commerical) with narrowing it down to sequence number 170 as shown below

![packet injection via running python script towards router 3](/assets/images/zigbee/progress_zigbee/confirmation_of_packet_injection_whad.png)

## 03/19

Packet Injection on the xbee router to leave the zigbee2mqtt network

Analysis of the Capture
Frame 1 (The Attack): You can see a Data frame (actually the spoofed MAC Command) with Source: 0x0000 (the Coordinator) and Destination: 0x77fb (the XBee Router). This is your injected Coordinator Realignment (0x07) command.

Frame 2 (The Reaction): Immediately following your injection, the sniffer captured an IEEE 802.15.4 Beacon Request.

The Significance: A router only sends a Beacon Request when it is "orphaned" or searching for a network. This proves the XBee accepted your rogue command, moved to the Rogue PAN ID (0xDEAD), and—finding no legitimate hub there—began frantically searching for a new parent.

```bash
python packet_injection_on_xbee_router.py
```

![Running the python file](/assets/images/zigbee/progress_zigbee/cmd_line_running_script_inject_xbee_router.png)

Then you see from the packet sniffer captures information

![xbee router wireshark capture informaition](/assets/images/zigbee/progress_zigbee/wireshark_capture_xbee_router_leaving_network.png)

tried it again but this time the xbee router address changed so I needed to update the code pase

![xbee router cmd lind](/assets/images/zigbee/progress_zigbee/cmd_line_2_xbee_router_injection.png)

![wireshark capture of packets sent to xbee module](/assets/images/zigbee/progress_zigbee/wireshark_capture_packet_injection_2_on_xbee_router.png)

##03/20

The fact that you see an ACK in your latest capture (Frame 19) is a massive breakthrough for your experiment. It proves that your timing was perfect and the door_sensor_endDevice (0x1df4) physically "heard" and accepted your packet at the radio level.

However, the reason the sensor stayed on the network is the difference between Hardware Acceptance and Protocol Execution.

1. Analysis of the "Silent Failure"
In your screenshot image_b6df21.png, the sequence of events tells the whole story:

Frame 18 (The Injection): Your ButteRFly dongle sent the Realignment command to 0x1df4.

Frame 19 (The ACK): The door sensor's radio chip immediately sent a hardware acknowledgement. This confirms you hit the "wake-up window" while you were opening/closing the door.

The Discard: Even though the radio chip said "I got it," the Zigbee 3.0 Stack inside the Third Reality sensor likely discarded the command. Unlike the XBee Router, which is often more permissive with legacy commands, modern Zigbee 3.0 end devices typically ignore MAC-layer management frames (like 0x07 Realignment) unless they are encrypted with the Network Key.