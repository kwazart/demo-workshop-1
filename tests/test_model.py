from src.model.model import load_tokenizer, load_bart_model,  make_summary_text
import os


tokenizer = load_tokenizer()
model = load_bart_model()


def test_load_tokenizer():
    assert tokenizer is not None


def test_load_bart_model():
    assert model is not None


def test_get_text():
    with open(os.path.join("tests", "resources", "text_1.txt"), mode='r', encoding="utf_8_sig") as f:
        text_1 = f.read()
    with open(os.path.join("tests", "resources", "text_2.txt"), mode='r', encoding="utf_8_sig") as f:
        text_2 = f.read()

    summary = make_summary_text(tokenizer, model, text_1)
    assert isinstance(summary, str)
    # Данный текст длиннее чем может обработать модель.
    # Проверка работы токенизатора урезания текста (truncation)
    summary_2 = make_summary_text(tokenizer, model, text_2)
    assert isinstance(summary_2, str)
