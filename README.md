# Blender 4 Rhino
by SoaringStarsLab


```
Version 0.7
```

## The Rhino Blender Bridge


![This is an image](https://github.com/ALanMAttano/Blender_4_Rhino/blob/master/Blender4RhinoBridge1k.jpg)



### FULL DESCRIPTION

**"A Blender 4 Rhino" is a mesh Blender bridge for Rhino. Let you export the selected mesh from Rhinoceros 3D using a (custom) button. Import that mesh quickly inside Blender (using this plugin script). The python file for Blender let you import and export using one button. In Rhino, pressing right-click on this custom button will import back the Blender mesh.**


### FREE LICENSE

¡Do whatever you want with my software!

SOFTWARE WITHOUT ANY WARRANTY. 
INSPECT AND TEST IT RESPONSIBLY BEFORE USE.
Free License: https://github.com/ALanMAttano/Blender_4_Rhino/blob/master/LICENSE




### Quick Intro

BLENDER SETUP
* After a new Blender installation update
* Download Blender plug-in "A Blender 4 Rhino.py" file and place it somewhere on your PC
* Open it with a text editor
* Make a modification to the path pointing to your 3D mesh.obj file: `DoNotMove/...` folder
* Open Blender user preferences
* Go to Addons and press Install
* Select the Blender plug-in "A Blender 4 Rhino.py" file and select Install Addon
* In Blender Preference enable the plug-in
* Eventually, delete older versions
* Restart if necessary
* Under View3D, goto Add > Mesh > New Rhino Object, will load the mesh file
* In the same location, there is an export to save the mesh into the same location



RHINO SETUP
* Add a new custom button
* Open the file "A Blender 4 Rhino.txt"
* Copy the left and right command content of the .txt 
* Inside the Button Editor past both command scripts to left and right
* In Appearance select Both image and text
* Text: Blender
* Edit place the Blender icon image and press OK to save the image.
* Press OK to save and close the editor button.
* Close Rhino to Save the UI button layout. If you do not close Rhino you will lose the button.



HOW TO USE IT
* In Rhino, select the mesh that you want to pass to or edit on Blender.
* To export, Left-click on the custom Blender button bridge ("A Blender 4 Rhino")
* Open Blender and under View3D, select Add > Mesh > New Rhino Object: it will load the mesh file
* In Blender, after editing the mesh
* To export goto Add > Mesh > Save Rhino Object, to export the file back
* Inside Rhino, delete the file
* Right-click the custom Blender button bridge

Note you can automate the delete step by adding a `!Delete` command on top of the custom right button script





-----------------------



### Links
FORUM: https://discourse.mcneel.com/t/rhino-to-blender-mesh-bridge-import-and-export/94448

Blender Python Scripting Video Tutorials: 
* https://youtu.be/pim5YIfWv-M
* https://youtu.be/uahfuypQQ04

Supported funding platforms:
* Patreon: [soaringsimulator](https://patreon.com/soaringsimulator)
* PayPal: [paypal.me/SoaringClouds](http://paypal.me/SoaringClouds)
* BTC: https://www.blockchain.com/btc/address/3QSTuvAqTsYEz39A8SUMQQiu2oNgBZLUbU
* ETH: https://www.blockchain.com/eth/address/0x4110eceDEacf6304B53728ffF600CEE4B229cf3f
* [GOGO GURU](https://assetstore.unity.com/packages/3d/vehicles/land/gogo-allroad-tire-r16-157878) is not part of Blender4Rhino


2021 Alan Mattanó SoaringStarsLab
