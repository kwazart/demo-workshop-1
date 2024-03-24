from transformers import pipeline


def load_cloud_model():
    model_pipeline = pipeline(
        task="question-answering", model="deepset/roberta-base-squad2"
    )
    return model_pipeline


# Функция запуска модели
def execute(cloud_model, question, text):
    result = cloud_model(question=question, context=text)
    return result["answer"]
