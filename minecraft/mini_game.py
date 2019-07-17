
# Minecraft Pi Mini Game
# Created by Joe Coburn for Make Use Of
# 15/07/2015
# http://www.makeuseof.com/connecting-minecraft-pi-real-world-beginner-electronics

from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create() # create Minecraft Object

while True:
    x, y, z = mc.player.getPos()
    block_under_player = mc.getBlock(x, y - 1, z)
    
    if block_under_player == 12:
        # player standing on sand, start the timer
        random_time = random.uniform(0.1, 2.5) # generate random number
        time.sleep(random_time); # wait
        mc.setBlock(x, y - 1, z, 11) # turn it into lava
