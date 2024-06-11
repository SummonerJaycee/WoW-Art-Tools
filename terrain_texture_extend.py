import bpy


for obj in bpy.context.selected_objects:
    for mat_slot in obj.material_slots:
        mat = mat_slot.material
        node_tree = mat.node_tree
        nodes = node_tree.nodes
        if hasattr(nodes['Image Texture'], 'image'):
            if hasattr(nodes['Image Texture'].image, 'alpha_mode'):
                nodes['Image Texture'].extension = "EXTEND"
                
                

     