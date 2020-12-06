#Set the LED PIN
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin = 36
GPIO.setup(ledPin,GPIO.OUT)

deviceId = "YOUR_DEVICE_ID"
deviceKey = "YOUR_DEVICE_KEY"

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
