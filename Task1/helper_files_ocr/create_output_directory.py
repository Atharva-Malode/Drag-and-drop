import os
from datetime import datetime
def create_output_directory(image_path):
    """
    Create output directory based on input image name
    """
    # Get image name without extension
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    
    # Create main output directory if it doesn't exist
    main_output_dir = "ocr_output"
    os.makedirs(main_output_dir, exist_ok=True)
    
    # Create image-specific directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_output_dir = os.path.join(main_output_dir, f"{base_name}_{timestamp}")
    os.makedirs(image_output_dir, exist_ok=True)
    
    return image_output_dir