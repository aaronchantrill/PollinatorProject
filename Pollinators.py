#!/usr/bin/python3
# Written by Aaron Chantrill
# Intended to be run
# Temperature reporting based on
# https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
# picamera installed using sudo apt install python3-picamera
import datetime
import sys
import time
import Adafruit_DHT
from picamera import PiCamera


def get_filename(temperature):
    return datetime.datetime.now().strftime("/home/pi/%Y-%m-%d_%H.%M.%S_{}.h264".format(temperature))

while True:
    # Try to grab a sensor reading using the read_retry method
    # this will try to get a sensor reading up to 15 times
    # (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, "17")
    temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity))
        camera = PiCamera()
        camera.start_recording(get_filename(temperature))
        time.sleep(60*10) #  10 minutes
        camera.stop_recording()
        break
    else:
        # If you still failed to get a result, give up.
        print('Failed to get reading.')
        sys.exit(1)
