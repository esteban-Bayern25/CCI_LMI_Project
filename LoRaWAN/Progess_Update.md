MultiTech Gateway:
The gateway was set up according to the product page documentation. The web interface includes many different configurations, which were changed to allow ssh and connect wirelessly to the network for any updates. According to ChirpStack documentation, the ChirpStack Gateway Bridge was installed on the gateway, which is used to convert LoRa Packet Forwarder protocols into a ChirpStack common data-format. A Packet Forwarder has also been configured using the web interface, and it currently sends packets to the local Gateway Bridge. The gateway was added to ChirpStack, and it forwards LoRaWAN packets from the end-devices to the server. 
ChirpStack Server:
The ChirpStack server currently uses a Docker Compose file from the ChirpStack GitHub repository: https://github.com/chirpstack/chirpstack-docker. 

End-device:
Have been set up and connected to the ChirpStack server by adding an application to the ChirpStack server. The application allows devices to be added, but only if a device profile containing specific information like the region and MAC version is added. This device profile was used for both of the wireless trackers since they both run the same firmware. The application key and device EUI were both uploaded to the wireless trackers using Arduino IDE. By using Arduino IDE, the software on the trackers can be changed to run security tests. The ChirpStack server has very detailed logging of both uplinks and downlinks from each end-device. 

DIY LoRaWAN Gateway:
Although the Raspberry Pi 4 has been received, the HAT and other accessories needed to create the gateway have not yet been received. 