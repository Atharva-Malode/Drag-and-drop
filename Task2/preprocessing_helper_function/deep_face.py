import numpy as np
from deepface import DeepFace
def extract_deepface_features(image, model_name="Facenet"):
    """
    Extracts features using DeepFace.
    :param image: Input face image.
    :param model_name: DeepFace model to use for feature extraction (default: "Facenet").
    :return: Feature vector.
    """
    print(f"Extracting features using DeepFace ({model_name}).")
    embedding = DeepFace.represent(image, model_name=model_name, enforce_detection=False)[0]["embedding"]
    return np.array(embedding)