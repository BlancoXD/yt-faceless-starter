import requests
import uuid
import os

def text_to_speech(script_text, api_key, voice_id="EXAVITQu4vr4xnSDxMaL"):
    output_path = f"output/audio/{uuid.uuid4()}.mp3"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": script_text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return output_path
        else:
            print("Voiceover error:", response.text)
    except Exception as e:
        print("TTS Exception:", e)

    return None
