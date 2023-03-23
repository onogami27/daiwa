import requests
import json

headers = {
    'accept': 'application/json',
    #APIキー
    'x-gladia-key': 'd332972b-3312-4d9f-ac8a-1c57fd6df153',
}

params = {
    #モデル [large-v2 , medium]
    'model': 'large-v2',
}

files = {
    #読み込みファイル
    'audio': ("ki_va.mp3", open('ki_va.mp3', 'rb'), 'audio/mpeg'),
    #翻訳言語
    'language': (None, 'japanese'),
    #言語行動 [manual, automatic single language, automatic multiple languages]
    'language_behaviour': (None, 'manual'),
    #ノイズ減少機能
    'noise_reduction': (None, 'false'),
    #出力フォーマット [json, srt, txt, plain]
    'output_format': (None, 'json'),
    #話者分離機能
    'toggle_diarization': (None, 'false'),
    #直訳機能
    'toggle_direct_translate': (None, 'false')
}

response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', params=params, headers=headers, files=files)



out = json.loads(response.text)
print(out)
#for i in out["prediction"]:
#    print(i["transcription"])