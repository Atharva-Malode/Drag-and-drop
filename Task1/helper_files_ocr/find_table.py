def find_table(ocr_result):
    """
    Find table-like content based on text arrangement
    """
    if not ocr_result:
        return []
    
    rows = {}
    for box in ocr_result:
        y_coord = int(box[0][0][1])
        x_coord = box[0][0][0]
        text = box[1][0]
        
        row_found = False
        for existing_y in rows.keys():
            if abs(existing_y - y_coord) < 10:
                rows[existing_y].append((x_coord, text))
                row_found = True
                break
        
        if not row_found:
            rows[y_coord] = [(x_coord, text)]
    
    table_data = []
    for y in sorted(rows.keys()):
        row_contents = sorted(rows[y], key=lambda x: x[0])
        table_data.append([text for _, text in row_contents])
    
    return table_data