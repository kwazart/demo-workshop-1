from transformers import pipeline


def load_cloud_model():
    model_pipeline = pipeline(
        "question-answering", "timpal0l/mdeberta-v3-base-squad2"
        )
    return model_pipeline


# Функция запуска модели
def execute(cloud_model, question, context):
    result = cloud_model(question=question, context=context)
    return result["answer"]
