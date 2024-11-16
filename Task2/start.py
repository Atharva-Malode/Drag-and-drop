from training.train import process_images


input_folder = "Dataset"  # Folder containing the images
output_folder = "clustered_faces"  # Folder to save clustered images
model_path = "kmeans_model.pkl"  # Path to save the KMeans model
model_name = "Facenet"  # DeepFace model for feature extraction

# Run the process
process_images(input_folder, output_folder, model_path, n_clusters=4, model_name=model_name)