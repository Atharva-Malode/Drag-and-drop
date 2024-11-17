import os
import json

def save_results(results, output_dir):
    """
    Save results to text and JSON files
    """
    # Save as text file
    txt_path = os.path.join(output_dir, "extracted_text.txt")
    with open(txt_path, 'w', encoding='utf-8') as f:
        if results['title']:
            f.write("=== DOCUMENT TITLE ===\n")
            f.write(results['title'] + "\n\n")
        
        if results['table']:
            f.write("=== TABLE CONTENT ===\n")
            for row in results['table']:
                f.write(" | ".join(row) + "\n")
            f.write("\n")
        
        if results['key_value_pairs']:
            f.write("=== KEY-VALUE PAIRS ===\n")
            for key, value in results['key_value_pairs'].items():
                f.write(f"{key}: {value}\n")
            f.write("\n")
        
        if results['plain_text']:
            f.write("=== PLAIN TEXT ===\n")
            f.write(results['plain_text'] + "\n")
    
    # Save as JSON file
    json_path = os.path.join(output_dir, "extracted_data.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    return txt_path