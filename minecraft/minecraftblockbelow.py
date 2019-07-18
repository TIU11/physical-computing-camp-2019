from gpiozero import LED, Button
from mcpi.minecraft import Minecraft
from time import sleep

mc = minecraft.create()

red = LED(22)
blue = LED(10)
green = LED (7)
button = Button(2)

air = 0
grass = 2
gold = 41

x,y,z = mc.player.getPos()
block_below = mc.getBlock(x,y-1,z)

while True:
    button.wait_for_press()
    sleep(0.1)
    mc.setBlock(x+1,y,z,gold)
    sleep(0.1)
    
    if block_below == air:
        red.on()
        blue.off()
        green.off()
    if block_below == grass:
        green.on()
        red.off()
        blue.off()
    sleep(0.1)