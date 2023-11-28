import torch
import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
from transformers import T5Tokenizer, T5ForConditionalGeneration

st.title('Краткий пересказ текстов')
st.markdown('Выберите одну из двух моделей для пересказа')
model = st.selectbox('Выберите модель', ('BART', 'T5'))

_num_beams = 4
_no_repeat_ngram_size = 3
_length_penalty = 1
_min_length = 12
_max_length = 526
_early_stopping = True

text = st.text_area('Введите текст')

def run_model(input_text):
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   if model == "BART":
       bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-base")
       bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")
       input_text = str(input_text)
       input_text = ' '.join(input_text.split())
       input_tokenized = bart_tokenizer.encode(input_text, return_tensors='pt').to(device)
       summary_ids = bart_model.generate(input_tokenized,
                                       num_beams=_num_beams,
                                       no_repeat_ngram_size=_no_repeat_ngram_size,
                                       length_penalty=_length_penalty,
                                       min_length=_min_length,
                                       max_length=_max_length,
                                       early_stopping=_early_stopping)
       output = [bart_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
       st.write('Summary')
       st.success(output[0])
   else:
       t5_model = T5ForConditionalGeneration.from_pretrained("t5-base")
       t5_tokenizer = T5Tokenizer.from_pretrained("t5-base")
       input_text = str(input_text).replace('\n', '')
       input_text = ' '.join(input_text.split())
       input_tokenized = t5_tokenizer.encode(input_text, return_tensors="pt").to(device)
       summary_task = torch.tensor([[21603, 10]]).to(device)
       input_tokenized = torch.cat([summary_task, input_tokenized], dim=-1).to(device)
       summary_ids = t5_model.generate(input_tokenized,
                                     num_beams=_num_beams,
                                     no_repeat_ngram_size=_no_repeat_ngram_size,
                                     length_penalty=_length_penalty,
                                     min_length=_min_length,
                                     max_length=_max_length,
                                     early_stopping=_early_stopping)
       output = [t5_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
       st.write('Краткий пересказ')
       st.success(output[0])

if st.button('За работу'):
   run_model(text)
