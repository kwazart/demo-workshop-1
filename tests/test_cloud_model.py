from src.model.cloud_model import load_cloud_model

model = load_cloud_model()


def test_load_cloud_model():
    assert model is not None
