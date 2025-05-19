from moviepy.editor import *
import uuid
import os

def create_video(audio_path, topic):
    output_path = f"output/videos/{uuid.uuid4()}.mp4"
    images = [f for f in os.listdir("assets") if f.endswith((".png", ".jpg", ".jpeg"))]

    if not images:
        raise Exception("No images found in /assets folder")

    image_clip = ImageClip(f"assets/{images[0]}").set_duration(AudioFileClip(audio_path).duration)
    audio_clip = AudioFileClip(audio_path)

    final = image_clip.set_audio(audio_clip)
    final.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')

    return output_path
