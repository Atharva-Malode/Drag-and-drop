

from paddleocr import PaddleOCR
from helper_files_ocr.preprocesse_image import preprocess_image
def extract_text_from_image(image_path):
    """
    Extract text from image using PaddleOCR
    """
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    processed_image = preprocess_image(image_path) 
    result = ocr.ocr(processed_image) 
    # result = ocr.ocr(image_path)
    if not result or not result[0]:
        return None
    return result[0]
