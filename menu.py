# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.7
#  Last Updated: August 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform
import nukescripts


# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\willh\.nuke'
MacOSX_Dir = '/Users/willhackett/.nuke'
Linux_Dir = '/home/willh/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None

	
	
# --------------------------------------------------------------
#  KNOB DEFAULTS  ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.knobDefault('Transform.label', "motionblur: [value motionblur]")
nuke.knobDefault('Merge2.label',"Mix: [value mix]")
nuke.knobDefault('VectorBlur2.label', "Channels: [value channels]\nUV: [value uv]\nmotionblur: [value scale]")
nuke.knobDefault('Roto.cliptype','no clip')
nuke.knobDefault('RotoPaint.cliptype','no clip')
nuke.knobDefault('Tracker4.adjust_for_luminance_changes','1')
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('Crop.crop','0')
nuke.knobDefault('VectorBlur2.uv', "motion")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

# --------------------------------------------------------------
#  KEYBOARD SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+shift+t", icon="Tracker.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Other/Backdrop", "nuke.createNode('BackdropNode')", "shift+b", icon="Backdrop.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Time/FrameHold", "nuke.createNode('FrameHold')", "ctrl+shift+f", icon="FrameHold.png", shortcutContext=2) 
nuke.menu('Nodes').addCommand("Merge/Premult", "nuke.createNode('Premult')", "shift+p", icon="Premult.png", shortcutContext=2)
nuke.menu('Nuke').addCommand('Edit/Paste', 'paste_selected.paste_selected()', 'ctrl+v')

# --------------------------------------------------------------
#  PYTHON SCRIPTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import shuffleShortcuts
import listNavigator
import filepathLister
import paste_selected
import shortcut_NodeCustomizer
import shortcut_operationSwitcher
import moblur_controller
import keylightdespill
import autoBackdropBW
import KeyingTemplate

# ----- MERGE NODE SHORTCUTS -----------------------------------
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+s", icon="Out.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+m", icon="In.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+p", icon="MergePlus.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+f", icon="From.png", shortcutContext=2)
mergeMenu.addCommand('Divide', 'nuke.createNode("Merge2", "operation divide")', "alt+d", icon="MergeDifference.png", shortcutContext=2)
mergeMenu.addCommand('Multiply', 'nuke.createNode("Merge2", "operation multiply")', "shift+alt+m", icon="MergeMultiply.png", shortcutContext=2)


# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")
myGizmosMenu.addCommand('NODE_DISABLER_v2', 'nuke.createNode("NODE_DISABLER_v2")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('bm_Lightwrap', 'nuke.createNode("bm_Lightwrap")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('bm_OpticalGlow', 'nuke.createNode("bm_OpticalGlow")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('DASgrain', 'nuke.createNode("DASgrain")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Edge_Expand', 'nuke.createNode("Edge_Expand")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('PA_EdgeMatte', 'nuke.createNode("PA_EdgeMatte")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('IBK_Colour_Plus', 'nuke.createNode("IBK_Colour_Plus")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Match_Black_White', 'nuke.createNode("Match_Black_White")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Erode_Fine', 'nuke.createNode("Erode_Fine")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('FractalBlur', 'nuke.createNode("FractalBlur")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('apDespill', 'nuke.createNode("apDespill")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('pProj', 'nuke.createNode("pProj")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('IllegalPixelFiller', 'nuke.createNode("IllegalPixelFiller")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('saturationcheck', 'nuke.createNode("saturationcheck")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('CameraMatchMover', 'nuke.createNode("CameraMatchMover")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Edge', 'nuke.createNode("Edge")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Reconcile3Dfast', 'nuke.createNode("Reconcile3Dfast")', icon="myGizmos_icon.png")
