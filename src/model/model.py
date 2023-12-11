from transformers import pipeline


def load_model():
    """Загрузка предобученной модели для суммаризации текста.

    Returns
    -------
    summarizer: Pipeline
        Функция Pipeline суммаризации текста.
    """

    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    summarizer = pipeline(
        "summarization", model=model_name, tokenizer=model_name)
    return summarizer


def get_text(summarizer, text):
    """Функция суммаризации текста.

    Parameters
    ----------
    summarizer : Pipeline
        Функция возвращаемая load_model() -> Pipeline
    text : str
        Текст для обработки моделью.

    Returns
    -------
    sum_text : str
        Суммаризированный текст.
    """

    summary = summarizer(text, max_length=600, min_length=50,
                         length_penalty=2.0, no_repeat_ngram_size=4)
    sum_text = summary[0]['summary_text']
    return sum_text
