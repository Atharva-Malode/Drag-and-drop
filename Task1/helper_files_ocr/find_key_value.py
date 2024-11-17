def find_key_value_pairs(ocr_result):
    """
    Find key-value pairs (text containing colons)
    """
    pairs = {}
    if not ocr_result:
        return pairs
    
    for box in ocr_result:
        text = box[1][0]
        if ':' in text:
            key, value = text.split(':', 1)
            pairs[key.strip()] = value.strip()
    
    return pairs