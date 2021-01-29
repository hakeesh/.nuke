set cut_paste_input [stack 0]
version 12.1 v2
Constant {
inputs 0
channels rgb
color {0.03412080556 0.03360264376 0.03288039938 1}
name BG
selected true
xpos 3482
ypos 2845
}
Constant {
inputs 0
channels rgb
color {0 1 0 1}
name CLEANPLATE
selected true
xpos 3216
ypos 2570
}
clone node149d222ec00|Saturation|11520 Saturation {
saturation 0
name Saturation6
selected true
xpos 3231
ypos 2791
}
set Cd222ec00 [stack 0]
Merge2 {
inputs 2
operation divide
name Merge7
label "\[if \{\[value mix] != 1\} \{return \"\[value mix]\"\}]"
selected true
xpos 3231
ypos 2869
}
push $cut_paste_input
Dot {
name Dot9
selected true
xpos 2806
ypos 2407
}
set Nd222f400 [stack 0]
OFXuk.co.thefoundry.keylight.keylight_v201 {
show "Final Result"
unPreMultiply false
screenColour {0.09388703108 0.2177287936 0.086804308}
screenGain 1
screenBalance 0.5
alphaBias {0.6000000238 0.5 0.5}
despillBias {0.5 0.5 0.5}
gangBiases true
preBlur 0
"Screen Matte" 0
screenClipMin 0
screenClipMax 1
screenClipRollback 0
screenGrowShrink 0
screenSoftness 0
screenDespotBlack 0
screenDespotWhite 0
screenReplaceMethod "Soft Colour"
screenReplaceColour {0.5 0.5 0.5}
Tuning 0
midPoint 0.5
lowGain 1
midGain 1
highGain 1
"Inside Mask" 0
sourceAlphaHandling Ignore
insideReplaceMethod "Soft Colour"
insideReplaceColour {0.5 0.5 0.5}
Crops 0
SourceXMethod Colour
SourceYMethod Colour
SourceEdgeColour 0
SourceCropL 0
SourceCropR 1
SourceCropB 0
SourceCropT 1
balanceSet false
insideComponent None
outsideComponent None
cacheBreaker true
name Keylight3
selected true
xpos 2772
ypos 2631
}
Dot {
name Dot21
selected true
xpos 2803
ypos 2712
}
set Nd222e000 [stack 0]
push $Nd222f400
Dot {
name Dot30
selected true
xpos 3106
ypos 2434
}
Merge2 {
inputs 2
operation from
name Merge8
selected true
xpos 3086
ypos 2709
}
clone $Cd222ec00 {
xpos 3086
ypos 2790
selected true
}
Merge2 {
inputs 2
operation multiply
name Merge22
label "\[if \{\[value mix] != 1\} \{return \"\[value mix]\"\}]"
selected true
xpos 3079
ypos 2869
}
push $Nd222e000
Merge2 {
inputs 2
operation plus
name Merge9
label "Mix: \[value mix]"
selected true
xpos 2780
ypos 2863
}
