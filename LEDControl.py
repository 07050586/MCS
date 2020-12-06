#Set the LED PIN

#!/usr/bin/python3
import time
import sys
import http.client as http
import urllib
import json
import sys

import Adafruit_DHT

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

deviceId = "DI0lDXZT"
deviceKey = "JKrmh91UHfiIGP1c"

#Set MediaTek Cloud Sandbox (MCS) Connection
def get_to_mcs():
  host = "http://api.mediatek.com"
  endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/ledswitch/datapoints"
  url = host + endpoint
  headers = {"Content-type": "application/json", "deviceKey": deviceKey}
  r = requests.get(url,headers = headers)
  value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
  return value

# Receive the Data from MCS
while(Ture):
  if(get_to_mcs()==1):
	print("LED turning on.")
	GPIO.putput(ledPin,GPIO.HIGH)
	time.sleep(0.5)

  if(get_to_mcs()==0)
	print("LED turning off.")
	GPIO.output(ledPin.GPIO.LOW)
	time.sleep(0.5)
