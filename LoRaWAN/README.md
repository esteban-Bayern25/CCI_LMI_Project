# Security Tests

## Vulnerabilities
LoRaWAN's cryptography is strong due to its use of AES-128, MIC validation, and session keys. Most of its weaknesses come from the implementation of LoRaWAN, specifically:
- Provisioning weaknesses
- Assumptions made about infrastructure trust
- Configuration errors

However, LoRaWAN implementations may be vulnerable to:
- Credential extraction
- Device cloning from identical credentials
- Reusing DevNonce values
- Malicious gateway
- Frame counter (FCntUp / FCntDown) reset after power loss
- Join flooding

## Credential Extraction
Objective: Extract AppKey and DevEUI if they are stored in plaintext on the end devices with physical access. Determine whether the AppKey is extractable from the firmware or if firmware readout is possible. 

### Setup:
1. Connect the end device to laptop.
2. Dump device's flash memory with esptool.py.
4. Identify the serial port using `mode`, for me it was COM8

![Esptool_size_output](../assets/images/lorawan/device_manager_showing_wireless_tracker_com8.png)  
5. Dump the entire flash.
```bash
# First detect boot size
python -m esptool --port COM8 flash-id
# Then dump flash, my detected flash size was 8mb so I used 0x800000
python -m esptool --port COM8 read-flash 0x00000000 0x800000 flash_dump.bin
```

This was my output:  
![Esptool_size_output](../assets/images/lorawan/esptool_size_output.png)  

3. If the dump is successful, find the AppKey and DevEUI. In my case, the dump was successful:
![flash_dump](../assets/images/lorawan/flash_dump.png)  
However, I needed to look through the binary file that was generated. I chose to use Ghidra since it is a well-known software reverse engineering framework. 
I opened Ghidra and searched for the AppKey that I used when I configured the AppKey using Arduino IDE:
![flash_dump](../assets/images/lorawan/app_key_in_dump.png)  
The AppKey, as well as the devEui and appEui were all stored in plaintext. After finding the specific address where these were found, I dumped the other device's flash memory and found that the keys were also stored in plaintext in the exact same addresses as before, which is a serious security vulnerability.  
![flash_dump_2](../assets/images/lorawan/other_dump.png) 


## Device Cloning
Objective: Ensure that LoRaWAN has protection against cloned identities, specifically devices with the same DevEUI and AppKey. 

Before setup, I made sure to capture packets of legitimate traffic as a baseline to compare to for this test. Below are screenshots of the logs in ChirpStack for both wireless trackers.
![flash_dump_2](../assets/images/lorawan/wireless_tracker_1_logs.png) 
![flash_dump_2](../assets/images/lorawan/wireless_tracker_2_logs.png) 
There are many instances of Confirmed Data Up, which means that the device sends packets and expects an ACK from the network server. There are also a few instances of Unconfirmed Data Down, which means that the server sent a downlink without requiring the device tto acknowledge it. This is the default for downlinks because it saves batery and airtime. The MultiTech Gateway was set up as a packet forwarder, which means it does not enforce reliability rules. 

After the baseline was done, I flashed identical credentials on the devices using these steps. 

### Setup:
1. Flash identical credentials on two end devices using the C++ file in this folder. The AppKey, DevEUI, and AppEUI are all the same. 
![flash_dump_2](../assets/images/lorawan/flashing_identical_keys.png) 
2. Power on both devices with batteries. 
3. Attempt to authenticate over the air on both devices, this is done automatically from the C++ program.
4. Observe if the server validates each device, or if any error logs are generated.

In my case, no error logs were generated. Both devices successfully joined using the same credentials. 
![device_clone](../assets/images/lorawan/device_clone.png) 
This highlights another serious vulnerability, where a rogue device can join the network once it has the same devEUI, appEUI, and appKey when joining with Over the Air Authentication (OTAA). 

## DevNonce Handling
Objective: Make sure that the network server rejects reused DevNonce values during Over The Air Authentication (OTAA). Specifically, demonstrate that LoRaWAN has replay protection to prevent reused DevNonce values.

For some devices, the DevNonce is stored in RAM and not persistent storage, which means the DevNonce value may reset if the device is reset. To test this, I captured join requests with ChirpStack and hit the reset button on the wireless tracker over and over again to see if there would be a different DevNonce value each time, and there was. This meant that the device did correctly create a new DevNonce everytime it wanted to join. This behavior helps prevent replay attacks since the network will reject any request to join that has the same DevNonce value as a prior attempt. This also meant that I had to change the firmware manually to send the same DevNonce for every join request.

### Setup:
In order to target the join procedure between an end-device and the COTS gateway:
1. Capture the join request through the network server logs, specifically recording the DevNonce.
2. Force the device to reboot without incrementing the DevNonce. Modify the firmware to send the same DevNonce as the last join request. I did this through changing the source code for the Arduino IDE library that I was using to flash the wireless trackers. In the source code, there is a file called `LoRaMac.c`, which specifically sets the DevNonce value. 
![devnonce_default](../assets/images/lorawan/devnonce_default.png) 
I changed this to be a static value, specifically a DevNonce value that I observed in the logs when the end-device sent a JoinRequest.
![modified_devnonce](../assets/images/lorawan/modified_devnonce.png) 
I flashed the wireless tracker with the new code. 
3. Transmit the join request with the DevNonce.
4. Observe if the network server accepted or rejected the request. I found that the server did not accept the request, which demonstrates how LoRaWAN prevents replay attacks by keeping track of DevNonce values.
![join_requests](../assets/images/lorawan/join_requests.png) 

## Malicious Gateway
Objective: Figure out if a malicious gateway that pretends to be legitimate can alter traffic from an end device to a real gateway.

### Setup:
1. Deploy both gateways, connect them to the same ChirpStack server.
2. Configure the Pi gateway to modify RSSI values, drop packets, and inject latency.
3. Observe if the server recieves the traffic as legitimate. 

## Frame Counter Persistence
Objective: Determine whether the end device persists FCntUp across power cycles, and correctly resumes session state after being rebooted. LoRaWAN prevents replay attacks with FCntUp, an uplink frame counter, and FCntDown, a downlink counter. If FCntUp resets to 0 after power is lost, it could lead to the server to be susceptible to join flooding or consume more battery than a normal uplink. 

### Setup:
1. Let the device reach a stable FCntUp.
2. Physically disconnect power and wait 10-20 seconds.
3. Restore power.
4. Observe the next uplink, and whether the server resumes count of the uplink, or resets.

In my case, I disconnected the wireless tracker from power for about 21 minutes. After reconnecting, it sent a join request to the server which the server accepted, and it reset the FCntUp to 0. After a device joins the network, the count is always reset to 0 and it starts adding one for each uplink. 
![fcnt](../assets/images/lorawan/fcnt_after_join.png) 
After reconnecting after several different time intervals ranging from 5 seconds to 5 minutes, I found that the wireless tracker always sends a join request when power is connected, which meants the FCnt never resumes after disconnecting since it is always intialized to 0 after joining. However, the dashboard on ChirpStack still indicates that the device is active even if it isn't powered. This is the expected behavior of LoRaWAN since a new session is created and each session uses new session key, which enforces replay protection. 

## Join Flooding
Objective: Evaluate whether the LoRaWAN network (gateway + ChirpStack server) is resilient against excessive or malicious join attempts that attempt to exhaust network resources. Specifically, determine whether repeated OTAA Join Requests can:
- Degrade network server performance
- Prevent legitimate devices from successfully joining

### Setup:
1. Configure one end device to repeatedly send OTAA join requests by modifying its firmware. I did this with Arduino IDE and the following code:
![join_request](../assets/images/lorawan/modified_code.png)

2. Have one other end device join legitimately
3. Observe logs on server to check if the device that was joining legitimately could join, or if the other device prevented it from joining. In my case, it didn't seem to impact legitimate traffic even though many join requests were sent. I also compared the time between each uplink and downlink during join flooding and without it, and didn't find much of a difference between the timing.   
This was the normal tracker with legitimate traffic:  
![join_request](../assets/images/lorawan/normal_tracker_during_joins.png)
And this was the device that was sending join requests every couple seconds: 
![join_request](../assets/images/lorawan/multiple_join_request_device.png)
Overall, it didn't seem to have much of an impact, so I would say that LoRaWAN does defend well against this attack. 

## Resilience to Malformed Frames
Objective: Make sure malformed frames do not crash the gateway or server.

### Setup:
1. Modify the end device's firmware to send an invalid MIC.
In order to modify the firmware, I modified the source code of the LoRaWAN library that I was using to flash the wireless trackers. Specifically, I modified the `LoRaMacComputeMic` function in `LoRaMacCrypto.c`. After the MIC is computed, I flip all of the bits, which produces an invalid MIC. 
![modified_mic_code](../assets/images/lorawan/modified_mic_code.png)
2. Observe how the gateway and server handle the malformed frames, whether they crash or if memory leaks occur. 
After flashing one of the wireless trackers with the modified code, this is what the logs in ChirpStack Docker containers looked like:
![invalid_mic_logs](../assets/images/lorawan/chirpstack_logs_invalid_mic.png)
Although there were no errors present in the dashboard, after the device successfully joined, there were no uplinks or downlinks that were shown in the logs. This meant that the packet was dropped immediately, which resulted in no errors taking place. I also tried this with a slight corruption where only the last byte is flipped (`*mic ^= 0x000000FF;`), and had the same results. This is what is expected in LoRaWAN, since LoRaWAN defines the MIC as the message integrity protection mechanism. If the MIC is computed to be invalid, there may have been packet tampering. If the MIC is invalid, the server should drop the uplink without forwarding it. This helps protect LoRaWAN against packet tampering attacks, MAC command injection, and replay attacks. This helps ensure the security and resilience of the network. 

## Mapping Vulnerabilities with STRIDE
| STRIDE Category  | LoRaWAN Vulnerability | Technical Impact |
| ------------- | ------------- | ------------- |
| Spoofing | Device Cloning | Devices with identical credentials as another authorized device and cause frame counter conflicts or cause DoS through identity collision |
| Tampering  | Comprimised Gateway | A rogue gateway can interfere with packets that end devices send to the server |
| Information Disclosure  | Credential Extraction | Through physical access to an end device, the AppKey and DevEUI may potentially be extracted if they are stored in plaintext on the device |
| Denial of Service (DoS)  | Join Flooding | By transmitting many fake join requests, it prevents authorized devices from joining and sending legitimate traffic |
| Elevation of Privilege | Network Server/API Misconfiguration | Attacker gains administrative access to the server, which allows them to register devices, modify keys, and disable security checks |