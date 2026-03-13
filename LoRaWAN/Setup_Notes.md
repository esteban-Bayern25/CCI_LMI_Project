# How to Setup a LoRaWAN network

## 1. Create a ChirpStack Server
A ChirpStack server can be created through Docker containers, which are found at https://github.com/chirpstack/chirpstack-docker. ChirpStack can also be hosted without docker since it provides Devian and Ubuntu packages for  installation. Although ChirpStack can run on the gateway, best practice is to run it on a separate server since it's easier to scale and better for monitoring. It also provides segmentation so that if the gateway goes down, the ChirpStack server is still up. 

1. Clone the repository: https://github.com/chirpstack/chirpstack-docker
```bash
git clone https://github.com/chirpstack/chirpstack-docker
```
Make sure to change the default configuration to match the frequency that is needed for your network. In the US, choose US915 for the frequency in the Docker Compose file. 

2. Change to the directory containing Docker Compose files
```bash
cd chirpstack-docker
```
3. Start the Docker containers
```bash
docker compose up
```
This will start up a ChirpStack server, a gateway bridge, a gateway bridge workstation, a REST API, mosquitto, and a postgresql container. 

## 2. Set up the Multi-Tech Gateway
The Multi-Tech gateway acts as a packet forwarder for any LoRaWAN packets that are transmitted by end-devices that have already established authentication on the server. It also receives downlink packets from the server and transmits them back over LoRa to the end-device. The gateway does NOT read the payload, and encryption keys are only held at the end-device and the network server. The gateway provides very little LoRaWAN-layer security. The gateway must be on the same frequency as both the end-devices and the ChirpStack server. 

1. Make sure all antennas are connected before giving the device power. Also make sure to connect the gateway to your PC via ethernet. 

2. Set a static IP on the ethernet adapter. I used an IP address of `192.168.2.10` and a default gateway of `192.168.2.1`. The default gateway is what you'll use to access the web UI of the gateway. 

3. Head to the default gateway that you set up. There should be steps to setup the gateway and set up an admin password. 

4. To create a packet forwarder, go to `LoRaWAN` > `Network Settings`. Under `LoRa Mode`, choose `PACKET FORWARDER`. In the `Server Settings`, type in `127.0.0.1` so that it sends the packets to the Gateway Bridge, which sends the packets to ChirpStack. Set the `Upstream Port` and `Downstream Port` to `1700`, which is the default port for the Semtech UDP Packet Forwarder Protocol. 

5. `Submit` changes and `Save and Apply` the changes. 

## 3. Set up the Gateway in ChirpStack
In order for the packets from the gateway to be seen by ChirpStack, it must  have the correct Gateway ID already configured in the server.

1. In ChirpStack, go to `Tenant` > `Gateways`, and add a new gateway.

2. Type in a name for the gateway and the Gateway ID, which is found on the physical gateway. 

3. `Submit` the changes, and go to the `Dashboard` to check if the gateway is online.

## 4. Set up the End-Devices (Wireless Trackers)

1. Install Arduino IDE.

2. Connect antennas BEFORE plugging the device into a PC via a usb-a to usb-c cable.

3. Follow the documentation here: https://docs.heltec.org/en/node/esp32/esp32_general_docs/lorawan/config_parameter.html to load LoRaWAN code onto the wireless tracker using Arduino IDE. The devEUI, appKey, and appEUI can all be configured using the example provided in the documentation. 

## 5. Set up the End-Devices in ChirpStack
In order to receive LoRaWAN packets from the end-devices, the server must know the 

1. In ChirpStack go to `Tenant` > `Device Profiles` and `Add Device Profile`. Make sure to choose the correct region, MAC version that the end-devices are running, and the ADR algorithm. Once all configurations have been set, `Submit`. 

2. Go to `Tenant` > `Applications` and choose `Add Application`. Create a name for the application and `Submit`.

3. In the application, add a device. The Device EUI, Join EUI, and Device profile must be chosen. The Device EUI and Join EUI corresponds to the DevEUI and AppEUI set in Arduino IDE. 

4. If successful, the devices should be shown as `Active` in the `Dashboard` when powered. 
