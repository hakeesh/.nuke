# autoBackdropBW V1.0 by Nicolas Leu 05.03.2016
# Modification of Nukes built-in autobackdrop() function that will only use greyscale values as tile color instead of colors

import nuke
import random

def autoBackdropBW(): 
    ''' 
    Automatically puts a backdrop behind the selected nodes. 

    The backdrop will be just big enough to fit all the select nodes in, with room 
    at the top for some text in a large font. 
    ''' 
    selNodes = nuke.selectedNodes() 
    if not selNodes: 
      return nuke.nodes.BackdropNode() 

    # Calculate bounds for the backdrop node. 
    bdX = min([node.xpos() for node in selNodes]) 
    bdY = min([node.ypos() for node in selNodes]) 
    bdW = max([node.xpos() + node.screenWidth() for node in selNodes]) - bdX 
    bdH = max([node.ypos() + node.screenHeight() for node in selNodes]) - bdY 

    # Expand the bounds to leave a little border. Elements are offsets for left, top, right and bottom edges respectively 
    left, top, right, bottom = (-10, -80, 10, 10) 
    bdX += left 
    bdY += top 
    bdW += (right - left) 
    bdH += (bottom - top)

    # Define greyscale values for the backdrop's tile color
    numbers = [x / 100.0 for x in range(5,16,1)] + [x / 100.0 for x in range(25,51,2)]
    y = random.choice(numbers)
    hexColor = int('%02x%02x%02x%02x' % (y*255,y*255,y*255,1),16)

    n = nuke.nodes.BackdropNode(xpos = bdX, 
                                bdwidth = bdW, 
                                ypos = bdY, 
                                bdheight = bdH, 
                                tile_color = hexColor, 
                                note_font_size=42)

    # revert to previous selection
    n['selected'].setValue(False) 
    for node in selNodes: 
      node['selected'].setValue(True) 

    return n 



