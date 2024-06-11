import bpy


bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.tris_convert_to_quads(uvs=True, vcols=True, seam=True, materials=True)
bpy.ops.mesh.remove_doubles()
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
bpy.ops.mesh.edges_select_sharp()
bpy.ops.transform.edge_crease(value=1, snap=False)
bpy.ops.transform.edge_bevelweight(value=1, snap=False)
bpy.ops.object.editmode_toggle()
bpy.ops.object.modifier_add(type='BEVEL')
bpy.context.object.modifiers["Bevel"].offset_type = 'WIDTH'
bpy.context.object.modifiers["Bevel"].width = 0.04
bpy.context.object.modifiers["Bevel"].segments = 2
bpy.context.object.modifiers["Bevel"].limit_method = 'WEIGHT'
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2

