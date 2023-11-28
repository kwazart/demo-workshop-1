from streamlit.testing.v1 import AppTest

def test_app():
   # Инициализация и запуск приложения
   at = AppTest.from_file("main.py").run()

   # Установка ввода и запуск приложения
   at.text_area[0].input("Какой-то текст для примера").run()

   # Проверка результата
   assert at.success[0].value == "Ожидаемый результат выводимого текста"
