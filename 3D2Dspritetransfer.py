import bpy
import math

output_dir = "/path/to/output/directory/"
frame_start = 1
frame_end = 250
angle_increment = 22.5

camera = bpy.data.objects['Camera']

bpy.context.scene.render.resolution_x = 128
bpy.context.scene.render.resolution_y = 128
bpy.context.scene.render.image_settings.file_format = 'PNG'

for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    for angle in range(0, 360, int(angle_increment)):
        camera.location = (5 * math.cos(math.radians(angle)), 5 * math.sin(math.radians(angle)), 2)
        camera.rotation_euler[2] = math.radians(angle)
        
        render_path = f"{output_dir}frame_{frame:04d}_angle_{angle:03d}.png"
        bpy.context.scene.render.filepath = render_path
        
        bpy.ops.render.render(write_still=True)
        
    print(f"Rendered frame {frame} at all 16 angles.")
