import machine
import pycom
from network import WLAN
wlan = WLAN(mode=WLAN.STA)
import time
pycom.heartbeat(False)
while True:
    #nets = wlan.scan()
    for net in wlan.scan():
        if net.ssid == 'NH15_20':
            print('Network found!')
            rssi = net.rssi
            print(net.ssid, net.rssi)

            if rssi > -50:
                    pycom.rgbled(0x007f00) # green
                    print('excellent')                        
            elif rssi in range (-61,-49):
                    pycom.rgbled(0x7f7f00) # yellow
                    print ('average')
            else:
                    pycom.rgbled(0x7f0000) # red
                    print ('bad')
    time.sleep(1)
