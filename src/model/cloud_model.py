from transformers import pipeline


def load_cloud_model():
    model_pipeline = pipeline(
        "question-answering", "timpal0l/mdeberta-v3-base-squad2"
        )
    return model_pipeline


# Функция запуска модели
def execute(cloud_model, question, context):
    # Проверка на пустую строку
    if context == "":
        return "Введите текст в окно выше"
    if question == "":
        return "Введите вопрос в окно выше"
    
    result = cloud_model(question=question, context=context)
    return result["answer"]
