import bpy

so = bpy.context.active_object

#create bevel modifier
mod_bevel = so.modifiers.new("ItemWork Bevel", 'BEVEL')

#adjust bevel settings
mod_bevel.offset_type = 'WIDTH'
mod_bevel.width_pct = 0.04
mod_bevel.segments = 2
mod_bevel.limit_method = 'WEIGHT'

#create subsurf modifier
mod_subsurf = so.modifiers.new("ItemWork Subdiv", 'SUBSURF')

#increase sub division levels
mod_subsurf.levels = 2
mod_subsurf.render_levels = 2


