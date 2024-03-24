import torch
import streamlit as st
from src.model.model import load_tokenizer, load_bart_model, make_summary_text
from src.model.cloudModel import load_cloud_model, execute


def launch_app():
    # определяем на чем будем запускать модель
    if torch.cuda.is_available():
        torch.device("cuda")
    else:
        torch.device("cpu")

    st.title("Краткий пересказ текстов и ответы на вопросы")
    # получаем текст от клиента
    text = st.text_area("Введите текст")
    question = st.text_input(label="Введите вопрос", value=" ")
    text_cloud = text

    # загружаем модель и токенизатор. Кешируем в Streamlit
    @st.cache_resource()
    def load_model():
        tokenizer = load_tokenizer()
        model = load_bart_model()
        model_cloud = load_cloud_model()
        return (tokenizer, model, model_cloud)

    tokenizer, model, model_cloud = load_model()

    st.write("Краткий пересказ")

    if st.button("Применить"):
        # вывод решения на экран
        st.success(make_summary_text(tokenizer, model, text))

    if text_cloud == " " or question == " ":
        disabled = True
    else:
        disabled = False

    executed = st.button(label="Выполнить", disabled=disabled)
    if executed:
        execute(model_cloud, question, text_cloud)
