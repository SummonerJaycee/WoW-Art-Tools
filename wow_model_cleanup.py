import bpy



#-------------------------------------------------------------------------------#
#                             model clean up                                    #
#-------------------------------------------------------------------------------#

class WoWModelCleanup(bpy.types.Panel):
    """Creates a panel on the Sidebar"""
    bl_label = "WoW Model Cleanup"
    bl_idname = "OBJECT_PT_WoWModelCleanup"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "WoW Model Cleanup"
    
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('wow_model_cleanup.creation_operator')
        

class CLEANUP_OT_CREATION(bpy.types.Operator):
    bl_label = "Clean Model"
    bl_idname = 'cleanup.creation_operator'
    
    
    def execute(self, context):
        
        
        bpy.ops.object.editmode_toggle()
        
        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.delete_loose()

        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.mesh.tris_convert_to_quads()

        bpy.ops.object.editmode_toggle()
            
            
        return {'FINISHED'}
        
        
def register():
        bpy.utils.register_class(WoWModelCleanup)
        bpy.utils.register_class(CLEANUP_OT_CREATION)
        
        
def unregister():
        bpy.utils.unregister_class(WoWModelCleanup)
        bpy.utils.unregister_class(CLEANUP_OT_CREATION)
        
        
        
if __name__ == "__main__":
    register()