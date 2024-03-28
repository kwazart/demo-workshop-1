import torch
import streamlit as st
from src.model.model import load_tokenizer, load_bart_model, make_summary_text
from src.model.cloud_model import load_cloud_model, execute
from src.model.cache import new_lru_cache


# загружаем модели и токенизатор. Кешируем в Streamlit
@st.cache_resource()
def load_model():
    tokenizer = load_tokenizer()
    model = load_bart_model()
    model_cloud = load_cloud_model()
    return tokenizer, model, model_cloud


def launch_app():
    # определяем на чем будем запускать модель
    if torch.cuda.is_available():
        torch.device("cuda")
    else:
        torch.device("cpu")

    # создадим кэш с размером 1024, чтобы каждый раз не вычислять ответ
    cache = new_lru_cache(size=1024)

    st.title("Краткий пересказ текстов и ответы на вопросы")
    # получаем текст от клиента
    text = st.text_area("Введите текст")

    tokenizer, model, model_cloud = load_model()

    st.write("Краткий пересказ")

    summary_key = text
    summary = cache.get(summary_key)  # сразу попробуем достать из кэша краткое содержание

    # если нажали кнопку и в кэше нет краткого описания
    if st.button("Получить краткий пересказ") and not summary:
        summary = make_summary_text(tokenizer, model, text)  # вычислим краткое содержание
        cache.set(summary_key, summary)  # положим в кэш

    if summary:  # если есть краткое содержание - отобразим
        st.success(summary)

    question = st.text_input(label="Задайте вопрос")

    answers_key = (question, text)
    answer = cache.get(answers_key) # сразу попробуем достать из кэша ответ на вопрос

    # если нажали кнопку и в кэше нет ответа на вопрос
    if st.button(label="Получить ответ на вопрос") and not answer:
        answer = execute(model_cloud, question, text) # получим ответ на вопрос
        cache.set(answers_key, answer) # сохраним в кэш

    if answer: # если есть ответ на вопрос - отобразим
        st.success(answer)
