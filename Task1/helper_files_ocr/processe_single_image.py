import cv2
import numpy as np
import os
from helper_files_ocr.text_from_image import extract_text_from_image
from helper_files_ocr.find_title import find_title
from helper_files_ocr.find_table import find_table
from helper_files_ocr.find_key_value import find_key_value_pairs
from helper_files_ocr.preprocesse_image import preprocess_image
from helper_files_ocr.draw_using_cv2 import draw_ocr_results
from helper_files_ocr.save_result import save_results


def process_single_image(image_path, output_dir):
    """
    Process a single image: preprocess, extract title, text, table, and annotate the image.
    
    Parameters:
        image_path (str): Path to the image file.
        output_dir (str): Directory to save output files.
    
    Returns:
        dict: Extracted information including title, table, key-value pairs, and plain text.
    """
    try:
        # Step 1: Read and preprocess the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Unable to read image from path: {image_path}")
        
        preprocessed_image = preprocess_image(image)  # From your existing code

        # Step 2: Perform OCR
        ocr_result = extract_text_from_image(preprocessed_image)  # From your existing code
        if not ocr_result:
            print(f"No text found in image: {image_path}")
            return {}

        # Step 3: Extract relevant components
        results = {
            'title': find_title(ocr_result),                # Extract title
            'table': find_table(ocr_result),                # Extract tables
            'key_value_pairs': find_key_value_pairs(ocr_result),  # Extract key-value pairs
            'plain_text': ' '.join(block[1][0] for block in ocr_result)  # Extract plain text
        }

        # Step 4: Save results using existing utilities
        os.makedirs(output_dir, exist_ok=True)
        save_results(results, output_dir)  # Uses your existing save_results function

        # Step 5: Annotate and save the image
        annotated_path = draw_ocr_results(image_path, ocr_result, output_dir)  # Uses your existing function
        print(f"Annotated image saved at: {annotated_path}")

        return results

    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        return {}