import cv2
import numpy as np
import joblib
from preprocessing_helper_function.deep_face import extract_deepface_features
from preprocessing_helper_function.detect_and_crop_face import detect_and_crop_faces

def predict_cluster(image_path, kmeans_model_path, model_name="Facenet"):
    # Load KMeans model
    kmeans_model = joblib.load(kmeans_model_path)
    
    # Detect and crop face
    cropped_face = detect_and_crop_faces(image_path)
    if cropped_face is None:
        return None
    
    # Extract features using DeepFace
    features = extract_deepface_features(cropped_face, model_name=model_name)
    
    # Predict the cluster
    predicted_cluster = kmeans_model.predict([features])[0]
    return predicted_cluster

# Example usage
if __name__ == "__main__":
    input_image_path = "test_images_from_web/shahrukh.jpg"  # Path to the input image
    kmeans_model_path = "kmeans_model.pkl"  # Path to the saved KMeans model
    
    # Predict the cluster
    cluster = predict_cluster(input_image_path, kmeans_model_path)
    if cluster is not None:
        print(f"Predicted cluster for the input image: Cluster {cluster + 1}")
