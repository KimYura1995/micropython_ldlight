# This file is executed on every boot (including wake-boot from deepsleep)

import esp

esp.osdebug(None)

import uos, machine

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc, network

#import webrepl

#webrepl.start()

gc.collect()


ssid = 'Kim_Main'
password = 'kimyura1995'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
	pass

print('Connection success')
print(station.ifconfig())
