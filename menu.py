# --------------------------------------------------------------
#  menu.py
#  Version: 1.0.0
#  Last Updated: July 8th, 2020
# --------------------------------------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform

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

nuke.knobDefault('Tracker.shutteroffset', "centered")
nuke.knobDefault('Tracker.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.knobDefault('Roto.cliptype','no clip')
nuke.knobDefault('RotoPaint.cliptype','no clip')
nuke.knobDefault('Tracker.adjust_for_luminance_changes','1')
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('Crop.crop','0')
nuke.knobDefault('STMap.uv', "rgb")
nuke.knobDefault('VectorBlur.uv', "motion")


# --------------------------------------------------------------
#  KEYBOARD SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------



# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Utilities menu & assign items ---

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')


# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon=dir+"/icons/myGizmos_icon.png")

