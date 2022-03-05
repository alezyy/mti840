#---------------------------------------------------------
#
#		This is a program for Barometer Pressure Sensor
#	Module. It could measure the pressure and temperature.
#
#		This program depend on BMP085.py writted by
#	Adafruit.
#
#	   Barometer Module			   Pi
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SCL ----------------- SCL1
#			SDA ----------------- SDA1
#
#---------------------------------------------------------
#!/usr/bin/env python3

#import Adafruit_BMP.BMP085 as BMP085

import Adafruit_Python_BMP.Adafruit_BMP.BMP085 as BMP085

import time
import json
import requests


# Constants

API_KEY          = "RASPBERRY_PI_DEMO_TOKEN"
THINGSBOARD_HOST = "96.126.105.251"

thingsboard_url  = "http://{0}/api/v1/{1}/telemetry".format(THINGSBOARD_HOST, API_KEY)

data = {}

def setup():
	print ('\n Barometer begins...')

def loop():
	while True:
		sensor = BMP085.BMP085()
		temp = sensor.read_temperature()	# Read temperature to veriable temp
		pressure = sensor.read_pressure()	# Read pressure to veriable pressure
		tempo = '{0:0.2f} C'.format(temp)
		pression = '{0:0.2f} Pa'.format(pressure)
        
	#temp = {0:0.2f} C.format(temp);

		#print ('')
		#print ('      Temperature =', tempo)		# Print temperature
		#print ('      Pressure =', pression)	# Print pressure
		
		data['temperature'] = tempo
		data['pressure']    = pression
		
		#r = requests.post(thingsboard_url, data=json.dumps(data))
		print(str(data))
		
		
		time.sleep(5)
		print ('')

def destroy():
	pass

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()