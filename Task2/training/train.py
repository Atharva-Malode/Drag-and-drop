import os
from preprocessing_helper_function.deep_face import extract_deepface_features
from preprocessing_helper_function.detect_and_crop_face import detect_and_crop_faces
import joblib
import numpy as np
from training.cluster_faces import cluster_faces
import cv2


def process_images(input_folder, output_folder, model_path=None, n_clusters=4, model_name="Facenet"):
    """
    Processes images to detect faces, extract features, and cluster them.
     param input_folder: Path to the folder containing input images.
     param output_folder: Path to save clustered images.
     param model_path: Path to save the KMeans model.
     param n_clusters: Number of clusters.
     param model_name: DeepFace model name for feature extraction.
    """
    print(f"Processing images in folder: {input_folder}")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    features = []
    face_images = []
    image_paths = []
    
    # Step 1: Detect and crop faces
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path):
            print(f"Checking file: {file_path}")
            cropped_face = detect_and_crop_faces(file_path)
            if cropped_face is not None:
                feature = extract_deepface_features(cropped_face, model_name=model_name)
                features.append(feature)
                face_images.append(cropped_face)
                image_paths.append(file_path)
    
    if len(features) == 0:
        print("No faces detected in the images.")
        return
    
    # Step 2: Cluster faces
    print("Starting clustering process.")
    features = np.array(features)
    labels, kmeans_model = cluster_faces(features, n_clusters=n_clusters)
    
    # Save the clustering model
    if model_path:
        joblib.dump(kmeans_model, model_path)
        print(f"KMeans model saved at {model_path}.")
    
    # Step 3: Save clustered images
    for i in range(n_clusters):
        cluster_folder = os.path.join(output_folder, f"cluster_{i+1}")
        os.makedirs(cluster_folder, exist_ok=True)
    
    for label, img, path in zip(labels, face_images, image_paths):
        file_name = os.path.basename(path)
        cluster_path = os.path.join(output_folder, f"cluster_{label+1}", file_name)
        cv2.imwrite(cluster_path, img)
        print(f"Saved image {file_name} to {cluster_path}")
    
    print(f"Clustering completed. Images are saved in {output_folder}.")