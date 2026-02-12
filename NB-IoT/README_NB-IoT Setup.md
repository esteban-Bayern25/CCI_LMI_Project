# Inital Steps


## 1. Install Linux:
Prepare the Linux VM (VMware Workstation Pro)
The Linux VM is the replay station and what performs analysis.

1. Create a VM with:

- 2–4 CPU cores
- 8 GB RAM
- Bridged networking
- USB passthrough enabled


2. Install Core Tooling 
- >sudo apt update
- >sudo apt install wireshark tcpdump minicom python3-pip socat


## 2. Boot and Configure Raspberry Pi 5 
Pi 5 is the gateway proxy

1. Install Raspberry Pi 5 OS 

Enable SSH: 
- >sudo raspi-config

Update:
- >sudo apt update && sudo apt upgrade

Install Tools:
- >sudo apt install tcpdump iptables socat screen


## 3. Configure the Pi as a proxy relay
Pi 5 should sit between:
- NB-IoT Modem Connection
- Remote endpoint

Typical Options: 
- Serial-to-IP relay
- Transparent TCP proxy
- Logging bridge

Ex of serial relay: socat -v /dev/ttyUSB0,raw TCP-LISTEN:9000

This allows:
- message interception
- delay injection
- replay testing


## 4. Set Up the Digi XBee NB-IoT Development Kit
This is the UE device under test

Kit includes: 
- NB-IoT modem
- development board
- SIM
- antenna
- USB interface

Connect Hardware: 
- Attach antenna
- Insert SIM
- USB → Raspberry Pi (or Linux VM for initial config)

    You should see: 
  /dev/ttyUSB0
  /dev/ttyUSB1


Test Modem Communication:
- >sudo minicom -D /dev/ttyUSB0 -b 9600

Test AT Commands:
- >AT
- >AT+CSQ
- >AT+CGATT?


If attached to network:
- >AT+CEREG?


That confirms:
- modem power
- SIM authentication
- network registration




