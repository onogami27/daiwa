from transformers import pipeline

nlp = pipeline("fill-mask", model="cl-tohoku/bert-base-japanese-char")

def insert_char_to_sentence(i, char, sentence): # sentenceのi文字目にcharを挿入する
    l = list(sentence)
    l.insert(i, char)
    text = "".join(l)
    return text

original_sentence = """
古河AS㈱　調達本部調達2部　左近様

いつもお世話になります

すでに当時の金型メーカーも無くなっておりますし新たに3Dデータの作成も含まれております
また金型材料費につきましても20年前と比べても高騰しておりますのでこの価格でお願いできたらと思っております

生準トライPPAP等かかる費用を別途請求する事は御座いませんのでご安心ください

起工前検討の御社設計殿との打ち合わせが必要であれば担当者様のご紹介をお願い致します


""" # 省略
thresh = 0.7 # このスコア以上の場合、句読点を挿入する
i = 0
punctuations = ["、", "。", "?"]
chars_after_mask = 100
corrected_sentence = original_sentence
while i < len(corrected_sentence):
    i += 1
    if corrected_sentence[i-1] in punctuations: continue # 句読点が連続してくることはない
    masked_text = insert_char_to_sentence(i, nlp.tokenizer.mask_token, corrected_sentence)
    
    pre_context, post_context = masked_text.split("。")[-1].split(nlp.tokenizer.mask_token)
    res = nlp(f"{pre_context}{nlp.tokenizer.mask_token}{post_context[:chars_after_mask]}")[0] # scoreが一番高い文
    if res["token_str"] not in punctuations: continue
    if res["score"] < thresh: continue

    punctuation = res["token_str"] if res["token_str"] != "?" else "。" # 今回は"？"は"。"として扱う
    corrected_sentence = insert_char_to_sentence(i, punctuation, corrected_sentence)
    
print(corrected_sentence)