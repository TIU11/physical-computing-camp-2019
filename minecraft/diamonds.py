
# Minecraft Pi Diamond Detector
# Created by Joe Coburn for Make Use Of
# 15/07/2015
# http://www.makeuseof.com/connecting-minecraft-pi-real-world-beginner-electronics

import RPi.GPIO as GPIO
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # create Minecraft Object

led_pin = 14 # store the GPIO pin number

GPIO.setmode(GPIO.BCM) # tell the Pi what headers to use
GPIO.setup(14, GPIO.OUT) # tell the Pi this pin is an output

while True:
    # repeat indefinitely 
    x, y, z = mc.player.getPos()
    for i in range(15):
        # look at every block until block 15
        if mc.getBlock(x, y - i, z) == 56:
            GPIO.output(led_pin, True) # turn LED on
            time.sleep(0.25) # wait
            GPIO.output(led_pin, False) # turn LED off
            time.sleep(0.25) # wait
