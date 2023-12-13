import streamlit as st
import torch
import sys
import os

# model_path необходимо установить исходя из директории откуда запусается приложение
# дефолтный запуск приложения из src "streamlit run src/ui/client.py"
model_path = os.path.abspath('src/model')
sys.path.append(model_path)

from model import load_model, get_text

# определяем на чем будем запускать модель
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

st.title('Краткий пересказ текстов')
# получаем текст от клиента
text = st.text_area('Введите текст')

# запускаем модель
load_model = st.cache_resource(load_model)
summary = load_model()

st.write('Краткий пересказ')

if st.button('Применить'):
    # вывод решения на экран
    st.success(get_text(summary, text))
