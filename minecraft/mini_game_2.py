
# Minecraft Pi Mini Game 2
# Created by Joe Coburn for Make Use Of
# 15/07/2015
# http://www.makeuseof.com/connecting-minecraft-pi-real-world-beginner-electronics

import time
import random
from mcpi.minecraft import Minecraft 

mc = Minecraft.create() # create Minecraft Object

# clear area
mc.setBlocks(-10, 1, -10, 25, 5, 25, 0)

# create arena shell
mc.setBlocks(0, 0, 0, 25, 10, 25, 17)

# hollow out arena
mc.setBlocks(1, 1, 1, 24, 10, 24, 0)

# move player to arena
mc.player.setPos(14, 25, 20) # teleport player 

# make them stay put
# teleport player to start position every 1/10th second.
# do this for 5 seconds then start the game
time.sleep(2)
total_wait = 0
mc.postToChat("Waiting to Start")
while total_wait < 5:
    mc.player.setPos(14, 1, 20) # teleport player
    time.sleep(0.1)
    total_wait += 0.1

mc.postToChat("BEGIN!")

# 10 levels
for level in range(10):
    x, y, z = mc.player.getPos()
    level_time = 10 - level # reduce time by 1 second for each level
    mc.postToChat("Level - " + str(level + 1) + " start")

    # build floor
    mc.setBlocks(0, 0, 0, 25, 0, 25, 17)

    # make safe area
    safe_area_start = random.uniform(0, 22)
    safe_area_end = random.uniform(0, 22)

    mc.setBlocks(safe_area_start, 0, safe_area_end, safe_area_start + level, 0, safe_area_end + level, 57)

    elapsed_time = 0
    while elapsed_time < 10:
        x, y, z = mc.player.getPos()
        time.sleep(0.25)
        elapsed_time += 0.25
        # check player is still on floor
        if y < 0.75:
            mc.postToChat("Game Over")
            break;
    else:
        # remove floor
        mc.setBlocks(-10, 0, -10, 25, 0, 25, 8)

        # put safe area back
        mc.setBlocks(safe_area_start, 0, safe_area_end, safe_area_start + level, 0, safe_area_end + level, 57)
        time.sleep(2.5)
        continue
    break
