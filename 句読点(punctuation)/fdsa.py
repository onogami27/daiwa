import transformers

# モデルの読み込み
model = transformers.pipeline('text-classification', model='cl-tohoku/bert-base-japanese-char-whole-word-masking')


# 文章
text = "こんにちは 今日はいい天気ですね何してるの僕は嫌だ何してるの偶然だねこんなところで出会える　とは思わなかった"

# 予測

result = model(text, padding=True, )
# 句読点の挿入
punctuation = "、"
inserted_text = text + punctuation

# 結果の表示
print(inserted_text)