
# Minecraft Pi House
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


from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
import time

mc = Minecraft.create() # create Minecraft Object

GPIO.setmode(GPIO.BCM) # tell the Pi what headers to use
GPIO.setup(14, GPIO.IN) # tell the Pi this pin is an input

while True:
    if GPIO.input(14) == True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x + 2, y - 1, z + 2, x + 7, y + 3, z + 8, 5) # make shell
        mc.setBlocks(x + 3, y, z + 3, x + 6, y + 2, z + 7, 0) # remove inside
        mc.setBlocks(x + 2, y, z + 5, x + 2, y + 1, z + 5, 0) # make doorway
        mc.setBlocks(x + 4, y + 1, z + 8, x + 5, y + 1, z + 8, 102) # make window 1
        mc.setBlocks(x + 4, y + 1, z + 2, x + 5, y + 1, z + 2, 102) # make window 2
        mc.setBlocks(x + 7, y + 1, z + 4, x + 7, y + 1, z + 6, 102) # make window 3
