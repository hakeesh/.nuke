# --------------------------------------------------------------
#  shuffleShortcuts.py
#  Version: 1.0.0
#  Author: Will Hackett
#
#  Last Modified by: Will Hackett
#  Last Updated: July 20th, 1985
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Creates a shuffle node that shuffles RGBA channels into the Green channel.
# --------------------------------------------------------------

import nuke

# Define the function
def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):

    # Create a new shuffle node, and assign it to a variable so we can change some things...
    myShuffle = nuke.createNode("Shuffle")

    # Change the input & output channels to what is defined in the in_channel and out_channel arguments.
    myShuffle['in'].setValue(in_channel)
    myShuffle['out'].setValue(out_channel)

    # Change the relevant knobs to shuffle the RGBA channels to the green channel.
    myShuffle['red'].setValue(set_channel)
    myShuffle['green'].setValue(set_channel)
    myShuffle['blue'].setValue(set_channel)
    myShuffle['alpha'].setValue(set_channel)

    # Change the node colour to green (we have to convert Nuke's weird hex colour values to RGB to be a bit more human-readable)
    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1),16))

    # Add a node label
    myShuffle['label'].setValue("[value red] > [value out]")



# Define the function
def shuffleRGBchannels():

    # Create a variable for the selected node, before creating any shuffle nodes.
    selectedNode = nuke.selectedNode()

    # Get the X-Position and y-Position of the selected node.
    selectedNode_xPos = selectedNode['xpos'].value()
    selectedNode_yPos = selectedNode['ypos'].value()

    # Create our Red, Green & Blue Shuffle nodes, and assign them to a variable after creation.
    createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)
    redShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)
    greenShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)
    blueShuffle = nuke.selectedNode()

    # Set the input of the Red Shuffle node to the selected node, and Transform the Red Shuffle node down and to the left.
    redShuffle.setInput(0, selectedNode)
    redShuffle['xpos'].setValue(selectedNode_xPos-150)
    redShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Set the input of the Green Shuffle node to the selected node, and Transform the Green Shuffle node down.
    greenShuffle.setInput(0, selectedNode)
    greenShuffle['xpos'].setValue(selectedNode_xPos)
    greenShuffle['ypos'].setValue(selectedNode_yPos+150)

    # Set the input of the Blue Shuffle node to the selected node, and Transform the Blue Shuffle node down and to the right.
    blueShuffle.setInput(0, selectedNode)
    blueShuffle['xpos'].setValue(selectedNode_xPos+150)
    blueShuffle['ypos'].setValue(selectedNode_yPos+150)



# Add menu items to the Channel nodes menu
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)", "ctrl+shift+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to All)", "shuffleShortcuts.createCustomShuffle('alpha', 'rgba', 'alpha', 1, 1, 1)", "ctrl+shift+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 0)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "ctrl+shift+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 1)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "ctrl+shift+1", icon="alpha1Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "shuffleShortcuts.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)

