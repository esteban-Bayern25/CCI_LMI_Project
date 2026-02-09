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
- Frame counter (FCntUp / FCntDown) reset after power loss
- Device cloning due to poor key storage
- Join flooding due to improper retry backoff logic

## Credential Extraction
Objective: Extract AppKey and DevEUI if they are stored in plaintext on the end devices with physical access. Determine whether the AppKey is extractable from the firmware or if firmware readout is possible. 

### Setup
1. Connect the end device to laptop.
2. Dump device's flash memory with a tool like esptool.py.
3. If the dump is successful, find the AppKey and DevEUI.

## Device Cloning
Objective: Ensure that LoRaWAN has protection against cloned identities, specifically devices with the same DevEUI and AppKey. 

### Setup
1. Flash identical credentials on two end devices.
2. Power on both devices.
3. Attempt to authenticate over the air on both devices.
4. Observe if the server validates each device, or if any error logs are generated.

## DevNonce Handling
Objective: Make sure that the network server rejects reused DevNonce values during Over The Air Authentication (OTAA). Specifically, demonstrate that LoRaWAN has replay protection to prevent reused DevNonce values.

### Setup
In order to target the join procedure between an end-device and the COTS gateway:
1. Capture the join request through the network server logs, specifically recording DevEUI, DevNonce, and JoinEUI.
2. Force the device to reboot without incrementing the DevNonce. Modify the firmware to send the same DevNonce as the last join request.
3. Transmit the join request with the DevNonce.
4. Observe if the network server accepted or rejected the request.

## Malicious Gateway
Objective: Figure out if a malicious gateway that pretends to be legitimate can alter traffic from an end device to a real gateway.

### Setup:
1. Deploy both gateways, connect them to the same ChirpStack server.
2. Configure the Pi gateway to modify RSSI values, drop packets, and inject latency.
3. Observe if the server recieves the traffic as legitimate. 

## Frame Counter Persistence
Objective: Determine whether the end device persists FCntUp across power cycles, and correctly resumes session state after being rebooted. LoRaWAN prevents replay attacks with FCntUp, an uplink frame counter, and FCntDown, a downlink counter. If FCntUp resets to 0 after power is lost, it could lead to the server rejecting packets, battery drain, or the device may become unavailable. 

### Setup:
1. Let the device reach a stable FCntUp.
2. Physically disconnect power and wait 10-20 seconds.
3. Restore power.
4. Observe the next uplink, and whether the server resumes count of the uplink, or resets.

## Resilience to Malformed Frames
Objective: Make sure malformed frames do not crash the gateway or server.

### Setup:
1. Modify the end device's firmware to send an invalid MIC or corrupted MAC commands.
2. Observe how the gateway and server handle the malformed frames, whether they crash or if memory leaks occur. 