from transformers import pipeline
import torch
import streamlit as st

st.title('Краткий пересказ текстов')

text = st.text_area('Введите текст')

def run_model(text):
    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)
    article_text = text
    summary = summarizer(article_text, max_length=600, min_length=50, length_penalty=2.0, no_repeat_ngram_size=4)
    st.write('Краткий пересказ')
    st.success(summary[0]['summary_text'])


if st.button('Применить'):
   run_model(text)
