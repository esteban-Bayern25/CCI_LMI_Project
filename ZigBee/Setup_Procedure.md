# Configuration and Setup for ZigBee Network

**Note** All equipments that are involved in the creation of the zigbee network and tests are listed at the bottom of this README.

## Setting up the Zigbee Coordinator Commerical Grade Equipment

### 1. Setting up the ZigBee Coordinator

Using a Raspberry Pi 5 and the Sonoff Zigbee 3.0 USB Dongle Plus, you can create a ZigBee network and interact with devices through Zigbee2MQTT.
Begin by setting up the Raspberry Pi 5 as you normally would: install the operating system onto a microSD card, insert it into the device, and power it on. Once the system is running, enable SSH so you can remotely access and configure the Raspberry Pi from another computer. This will allow you to complete the remaining setup steps and interact with the terminal more easily. Next, follow a setup guide to configure the Raspberry Pi with the Sonoff Zigbee 3.0 USB Dongle Plus-E and a ZigBee motion sensor. This process will install and run Zigbee2MQTT, which creates an open MQTT bridge for ZigBee devices, allowing them to communicate with other systems and applications.

1. Plug in the Zigbee 3.0 USB Dongle Plus into one of the USB ports of the Rasberry Pi 5

2. To ensure the device is present run this command:

``` bash
ls /dev/serial/by-id
```
Once the device is listed, which has a long name

3. Install and enable a local MQTT broker for Zigbee2MQTT to publish data.

``` bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
```

To ensure that it is working run the command:
``` bash
mosquitto_sub -t zigbee2mqtt/bridge/state -v
```
Nothing prints until Zigbee2MQTT starts publishing, which is normal.

4. Clone the repository and install Node.js and pnpm, then install dependencies.

```bash
sudo apt install -y git curl
sudo git clone https://github.com/Koenkk/zigbee2mqtt.git /opt/zigbee2mqtt
cd /opt/zigbee2mqtt
```

Install latest update of dependencies

``` bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
```

```bash
sudo npm install -g pnpm
```
``` bash
sudo pnpm install
```
Zigbee2MQTT repository is cloned and dependencies are installed to allow starting the service.

5. Configure Zigbee2MQTT

``` bash
sudo nano /opt/zigbee2mqtt/data/configuration.yaml
```
    
**Note** The configuration.yaml should already be setup up, please observe or if you would like to make changes edit the .yaml file

6. Launch Zigbee2MQTT and watch it initialize.

``` bash
cd /opt/zigbee2mqtt
sudo npm start
```
Expected result: You should see output similar to:

``` 
Starting Zigbee2MQTT...
Zigbee2MQTT started!
```

7. Access the Zigbee2MQTT UI, Open the Zigbee2MQTT frontend to manage devices and permit joining.
In a browser on your local network go to the Pi IP and port 8080.

``` bash
http://<your_pi_ip>:8080
```

Add devices to the Zigbee2MQTT and can get a network as shown below: 

![Network Visual of Zigbee2MQTT](/assets/images/zigbee/progress_zigbee/zigbee2mqtt_network_visual.png)

### Setting up the nRF52840 Dongle for Sniffing

Please refer to [nRF52840 Dongle Documentation](https://docs.nordicsemi.com/bundle/ug_nrf52840_dongle/page/UG/nrf52840_Dongle/intro.html)

Please refer to [nRF52840 Dongle Sniffer Documentaiton for 802.15.4](https://docs.nordicsemi.com/bundle/ug_sniffer_802154/page/UG/sniffer_802154/intro_802154.html)

**Note** The Dongle is already configured and flash you just need to install the dependencies onto your computer and test via wireshark.

### Configuration of the Digi Xbee Router Module for Test 2

To get an xbee module properly configur and join the Zigbee2MQTT network (configured with the rasbperry pi and SonOFF Dongle Plus), similar to the router configuration

**Note** The modules should already be flashed with the lastest Zigbee firmware

These are the following parameters that need to change:
- CE Device Role: Join Network [0]
- ZS Zigbee Stack Profile: 2
- JV Coordinator Verification: Enabled[1]
- NI Node Identifer: router_xbee
- EE Encryption Enable: Enabled[1]
- EO Encryption Options: 2
- SM Sleep Mode: No Sleep (Router)[0]
- SP Sleep Time: 1F4
- AP API Enable: API Mode Without Escapes [1]

For addtional informaiton please refer to the link below on xbee working with Zigbee2MQTT
- [digi xbee modules communicate with other](https://www.digi.com/support/knowledge-base/can-digi-s-xbee-zb-modules-communicate-with-other)
- [zigbee home automation](https://www.digi.com/support/knowledge-base/zigbee-home-automation)
- [pdf documentation](https://docs.digi.com/resources/documentation/digidocs/pdfs/90001539.pdf)


## Setting up the Digi Xbee Zigbee Mesh Network

[Refer to Documentation on the Xbee Zigbee Mesh Kit User Guide](https://docs.digi.com//resources/documentation/digidocs/90001942-13/#concepts/c_xbee_zigbee_mesh_kit.htm?TocPath=XBee%2520Zigbee%2520Mesh%2520Kit%2520User%2520Guide%257C_____0)

Would also recommend installing the [Digi Xbee Studio Application](https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/digi-xbee-studio)

For configuration parameters on the digi xbee modules:
- CE (Device Role): Defines the node’s function within the Zigbee stack. One node was designated as the
Network Coordinator [1] to initialize the network, while the remaining three were configured as Routers [0]
to facilitate multi-hop communication and mesh redundancy..
- ID (Extended PAN ID): A specific identifier (2026) was assigned to all modules. This ensures all nodes join
the same logical network and prevents cross-talk with other 2.4 GHz deployments in the vicinity
- ZS (Zigbee Stack Profile): Set to 2 (Zigbee PRO). This profile is mandatory for Zigbee 3.0 compatibility,
enabling advanced routing algorithms and support for larger node populations.
- JV (Channel Verification): Enabled on all Router nodes. This forces the routers to verify the presence of the
Coordinator on a specific operating channel before joining, ensuring a stable connection to the Trust Center.
- EE (Encryption Enable): Set to Enabled [1] to activate 128-bit AES symmetric encryption. This ensures data
confidentiality across both the Network (NWK) and Application Support Sub-layer (APS) layers.
- AP (API Enable): Configured to API Mode with Escapes [2]. This mode allows the host workstation to interact
with raw data frames rather than simple transparent text. This is a prerequisite for capturing the detailed packet
metadata required for the subsequent security and latency analysis.
- Baseline Configuration: All auxiliary parameters not explicitly listed—including Radio Frequency (RF) power
levels (PL), scan durations (SD), and network hop limits (NH)—were maintained at their factory default values.
This ensures that the performance results reflect the standard operational behavior of the Zigbee 3.0 protocol
without specialized optimization

### Setting up the WHAD device

**Note:** The nrf52840 dongle should already be flashed with the WHAD butterfly properties

For more informaiton please refer to the [open source whad docs](https://whad.readthedocs.io/en/latest/cli/generic/winject.html)


### **Equipement list**

| Commerical | Development Hardware | 
| --- | --- | 
| ZigBee coordinator ([SONOFF ZigBee 3.0 USB DonglePlus](https://sonoff.tech/en-us/products/sonoff-zigbee-3-0-usb-dongle-plus-zbdongle-p?srsltid=AfmBOoq05n5bl2pB1xAz3aOx3RIwYfIqM_I8NbOEmXzF3O2efw0Ij0s7))[^3] & [Another option for Coordinator](https://www.amazon.com/SMLIGHT-SLZB-07-Coordinator-Zigbee2MQTT-Assistant/dp/B0D737SJ5G?dib=eyJ2IjoiMSJ9.ppEgVhHKzbBp2a7RAhwpKX6zOrDh5UNGyvyNEn3H8PcEgEU3sqjH5ArnFaR6rVdX.pkkkl2FxHrIR1luYNXO4iFdPaTO-r5mrSv_TGE252qA&dib_tag=se&keywords=SLZB-07&qid=1741067435&s=electronics&sr=1-1&linkCode=sl1&tag=smarthomescen-20&linkId=2d3a69d903fbd973ba5ec0f5371f7774&language=en_US&ref_=as_li_ss_tl&th=1) | [RaspberryPi 5](https://www.digikey.com/en/products/detail/raspberry-pi/SC1432/21658257) | 
| ZigBee routers x2-4 (IoT smart Plug/ [Sonoff S31 Lite zb](https://sonoff.tech/en-us/products/sonoff-s31-lite-zb-smart-plug-us-type-zigbee-version?srsltid=AfmBOoouOWD-7qDYsYzVtx6ROJP727KxYbj710cNZLtBlKKkP0D6Rc7Z) or [ZBBridge-P](https://sonoff.tech/en-us/products/sonoff-zigbee-bridge-pro?pr_prod_strat=pinned&pr_rec_id=67b491ac0&pr_rec_pid=8812959826161&pr_ref_pid=8812958646513&pr_seq=uniform)) | [XBee 3 Pro Module](https://www.digi.com/products/embedded-systems/digi-xbee/rf-modules/2-4-ghz-rf-modules/xbee3-zigbee-3) | 
| |[End devices](https://www.digi.com/products/models/xb3-24z8st) |

**Digi Key Parts**
- [Digi XBee 3 Zigbee Mesh Kit](https://www.digikey.com/en/products/detail/digi/XK3-Z8S-WZM/8130956?utm_source=ecia&utm_medium=aggregator&utm_campaign=digiintl)
- nRF Sniffer for 802.15.4 [^2]
    - [nRF52840 Dongle](https://www.digikey.com/en/products/detail/nordic-semiconductor-asa/NRF52840-DONGLE/9491124?utm_source=oemsecrets&utm_medium=aggregator&utm_campaign=buynow) 
- [ZigBee startup kits/ home guide](https://www.youtube.com/watch?v=fHq2Bzrsnr8)

**software/ logger tools**
- python
- wireshark
- scapy
- [WHAD](https://whad.readthedocs.io/en/latest/cli/generic/winject.html)
- Zephyr RTOS
- [API](https://docs.zephyrproject.org/apidoc/latest/structieee802154__radio__api.html) 
- nRF Connect for Desktop
- zperf (Zephyr Utility)
- Pyserial
- Zigbee2MQTT or Home Assistant (ZHA)
- [ApiMote](http://apimote.com/)
- [nRF Sniffer for 802.15.4](https://docs.nordicsemi.com/bundle/ug_sniffer_802154/page/UG/sniffer_802154/intro_802154.html)


