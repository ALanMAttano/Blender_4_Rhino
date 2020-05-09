bl_info = {
    "name": "New Rhino Object - A Blender 4 Rhino",
    "author": "Alan Mattano, Soaring Stars lab",
    #"co-authors": "A. Negro, ",
    "version": (0, 7),
    "blender": (2, 81, 0),
    "location": "View3D > Add > Mesh > New Rhino Object",
    "description": "Adds a new Mesh Object - A Blender 4 Rhino",
    "warning": "",
    "wiki_url": "https://github.com/ALanMAttano/Blender_4_Rhino",
    "category": "Add Mesh",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Import a Rhino Mesh Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Add Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):        
        
        full_path_to_file = "X:\DoNotMove\Rhino-Blender-mesh.obj"
        # bpy.ops.import_scene.obj(filepath=full_path_to_file)
        bpy.ops.import_scene.obj(filepath=full_path_to_file, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl")

        return {'FINISHED'}

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Add Rhino Object",
        icon='PLUGIN')
        
        
# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://discourse.mcneel.com/t/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "rhino-to-blender-mesh-bridge-import-and-export/94448"),
    )
    return url_manual_prefix, url_manual_mapping

#----------------------------------------------------------------------------

class OBJECT_OT_add_objectexport(Operator, AddObjectHelper):
    """Import a Rhino Mesh Object"""
    bl_idname = "mesh.add_objectexport"
    bl_label = "Save Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):        
        
        print("Exporting...")
        full_path_to_file = "X:\DoNotMove\Rhino-Blender-mesh.obj"
        bpy.ops.export_scene.obj(filepath=full_path_to_file, use_selection=True)

        return {'FINISHED'}

def add_objectexport_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_objectexport.bl_idname,
        text="Save Rhino Object",
        icon='PLUGIN')


# Registration

def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)
    
    bpy.utils.register_class(OBJECT_OT_add_objectexport)
    bpy.types.VIEW3D_MT_mesh_add.append(add_objectexport_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)
    
    bpy.utils.unregister_class(OBJECT_OT_add_objectexport)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_objectexport_button)


if __name__ == "__main__":
    register()
