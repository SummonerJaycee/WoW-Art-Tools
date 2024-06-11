import bpy


for obj in bpy.context.selected_objects:
    for mat_slot in obj.material_slots:
        mat = mat_slot.material
        mat.blend_method = "OPAQUE"
        mat.shadow_method = "OPAQUE"
        node_tree = mat.node_tree
        nodes = node_tree.nodes
        nodes['Image Texture'].interpolation = "Cubic"
        if hasattr(nodes['Image Texture'], 'image'):
            if hasattr(nodes['Image Texture'].image, 'alpha_mode'):
                nodes['Image Texture'].image.alpha_mode = "NONE"