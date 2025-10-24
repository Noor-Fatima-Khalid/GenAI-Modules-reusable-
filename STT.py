import os
import requests

def speech_to_text(audio_file_path):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    url = "https://api.elevenlabs.io/v1/speech-to-text"

    headers = {
        "xi-api-key": api_key
    }

    data = {
        "model_id": "scribe_v1"
    }

    with open(audio_file_path, "rb") as audio:
        files = {
            "file": audio
        }

        response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 200:
        text = response.json().get("text", "")
        print(f"Transcription: {text}")
        return text
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


from google.colab import files
uploaded = files.upload()

for fn in uploaded.keys():
    speech_to_text(fn)
