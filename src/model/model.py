from transformers import pipeline


def load_model():
    """Загрузка предобученной модели для суммаризации текста. При использовании через Streamlit может потребоваться кеширование.

    Returns:
    Функция суммаризации - summarize (text: str) -> str.
    """

    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    summarizer = pipeline(
        "summarization", model=model_name, tokenizer=model_name)

    def summarize(text):
        summary = summarizer(text, max_length=600, min_length=50,
                             length_penalty=2.0, no_repeat_ngram_size=4)
        text = summary[0]['summary_text']
        return text

    return summarize
