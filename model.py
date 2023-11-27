from transformers import pipeline

model_name = "IlyaGusev/mbart_ru_sum_gazeta"
summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)

article_text = "..."  # Add txt

summary = summarizer(article_text, max_length=600, min_length=50, length_penalty=2.0, no_repeat_ngram_size=4)
print(summary[0]['summary_text'])