import cv2
def detect_and_crop_faces(image_path, output_size=(160, 160)):
    """
    Detects frontal faces in an image and crops them.
    :param image_path: Path to the input image.
    :param output_size: Tuple indicating the size to resize the cropped face.
    :return: Cropped face image or None if no frontal face is detected.
    """
    print(f"Processing image for face detection: {image_path}")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to read image file {image_path}. Skipping this file.")
        return None
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        print(f"No faces detected in image: {image_path}")
        return None
    
    # Crop the first detected face
    x, y, w, h = faces[0]
    cropped_face = image[y:y+h, x:x+w]
    resized_face = cv2.resize(cropped_face, output_size)
    print(f"Face detected and cropped from: {image_path}")
    return resized_face