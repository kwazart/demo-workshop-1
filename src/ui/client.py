import torch
import streamlit as st
from src.model.model import load_tokenizer_and_model, get_text

def client():
    # определяем на чем будем запускать модель
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    st.title('Краткий пересказ текстов')
    # получаем текст от клиента
    text = st.text_area('Введите текст')

    # загружаем модель и токенизатор. Кешируем в Streamlit
    @st.cache_resource()
    def load_model():
        tokenizer, model = load_tokenizer_and_model()
        return (tokenizer, model)

    tokenizer, model = load_model()

    st.write('Краткий пересказ')

    if st.button('Применить'):
        # вывод решения на экран
        st.success(get_text(tokenizer, model, text))
