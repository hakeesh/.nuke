# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.0
#  Last Updated: July 9th, 2020
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

--------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Utilities menu & assign items ---

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')


# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")
