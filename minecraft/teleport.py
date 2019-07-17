
# Minecraft Pi Teleporting
# Created by Joe Coburn for Make Use Of
# 15/07/2015
# http://www.makeuseof.com/connecting-minecraft-pi-real-world-beginner-electronics

import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create() # create Minecraft Object

GPIO.setmode(GPIO.BCM) # tell the Pi what headers to use
GPIO.setup(14, GPIO.IN) # tell the Pi this pin is an input

while True:
    if GPIO.input(14) == True: # look for button press
        mc.player.setPos(0, 0, 0) # teleport player
        time.sleep(0.5) # wait 0.5 seconds
