from num2words import num2words
import requests
import webbrowser

def numToWords(n):
    return print("Xuat ra cach doc cua " + str(n) + " la: "+num2words(n, lang="vi"))

def vietnameseSpeech(n):
    url = 'https://api.zalo.ai/v1/tts/synthesize'
    headers = {
        'apikey': 'UGHyRpQ48nYu6va1KsrKWI5I6PQwuS2m'
    }
    text = num2words(n, lang="vi")
    data = {
        "speed": "1.0",
        "encode_type": "0",
        "speaker_id": "1",
        "input": text
    }
    response = requests.post(url, headers=headers, data=data)
    link = response.json()["data"]["url"]
    return webbrowser.open(link)






