import cv2
def preprocess_image(image):
    """
    Preprocess the input image for better OCR results.
    Steps include grayscale conversion, noise removal, and thresholding.
    
    Parameters:
        image (numpy.ndarray): Input image in BGR format.
    
    Returns:
        numpy.ndarray: Preprocessed binary image.
    """
    try:
        # Step 1: Convert to grayscale if the image is in color
        if len(image.shape) == 3:  # Check if the image has 3 channels
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        
        # Step 2: Apply Gaussian Blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Step 3: Apply adaptive thresholding for binarization
        binary = cv2.adaptiveThreshold(
            blurred, 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 
            11, 2
        )

        # Step 4: Remove small noise using morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

        # Step 5: Denoise the image (optional but useful for OCR)
        denoised = cv2.fastNlMeansDenoising(cleaned, None, h=30)

        return denoised
    
    except Exception as e:
        raise Exception(f"Error during image preprocessing: {str(e)}")
