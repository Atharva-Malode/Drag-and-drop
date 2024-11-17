def get_plain_text(ocr_result):
    """
    Get all text in reading order
    """
    if not ocr_result:
        return ""
    
    sorted_blocks = sorted(ocr_result, 
                         key=lambda x: (x[0][0][1], x[0][0][0]))
    return ' '.join(block[1][0] for block in sorted_blocks)