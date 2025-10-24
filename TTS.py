import os
import requests

def text_to_speech(text, voice_id="9J08XLaVNO9dwqz7kWR7", output_file="output.mp3"):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Saved audio as {output_file}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


text_to_speech("Hello, welcome and thank you for taking the time to meet with us. Today’s interview will focus mainly on your technical skills and problem-solving approach. But first, could you briefly walk me through your experience and current projects?")
