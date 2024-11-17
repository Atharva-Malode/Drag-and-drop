import cv2
import numpy as np
import os
def draw_ocr_results(image_path, ocr_result, output_dir):
    """
    Draw bounding boxes and text annotations on the image
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read image")
    
    # Create a copy for drawing
    vis_image = image.copy()
    
    # Define colors and font
    box_color = (0, 255, 0)  # Green for boxes
    text_color = (255, 0, 0)  # Blue for text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    thickness = 2
    
    # Draw boxes and text for each detection
    for box in ocr_result:
        # Get coordinates and text
        coords = np.array(box[0]).astype(np.int32)
        text = box[1][0]
        confidence = box[1][1]
        
        # Draw bounding box
        cv2.polylines(vis_image, [coords], True, box_color, thickness)
        
        # Add text with confidence
        text_with_conf = f"{text} ({confidence:.2f})"
        
        # Calculate text position (above the box)
        text_x = int(coords[0][0])
        text_y = int(coords[0][1] - 10)
        
        # Add white background to text
        (text_width, text_height), _ = cv2.getTextSize(text_with_conf, font, font_scale, thickness)
        cv2.rectangle(vis_image, 
                     (text_x, text_y - text_height), 
                     (text_x + text_width, text_y + 5), 
                     (255, 255, 255), 
                     -1)
        
        # Draw text
        cv2.putText(vis_image, text_with_conf, 
                    (text_x, text_y), 
                    font, font_scale, text_color, thickness)
    
    # Save the visualized image
    output_path = os.path.join(output_dir, "annotated_result.jpg")
    cv2.imwrite(output_path, vis_image)
    
    return output_path