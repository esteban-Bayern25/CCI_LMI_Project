# Proposed Course

1. Infrastructure-Dependent Availability & Energy Fragility (Primary Test)
2. Mobility & Reattachment Latency (Alternative Test)

#### Objective
To quantify the operational resilience and security-depth of NB-IoT compared to Mist by simulating realistic, high-impact failure and attack-adjacent scenarios that do not require cryptographic compromise or infrastructure impersonation.

This plan evaluates “Operational Security”: How easily can a system be disrupted, drained, delayed, or rendered unusable without breaking encryption?

### Test 1: Infrastructure-Dependent Availability & Energy Fragility (Security + Cost + Availability)
- **Thesis:** NB-IoT remains operationally vulnerable even when encryption is intact, because devices can be forced into repeated receive/transmit cycles from within the private network; Mist resists this failure mode due to its non-IP tags and cloud-validated request model.

- **The Scenario:** NB-IoT devices operate on IP once connected to a private APN. 
UEs inside the same private APN can:
  - Discover other NB-IoT devices
  - Send ICMP traffic
  - Force repeated RX/TX activity
which can cause battery exhaustion and denial of service

The "Spoofing" Twist: Instead of spoofing a base station, you spoof legitimate network activity.

- Use a malicious UE or PC inside the same private APN
  Perform:
  - ICMP ping sweeps
  - Repeated ping loops
  Force the victim UE into:
  - Continuous listen/respond cycles
  - Retransmissions
  - Energy drain


### Test 2: Mobility & Reattachment Latency (Mobility + Latency + Reliability)
- **Thesis:** NB-IoT performs poorly under mobility due to cell reselection and reconnection overhead; Mist maintains low-latency continuity through local gateways and stateless tags.

- **The Scenario:** You simulate realistic movement of devices between:
  - Coverage zones
  - Signal strengths
  - Indoor/outdoor environments
  while observing:
  - Disconnect duration
  - Packet loss
  - Time to resume normal reporting
 
The Goal: quantify NB-IoT's reconnection time, latency during movement, and data loss window in comparison to Mist




## Equipment List

**Devices**
- NB-IoT Development Board
  - [Nordic nRF9160 DK (recommended)](https://www.newark.com/nordic-semiconductor/nrf9160-dk/dev-kit-32bit-arm-cortex-m33/dp/84AC2295?&CMP=KNC-GUSA-GEN-SKU-OPTMYZR-ONBOARD-COMP&gad_source=1&gad_campaignid=22986376236&gbraid=0AAAAAD5U_g0Uyb2Ir5j3ksK9uRmFpIiUE&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xq1ldrmNJ_5IrvFfNfEnjhyNFgNrL3Pv8d1EqbJSsioiW_EDF1EUzkaAri9EALw_wcB)
  - [Quectel BG95 / BG96 dev kit](https://www.digikey.com/en/products/detail/iot-botscom/IBT-QTC-AFC-BG95/21411195?gclsrc=aw.ds&gad_source=1&gad_campaignid=20243136172&gbraid=0AAAAADrbLlgOPOK-6qeak9Ou_Pskp5Rzo&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xrt_1x0DuN96oFvm0olrWfebsF-hE9ZPjgneeebiyzkF4fOuNj37UUaAtSwEALw_wcB)
- NB-IoT SIM card with private APN access
  - Private APN enabled (test SIMs)

**Malicious / Test UE**
- LTE phone or USB LTE modem
  - Used to:
    - Join private APN
    - Create hotspot for laptop

**Host Systems** 
- Laptop (Linux preferred)
- [USB power meter](https://www.digikey.com/en/products/detail/olimex-ltd/USB-POWER-METER/21661970?gclsrc=aw.ds&gad_source=1&gad_campaignid=20228387720&gbraid=0AAAAADrbLlhDySYOomKA1lOOx0ll19x1R&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xotYOudvP_TsXhASTgN6QaxfmYkO5G5mWkH6cBvNx_pB2bW2vWzcqsaAiDlEALw_wcB)



**Company Provided**
- 1 Mist Gateway 
- 1 Mist Extender
- 2-3 Mist Tags


**Software/Logger Tools**
- Wireshark (LTE + 802.15.4 dissectors)
- Python
- PySerial (device logs)
- nmap / Zenmap (ICMP scan demonstration)
- tcpdump
- Power logging software (USB power meter)
- CSV logging scripts (Python)


### References
[Vulnerability Assessment Reference](https://cora.ucc.ie/bitstreams/74b32367-7e66-4c4b-9669-f16362f2234d/download)
[NB-IoT Energy Consumption Characteristics](https://arxiv.org/pdf/2005.13648)
[Energy Consumption Analysis of LPWAN Technologies](https://pmc.ncbi.nlm.nih.gov/articles/PMC7506725/?utm_source=chatgpt.com)
[NB-IoT vs Alternatives in Mobility and Delay](https://www.zipitwireless.com/blog/nb-iot-explained-is-it-right-for-your-iot-solution?utm_source=chatgpt.com)
