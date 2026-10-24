import os
import subprocess
import imageio_ffmpeg

work_dir = r"c:\Users\bhara\CascadeProjects\whatsapp-tracker\HouseWarmingVideo"
scenes_dir = os.path.join(work_dir, "master_scene_pngs")
audio_file = os.path.join(work_dir, "master_30s_audio.aac")
output_mp4 = os.path.join(work_dir, "Abburi_Housewarming_Invitation_Smooth_30Sec.mp4")
root_mp4 = r"c:\Users\bhara\CascadeProjects\whatsapp-tracker\Abburi_Housewarming_Invitation_30Sec.mp4"

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

scene_files = [
    "scene1_ganesha.png",
    "scene2_muhurtham.png",
    "scene3_vratam.png",
    "scene4_venue.png",
    "scene5_welcome.png"
]

clip_dur = 6.64
trans_dur = 0.8

cmd = [ffmpeg_exe, "-y"]

# Input 5 images with constant 30fps
for fn in scene_files:
    fp = os.path.join(scenes_dir, fn)
    cmd.extend(["-loop", "1", "-t", str(clip_dur), "-framerate", "30", "-i", fp])

# Input Audio
cmd.extend(["-i", audio_file])

# Filter complex for mathematically seamless crossfades with ZERO gaps
filter_parts = []
for i in range(len(scene_files)):
    filter_parts.append(f"[{i}:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,format=yuv420p[v{i}]")

offsets = [5.84, 11.68, 17.52, 23.36]

current_stream = "v0"
for idx, off in enumerate(offsets):
    next_stream = f"v{idx+1}"
    out_stream = f"x{idx+1}" if idx < len(offsets) - 1 else "xfaded"
    filter_parts.append(
        f"[{current_stream}][{next_stream}]xfade=transition=fade:duration={trans_dur}:offset={off}[{out_stream}]"
    )
    current_stream = out_stream

# Smooth fade out at the very end (29.2s to 30.0s)
filter_parts.append(f"[xfaded]fade=t=out:st=29.2:d=0.8[outv]")
filter_parts.append(f"[{len(scene_files)}:a]afade=t=out:st=28.5:d=1.5[outa]")

filter_complex_str = ";".join(filter_parts)

cmd.extend([
    "-filter_complex", filter_complex_str,
    "-map", "[outv]",
    "-map", "[outa]",
    "-t", "30.0",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "19",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    output_mp4
])

print("Executing FFmpeg seamless xfade assembly...")
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if res.returncode == 0:
    size = os.path.getsize(output_mp4)
    print(f"SUCCESS: Generated smooth video: {output_mp4}")
    print(f"File Size: {size / (1024*1024):.2f} MB ({size:,} bytes)")
    
    # Copy to root
    import shutil
    shutil.copy2(output_mp4, root_mp4)
    print(f"Copied to root: {root_mp4}")
else:
    print("FFmpeg Error:")
    print(res.stderr[-1000:])
