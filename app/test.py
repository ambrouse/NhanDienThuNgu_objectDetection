from IPython.display import Audio
import requests
API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-vie"
headers = {"Authorization": "Bearer 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"}

def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

try:
        
    audio_bytes = query({
                "inputs": "aaaaaaaa",})
    print(audio_bytes)
    if audio_bytes == "b'Internal Server Error'":
            print("err_1")
    else:
        audio = Audio(audio_bytes)
        with open('./static/audio.mp3', 'wb') as f:
            f.write(audio.data)
except():
    print("err")