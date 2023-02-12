
from transformers import pipeline
import os
import torch

#モデル実行時の警告を消す
from transformers import logging
logging.set_verbosity_warning()
logging.set_verbosity_error()

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

#テキストを読み込む前に次へor前へボタンを押した時にエラーを出す為の信号
flug = False

#cudaの認識確認

if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")

nlp = pipeline("fill-mask", model="cl-tohoku/bert-base-japanese-char-whole-word-masking",device=device,batch_size=300)

#dev = torch.cuda.is_available()
#
 #モデルの読み込み
#    nlp = pipeline("fill-mask", model="cl-tohoku/bert-base-japanese-char-whole-word-masking",device="cpu:0")
    #pipelineの引数　device= 0を指定すると→CUDA　，　-1を指定すると→CPU　を選択できる
#elif dev == True:
#    nlp = pipeline("fill-mask", model="cl-tohoku/bert-base-japanese-char-whole-word-masking",device="cuda:0")
    
    
en = nlp(f"この度はよろしくお願いいたします{nlp.tokenizer.mask_token}")
print(en)