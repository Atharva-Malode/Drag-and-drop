import cv2
import numpy as np
from pdf2image import convert_from_path, pdfinfo_from_path


def convert_pdf_to_images(pdf_path, max_pages=2):
    """
    Convert PDF pages to images using pdf2image with better error handling.
    Limits the number of pages processed to max_pages.
    """
    images = []
    try:
        # First try to get PDF info
        try:
            pdf_info = pdfinfo_from_path(pdf_path)
            num_pages = min(int(pdf_info["Pages"]), max_pages)
        except Exception as e:
            print(f"Could not get PDF info, assuming single page: {str(e)}")
            num_pages = 1

        print(f"Converting {num_pages} page(s) from PDF...")
        
        # Convert PDF to images with specific page range
        pil_images = convert_from_path(
            pdf_path,
            dpi=300,
            fmt='png',
            first_page=1,
            last_page=num_pages,
            thread_count=1,  # Use single thread for better stability
            grayscale=False,
            size=None,
            use_pdftocairo=True  # Try pdftocairo first
        )
        
        # Convert PIL Images to CV2 format
        for pil_image in pil_images:
            # Convert PIL image to CV2 format
            opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
            images.append(opencv_image)
            
        print(f"Successfully converted {len(images)} page(s)")
        return images

    except Exception as e:
        print(f"Error in PDF conversion: {str(e)}")
        print("Attempting alternative conversion method...")
        
        try:
            # Fallback method using different parameters
            pil_images = convert_from_path(
                pdf_path,
                dpi=300,
                fmt='png',
                first_page=1,
                last_page=1,  # Try just first page
                thread_count=1,
                use_pdftocairo=False  # Try poppler direct
            )
            
            for pil_image in pil_images:
                opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
                images.append(opencv_image)
                
            print(f"Fallback method succeeded. Converted {len(images)} page(s)")
            return images
            
        except Exception as e2:
            print(f"Both conversion methods failed. Final error: {str(e2)}")
            return images