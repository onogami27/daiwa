import requests
import json

headers = {
    'accept': 'application/json',
    #APIキー
    'x-gladia-key': '2400b92a-a598-495c-b206-b6ba1d6051ac',
}

params = {
    #モデル [large-v2 , medium]
    'model': 'large-v2',
}

files = {
    #読み込みファイル
    'audio': ("cris.m4a", open('cris.m4a', 'rb'), 'audio/mpeg'),
    #翻訳言語
    'language': (None, 'japanese'),
    #言語行動 [manual, automatic single language, automatic multiple languages]
    'language_behaviour': (None, 'manual'),
    #ノイズ減少機能
    'noise_reduction': (None, 'true'),
    #出力フォーマット [json, srt, txt, plain]
    'output_format': (None, 'json'),
    #話者分離機能
    'toggle_diarization': (None, 'true'),
}

response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', params=params, headers=headers, files=files)



out = json.loads(response.text)

for i in out["prediction"]:
    print(i["transcription"])