from src.model.model import load_tokenizer, load_bart_model,  make_summary_text

tokenizer = load_tokenizer()
model = load_bart_model()

text_1 = open("./resources/text_1.txt", "r").read()
text_2 = open("./resources/text_2.txt", "r").read()


def test_load_tokenizer():
    assert tokenizer is not None


def test_load_bart_model():
    assert model is not None


def test_get_text():
    summary = make_summary_text(tokenizer, model, text_1)
    assert isinstance(summary, str)
    # Данный текст длиннее чем может обработать модель.
    # Проверка работы токенизатора урезания текста (truncation)
    summary_2 = make_summary_text(tokenizer, model, text_2)
    assert isinstance(summary_2, str)
