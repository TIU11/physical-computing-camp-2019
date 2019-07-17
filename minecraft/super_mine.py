
# Minecraft Pi Super Mining Button
# Created by Joe Coburn for Make Use Of
# 15/07/2015
# http://www.makeuseof.com/connecting-minecraft-pi-real-world-beginner-electronics

import RPi.GPIO as GPIO
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create() # create Minecraft Object

GPIO.setmode(GPIO.BCM) # tell the Pi what headers to use
GPIO.setup(14, GPIO.IN) # tell the Pi this pin is an input

while True:
    if GPIO.input(14) == True: # look for button press
        x, y, z = mc.player.getPos() # read the player position

        mc.setBlocks(x, y, z, x + 10, y + 10, z + 10, 0) # mine 10 blocks 
        mc.setBlocks(x, y, z, x - 10, y + 10, z - 10, 0) # mine 10 blocks

        time.sleep(0.5) # wait 0.5 seconds
