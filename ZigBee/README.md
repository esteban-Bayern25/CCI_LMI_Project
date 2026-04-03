# Navigating the Zigbee Folder

This directory contains the various subfolders and documentation required to replicate the security testing performed on the Zigbee IoT protocol. This README provides an outline to help you navigate the related work, experimental setups, and technical findings.


## [test/](/ZigBee/test/) Folder

This folder contains the core experimental procedures, script logic, and the high-level project roadmap.

- [nRF_setup](/ZigBee/test/nRF_setup/): Contains the Python configuration files and a dedicated README for initializing the nRF52840 dongle. Use this if you need to reconfigure the hardware interface.

- [python_scripts](/ZigBee/test/python_scripts/): A collection of custom Python scripts used for packet injection and automated exploitation during the Zigbee experiments. Each script is named according to its specific attack vector; refer to the internal README in that folder for detailed usage instructions. 

- [Test Procedure Outline](/ZigBee/test/README_Testprocedure.md): A comprehensive guide providing an in-depth explanation of the experimental setup. It includes visual aids and step-by-step instructions to recreate the sniffing and injection tests. [^1]

- [Test Outline Powerpoint](/ZigBee/test/test_outline.pptx): The initial technical draft used to define our testing approach and incorporate stakeholder feedback on experimental methodology.

## [nRF_sniffer/](/ZigBee/nRF_sniffer/nRF-Sniffer-for-802.15.4/) Folder

- [nRF sniffer setup](/ZigBee/nRF_sniffer/nRF-Sniffer-for-802.15.4/) Provides the necessary documentation for users starting from scratch. This includes firmware flashing procedures and environment configuration for the nRF52840 dongle to enable 802.15.4 traffic interception. [^2]

## Setup_Procedure Documentation

This README serves as the primary technical manual for initializing the test environment. It provides step-by-step instructions for:

- Building the Zigbee Coordinator: Deploying the network hub using a Raspberry Pi and the Zigbee2MQTT bridge.

- Sniffer Configuration: Preparing nRF52840 dongles for 802.15.4 packet interception and raw frame injection.

- Digi XBee 3 Fine-Tuning: Modifying internal module parameters to ensure mesh stability and support advanced security testing.

- Equipment Inventory: A detailed list of all commercial smart devices and development hardware utilized in this research.

### References
[^1]:[Security Assesesment Reference](https://securelist.com/zigbee-protocol-security-assessment/118373/)
[^2]: [Setup Dongle Tutorial](https://youtu.be/ptY3lrboV-c?si=IevqJVBHtRSsnEBb)

