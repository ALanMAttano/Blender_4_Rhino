# Blender 4 Rhino
by SoaringStarsLab


```
Version 0.7
```




### FULL DESCRITION

**"A Blender 4 Rhino" is a mesh Blender brige for Rhino.
Let you export the selected mesh form Rhinoceros 3D using a (custom) botton. Import that mesh quicklly inside Blender (using this plugin script). The pyton file for Blender let you import and export using one button. In Rhino, pressing right click on this custom button, it will import back the Blender mesh.**


### FREE LICENSE

¡Do whatever you want with my software!

SOFTWARE WITHOUT ANY WARRANTY. 
INSPECT AND TEST IT RESPONSIBLY BEFORE USE.
Free Licens: https://github.com/ALanMAttano/Blender_4_Rhino/blob/master/LICENSE




### Quick Intro

BLENDER SETUP
* After a new Blender installation update
* Download Blender plug-in .py file and place it somewhere in your PC
* Open it with text editor
* Make a modification to the path pointing to your 3D mesh.obj file: `DoNotMove/...` folder
* Open Blender user preferences
* Go to Addons and press Install
* Select the Blender plug-in .py file and select Install Addon
* In Blender Preference enable the plug-in
* Eventually, delete older versions
* Restart if nesesary
* Under View3D, goto Add > Mesh > New Rhino Object, will load the mesh file
* In the same location there is an export to save the mesh into the same location


RHINO SETUP
* Add a new custom button
Left button command
! -_Export _GeometryOnly=_Yes _SaveTextures=_No _SaveNotes=_No _SaveSmall=_Yes
"X:\DoNotMove\mesh.obj"
VertexWelding=Unmodified YUp=Yes enter enter

Right Button Command
! -_Import
"X:\DoNotMove\mesh.obj"
MapYtoZ=Yes
enter


HOW TO USE IT
* Select the mesh
* Left click on this custom Blender button ("A Blender 4 Rhino")
* Open Blender
* Under View3D, goto Add > Mesh > New Rhino Object, will load the mesh file
* After editing the mesh
* To export goto Add > Mesh > Save Rhino Object, to export the file back
* Inside Rhino, delete the file
* Rhight click the custom Blender button bridge

Note you can automate delete step by adding !Delete on top of the custom button script





-----------------------



### Links
Web Page: https://discourse.mcneel.com/t/rhino-to-blender-mesh-bridge-import-and-export/94448

Blender Python Scripting Video Tutorials: 
* https://youtu.be/pim5YIfWv-M
* https://youtu.be/uahfuypQQ04


2020 Alan Mattanó Argentina and Italy.
