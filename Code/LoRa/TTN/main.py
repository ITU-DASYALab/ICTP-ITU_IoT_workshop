from network import LoRa
import binascii
import struct
# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.AS923)

dev_addr = struct.unpack(">l", binascii.unhexlify('26041D15'))[0]
nwk_swkey = binascii.unhexlify('8433EAA1CAF1396BCDEAE5A23143477C')
app_swkey = binascii.unhexlify('C338A27062A3D09DA14EEDC1482228DA')

lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

import socket
import time

while True:
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    s.setblocking(False)
    s.send(bytes([1, 2, 3]))
    s.settimeout(5.0) # configure a timeout value of 3 seconds
    try:
       rx_pkt = s.recv(64)   # get the packet received (if any)
       print(rx_pkt)
    except socket.timeout:
      print('Waiting to send new packet')
