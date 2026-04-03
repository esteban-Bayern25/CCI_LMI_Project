import struct
from Crypto.Cipher import AES

def encrypt_zigbee_payload(payload, nwk_key, frame_counter, source_addr):
    # 1. Create the Nonce (13 bytes)
    # Includes Source IEEE Address, Frame Counter, and Security Control
    nonce = struct.pack("<Q", source_addr) + struct.pack("<I", frame_counter) + b"\x28"
    
    # 2. Setup AES-CCM Cipher
    # Zigbee uses AES-128 with a 4-byte MIC (integrity check)
    cipher = AES.new(nwk_key, AES.MODE_CCM, nonce=nonce, mac_len=4)
    
    # 3. Encrypt and generate MIC
    # The 'header' is the part of the Zigbee NWK layer that stays unencrypted
    ciphertext, mic = cipher.encrypt_and_digest(payload)
    
    return ciphertext + mic

# Example usage for  Management Leave command
target_ieee = 0xfffb40e06053b9a # From pcap
key = bytes.fromhex("7f4ab05ec85396ee07d8693d565c7209") #