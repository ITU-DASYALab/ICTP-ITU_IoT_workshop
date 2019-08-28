import machine
from network import WLAN
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == '__YOUR_SSID__':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, '__YOUR_PW__'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
