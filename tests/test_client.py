from streamlit.testing.v1 import AppTest

# Инициализация приложения
at = AppTest.from_file("src/ui/client.py")


def test_app():
    # Запуск приложения
    at.run(timeout=100)


def test_text_area_exists():
    assert at.text_area is not None


def test_text_area_is_empty():
    assert at.text_area.len == 0


def test_button_exists():
    assert at.button is not None


def test_success_exists():
    assert at.success is not None
