import os

from helper_function_for_file_format.processe_document import process_document

def main():
    # Example usage
    file_path = "test_input/cracking_the_coding_skills_-_v6.pdf"
    
    try:
        if not os.path.exists(file_path):
            print(f"Error: Input file not found at {file_path}")
            return
            
        print(f"Processing document: {file_path}")
        results, output_dir = process_document(file_path)
        
        if results:
            print("\nExtraction Preview:")
            print("Title:", results['title'])
            print("Table Rows:", len(results['table']))
            print("Key-Value Pairs:", len(results['key_value_pairs']))
            print("Plain Text Length:", len(results['plain_text']))
            print(f"\nAll results have been saved in: {output_dir}")
        else:
            print("No results were extracted from the document.")
            
    except Exception as e:
        print(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()
