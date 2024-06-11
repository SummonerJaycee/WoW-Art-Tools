import bpy


for obj in bpy.context.selected_objects:

    bpy.ops.object.origin_set(
        type='ORIGIN_GEOMETRY', 
        center='MEDIAN')
        
        
        
    bpy.context.object.location[1] = 0
    bpy.context.object.location[2] = 0
    bpy.context.object.location[0] = 0