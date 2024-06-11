import bpy


for obj in bpy.context.selected_objects:
    for mat in obj.data.materials:
        if mat.node_tree.nodes['Normal Map']:
            node_to_delete = mat.node_tree.nodes['Normal Map']
            mat.node_tree.nodes.remove(node_to_delete)