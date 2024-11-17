from helper_files_ocr.create_output_directory import create_output_directory
from helper_function_for_file_format.convert_pdf_to_image import convert_pdf_to_images
from helper_files_ocr.save_result import save_results
from pathlib import Path
import os
import cv2

# from helper_function_for_file_format.process_word import process_word_document
from helper_function_for_file_format.processe_word_documet import process_word_document
from helper_function_for_file_format.processe_html import process_html_file
from helper_files_ocr.processe_single_image import process_single_image

# from helper_function_for_file_format.process_html import process_html_file

def process_document(file_path):
    """Process different types of documents and extract information."""
    file_path = Path(file_path)
    output_dir = create_output_directory(str(file_path))
    results_list = []

    try:
        if file_path.suffix.lower() == '.pdf':
            print(f"Processing PDF: {file_path}")
            images = convert_pdf_to_images(str(file_path))

            if not images:
                raise ValueError("No images were extracted from the PDF")
            
            print(f"Processing {len(images)} pages...")
            for i, img in enumerate(images):
                temp_path = os.path.join(output_dir, f'page_{i}.png')
                cv2.imwrite(temp_path, img)
                result = process_single_image(temp_path, output_dir)
                results_list.append(result)

        elif file_path.suffix.lower() in ['.docx', '.doc']:
            print("Processing Word document...")
            result = process_word_document(str(file_path))
            results_list.append(result)

        elif file_path.suffix.lower() == '.html':
            print("Processing HTML file...")
            try:
                html_result = process_html_file(str(file_path))
                results_list.append(html_result)
            except Exception as e:
                print(f"Error processing HTML file: {str(e)}")


        elif file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp']:
            print("Processing image file...")
            result = process_single_image(str(file_path), output_dir)
            results_list.append(result)

        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")

        # Filter out empty results
        results_list = [r for r in results_list if r]

        if not results_list:
            print("Warning: No valid results were extracted from any pages")
            return None, output_dir

        # Combine results from multiple pages/files
        combined_results = {
    'title': next((r['title'] for r in results_list if r.get('title')), ''),
    'table': [row for r in results_list for table in r.get('table', []) for row in table],  # Flatten nested lists
    'key_value_pairs': {k: v for r in results_list for k, v in r.get('key_value_pairs', {}).items()},
    'plain_text': '\n'.join(r.get('plain_text', '') for r in results_list),  # Combine plain text
}



        # Save combined results
        output_path = save_results(combined_results, output_dir)
        return combined_results, output_dir

    except FileNotFoundError as e:
        print(f"File not found error: {str(e)}")
        return None, output_dir
    except Exception as e:
        print(f"Error processing document: {str(e)}")
        return None, output_dir
