import bpy
import bmesh

bl_info = {
    "name" : "Vertex Group Viewer",             
    "author" : "dskjal",                  
    "version" : (1, 0),                  
    "blender" : (2, 80, 0),              
    "location" : "View3D > View > Vertex Weights",   
    "description" : "Vertex Group Viewer",   
    "warning" : "",
    "wiki_url" : "",                    
    "tracker_url" : "",                 
    "category" : "Mesh"                   
}

class DSKJAL_PT_VGV(bpy.types.Panel):
    bl_label = "Vertex Group Viewer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"

    @classmethod
    def poll(self, context):
        o = context.object
        return o and o.type == 'MESH' and o.mode == 'EDIT'

    def draw(self, context):
        ob = context.object

        if ob.type == 'MESH' and ob.mode == 'EDIT':
            vgs = []
            num_vg = len(ob.vertex_groups)
            bm = bmesh.from_edit_mesh(ob.data)

            vg_layer = bm.verts.layers.deform.active
            selected = [v for v in bm.verts if v.select]
            for v in selected:
                layers = [i for i in range(num_vg) if i in v[vg_layer]]
                vgs.extend(layers)

            for vg in set(vgs):
                self.layout.label(text=str(ob.vertex_groups[vg].name))

def register():
    bpy.utils.register_class(DSKJAL_PT_VGV)

def unregister():
    bpy.utils.unregister_class(DSKJAL_PT_VGV)

if __name__ == "__main__":
    register()
