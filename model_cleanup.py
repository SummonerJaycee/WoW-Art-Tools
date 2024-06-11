import bpy



bpy.ops.object.editmode_toggle()

bpy.ops.mesh.delete_loose()

bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.mesh.tris_convert_to_quads(uvs=True, vcols=True, seam=True, materials=True)

bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.mesh.remove_doubles(threshold=0.0001)
 
bpy.ops.object.editmode_toggle()