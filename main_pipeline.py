import modules.niche_discovery as niche
import modules.script_generator as scriptgen
import modules.voiceover_generator as voice
import modules.video_creator as video
import modules.thumbnail_generator as thumb
import modules.youtube_uploader as uploader
import json
import os

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def ensure_dirs():
    os.makedirs("output/scripts", exist_ok=True)
    os.makedirs("output/audio", exist_ok=True)
    os.makedirs("output/videos", exist_ok=True)
    os.makedirs("output/thumbnails", exist_ok=True)

def main():
    ensure_dirs()
    config = load_config()

    topic = niche.get_niche(config["seed_keywords"])
    print("Topic:", topic)

    script = scriptgen.generate_script(topic, config["openai_api_key"])
    script_path = f"output/scripts/{topic}.txt"
    with open(script_path, "w") as f:
        f.write(script)

    audio_path = voice.text_to_speech(script, config["elevenlabs_api_key"])
    video_path = video.create_video(audio_path, topic)
    thumb_path = thumb.generate_thumbnail(topic)

    uploader.upload_video(
        title=topic,
        description=f"This video is about {topic}",
        video_file=video_path,
        thumbnail_file=thumb_path,
        credentials_path="credentials.json"
    )

if __name__ == "__main__":
    main()
