import bpy

so = bpy.context.active_object

#create subsurf modifier
mod_datatransfer = so.modifiers.new("DataTransfer Setup", 'DATA_TRANSFER')


#adjust data transfer settings
mod_datatransfer.use_vert_data = True
mod_datatransfer.data_types_verts = {'VGROUP_WEIGHTS'}
mod_datatransfer.vert_mapping = 'POLYINTERP_NEAREST'
