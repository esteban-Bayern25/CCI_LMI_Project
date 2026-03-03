# Progress updates for LMI

#### 02/23/2024
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
``` zbee.sec.key_id ```
``` zbee.sec.decryption_key ``` Allows you to find the Transport Key
``` zbee_nwk.addr == ADDRESS ``` Allows you to narrow the primary device

With these filters able to narrow down to which specific packet has the transport key (pkt 31) contains the standard network key transmitted at transport key
![Wireshark capture of transport key](/assets/images/zigbee/progress_zigbee/wireshark_capture_transportKey.png)

#### 02/24/2026
With the zigbee2MQTT able to see a visualization of the mesh network IRL

![Zigbee Mesh Network IRL](/assets/images/zigbee/progress_zigbee/zigbee_meshNetwork_IRL.png)

#### 02/25/2026
Able to see futher information in wireshark to see who is the communication with and how long they communicated for along with bytes payload 

Note to see further information ``` Statistical → conversations ```

![Wireshark capture information](/assets/images/zigbee/progress_zigbee/wireshark_statistical_capture.png)

#### 02/26/2026
Once keys are obtain you are able to enter them in wireshark (in preference setting, go to protocol, search for zigbee, enter keys)

![Information is Decrypted](/assets/images/zigbee/progress_zigbee/wireshark_keysObtained_InfoUnlocked.png)
![Information on end device Door sensor](/assets/images/zigbee/progress_zigbee/commerical_endDevice_info.png)

Went about setting up the Digi Xbee Zigbee Mesh Kit. For more information regarding the setup please refer to [DigiXbee Mesh Kit Setup](https://docs.digi.com//resources/documentation/digidocs/90001942-13/#containers/cont_zigbee_mesh_network_setup.htm?TocPath=Zigbee%2520Mesh%2520Network%2520Setup%257C_____0)

![Digi Xbee setup on XCTU](/assets/images/zigbee/progress_zigbee/DigiXbee_setup_XCTU.png)

#### 02/27/2026
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

#### 02/28/2026
More messing around in the XCTU via sending packets

![End device perspective](/assets/images/zigbee/progress_zigbee/DigiXbee_XCTU_messingAround1.png)
![Coordinator perspective](/assets/images/zigbee/progress_zigbee/DigiXbee_XCTU_messingAround2.png)
![Router perspective](/assets/images/zigbee/progress_zigbee/DigiXbee_XCTU_messingAround3.png)

#### 03/02/2026
Tried getting the Xbee module to join the Zigbee2MQTT and it was a success, and it sees it as a router, however having difficulty getting logs or information

Commands to get the Digi Xbee module to join again from the console log are shown below

![Console log commands](/assets/images/zigbee/progress_zigbee/DigiXbee_console_log_info.png)

![Log confirmation of Xbee device joining](/assets/images/zigbee/progress_zigbee/Zigbee2MQTT_log_XbeeDevice_Join.png)
![Updated visual network](/assets/images/zigbee/progress_zigbee/zigbee2MQTT_visual_IRL.png)

#### 03/03/2026
Setting up the nRF5280 Dongle to perform a WHAD (Wireless Hacking Device) to be able to spoof the end device with butterfly tool

