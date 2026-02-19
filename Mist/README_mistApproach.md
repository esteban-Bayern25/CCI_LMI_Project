# Documentation/ Library of Work for MIST

## Yocto Linux
Set of tools to create your own linux distribution
Bring embdeed device to market build working linux to get features you want (emulator)
[Yocto Linux](https://docs.yoctoproject.org/brief-yoctoprojectqs/index.html)
- [Video tutorial Yocto Linux](https://www.youtube.com/watch?v=yuE7my3KOpo)

## FMG Dongle - TS-7553-V2
[TS-7553-V2](https://www.embeddedts.com/products/TS-7553-V2#parts-accessories)

**Steps**

1. (Service Set Identifer) SSID - testlab gateway connects to your network of testing
2. Collector MQTT - IoT device logs

3. SSH



### Robust Category
Test 1 - Motion test
Stationary MMG and assocaited tags
then moving MMG with tags (motion test)

MMG as the gateway, reset the tags to rejoin the network and power cycle
rejoin relaibility testing

consistent route (slow, and fast moving) and observe stablization, tags properly reporting
tags continusly revieve messages when given

Test 2 - Maybe
Interference (jamming), show whether behavior is lost or remains the same 
generate 2.4GHz near the MMG 

Test 3 - behavior when cellular or backlog is lost
think power outage, backhaul
data buffer and flushes, reports from, data loss on backhaul outage
data loss or mmg stores the data, flushing behavior 
Credability mirors field deplyments 

### Security Category

Test 1 - Secure commisiong
stable and rejoin only of MMG moves or power cycle  (automatic rejoin)

Test 2 - rf slient until join (intentional), prejoin admissions are absent before it joins post 
sniffer to see establishment of MMG back to network, maybe tags included 

Test 3 - Over the air encryption -  maybe
frames are being protected, and plain text rf caputred 

### Latency Category
Test 1 - latency under Interference
tag event (motion, dynamic/trigger event) to MMG (Stationary) 
20 trials (base) time stamp, logs

Test 2 - latency under motion 
same thing when MMG is moving 

Test 3 - combining both Test 1 and Test 2
Another interfernece or distrubtion to MMG 



### Vulnerabilites
    - Access the UI on FMG Dongle 

- [Chip NXP i.MX6UL 696 MHz CPU Vulnerability](https://www.cve.org/CVERecord?id=CVE-2022-45163)