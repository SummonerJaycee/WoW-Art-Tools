import bpy


for obj in bpy.context.selected_objects:
    for mat in obj.data.materials:
        if not mat.use_nodes:
            mat.metallic = 0
            mat.specular = 0
            continue
        for n in mat.node_tree.nodes:
            if n.type == 'BSDF_PRINCIPLED':
                n.inputs["Metallic"].default_value = 0
                n.inputs["Specular IOR Level"].default_value = 0


