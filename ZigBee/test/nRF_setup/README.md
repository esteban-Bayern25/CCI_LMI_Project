# Setting up nRF52840 Dongle for Coordinator
[Setting up nRF Sniffer](https://academy.nordicsemi.com/topic/test/)
[Wireshark information with sniffer guide](https://docs.nordicsemi.com/bundle/ug_sniffer_802154/page/UG/sniffer_802154/running_sniffer_802154_ws.html)

[Page Tutorial](https://wiki.makerdiary.com/nrf52840-mdk-usb-dongle/guides/ncs/samples/zigbee/ncp/)
[Video Dongle Video](https://www.youtube.com/watch?v=kyPKIRQIacI&t=32s)

[Repo for Network Coordinator](https://github.com/makerdiary/ncs-playground/tree/main/samples/zigbee/network_coordinator)

[For linux VS code](https://docs.nordicsemi.com/bundle/ncs-latest/page/nrf/installation/install_ncs.html#install-ncs)

[Documentation for the XBEE Zigbee Mesh Kit](https://docs.digi.com//resources/documentation/digidocs/90001942-13/#concepts/c_xctu.htm?TocPath=Get%2520started%2520with%2520XBee%2520Zigbee%257C_____2)

[Setting up the home assistant](https://www.home-assistant.io/installation/raspberrypi)

https://github.com/makerdiary/ncs-playground?tab=readme-ov-file

https://wiki.makerdiary.com/nrf52840-mdk-usb-dongle/guides/ncs/setup/#get-the-code

https://wiki.makerdiary.com/nrf52840-mdk-usb-dongle/guides/ncs/samples/zigbee/shell/

https://github.com/kardia-as/zigpy-zboss

https://github.com/ffenix113/zigbee_home/discussions/8

https://shillehtek.com/blogs/news/raspberry-pi-zigbee-dongle-plus-e-zigbee2mqtt


https://www.youtube.com/watch?v=xvVvBKk9dN4

#### Want GPS?
https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/425/109020022_Web.pdf
https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/109020022/12323450
https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/110990031/5482557

#### Micropython Programming Approach
https://docs.digi.com/resources/documentation/digidocs/90002219/#reference/r_syntax.htm?TocPath=Differences%2520between%2520MicroPython%2520and%2520other%2520programming%2520languages%257CSyntax%257C_____0

**https://docs.digi.com/resources/documentation/digidocs/rf-docs/blu/blu-appdev-develop-micropython_t.html**
https://www.youtube.com/watch?v=ewImad6YckE

#### Setting up nRF52840 to be able to send pacekts links
https://www.home-assistant.io/integrations/zha/
https://github.com/zigpy/zigpy-xbee
https://pypi.org/project/zigpy-zboss/
https://github.com/ThomasGerstenberg/blatann
https://docs.nordicsemi.com/bundle/ncs-latest/page/zephyr/boards/nordic/nrf52840dongle/doc/index.html#nrf52840dongle
https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dongle/doc/index.html
https://docs.nordicsemi.com/bundle/ncs-2.9.2/page/nrf/samples/zigbee/shell/README.html
https://forums.digi.com/t/decrypting-encrypted-xbee3-traffic-wireshark/23700
https://digiblur.com/2021/08/21/zigbee-network-key-sniffing/

### Wireshark comands to filter
zbee.sec.key_id
zbee.sec.decryption_key (Allows you to find the Transport Key)
zbee_nwk.addr == 0xc4e9 (Allows you to narrow the primary device)

Zigbee Cluster Library (ZCL): defines standard clusters and commands so devices can interoperate.

Once we have the relevant keys, the decryption process is straightforward:


1 Open the capture in Wireshark.
2 Go to Edit -> Preferences -> Protocols -> Zigbee.
3 Add the network key and any link keys in our possession.
4 Wireshark will then show decrypted APS payloads and higher-level Zigbee packets.
After successful decryption, packet types and readable application commands will be visible, such as Link Status or on/off cluster commands:

#### Xbee working with Zigbee2MQTT
https://www.digi.com/support/knowledge-base/can-digi-s-xbee-zb-modules-communicate-with-other

https://www.digi.com/support/knowledge-base/zigbee-home-automation
https://docs.digi.com/resources/documentation/digidocs/pdfs/90001539.pdf

#### Sending spoofed packets via nRF52480