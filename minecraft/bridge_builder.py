
# Minecraft Pi Automated Bridge Builder 
# Created by Joe Coburn for Make Use Of
# 15/07/2015
# http://www.makeuseof.com/connecting-minecraft-pi-real-world-beginner-electronics

from mcpi.minecraft import Minecraft
mc = Minecraft.create() # create Minecraft Object
	
while True:
    x, y, z = mc.player.getPos() # store player position
 
    # store the surrounding blocks
    a = mc.getBlock(x, y - 1, z + 1) 
    b = mc.getBlock(x, y - 1, z - 1)
    c = mc.getBlock(x - 1, y - 1, z) 
    d = mc.getBlock(x + 1, y - 1, z) 

    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        # 8 or 9 is water. Set surrounding blocks on floor to a solid (stone) if water is found
        mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 1, 1) 
        mc.setBlocks(x, y - 1, z, x - 1, y - 1, z - 1, 1) 
        mc.setBlocks(x, y - 1, z, x - 1, y - 1, z + 1, 1) 
        mc.setBlocks(x, y - 1, z, x + 1, y - 1, z - 1, 1)
