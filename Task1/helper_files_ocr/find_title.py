def find_title(ocr_result):
    """
    Find the title from OCR results (usually at the top of the page)
    """
    if not ocr_result:
        return None
    
    top_blocks = sorted(ocr_result, key=lambda x: x[0][0][1])[:3]
    
    for block in top_blocks:
        text = block[1][0]
        if len(text) > 3:
            return text
    return None