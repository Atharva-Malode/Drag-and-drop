import os
import streamlit as st
from helper_function_for_file_format.processe_document import process_document

def main():
    # Streamlit App Title
    st.title("Document Processor App")
    st.markdown("Upload a document (PDF, Word, HTML, or Image) to extract key information.")
    
    # File Upload
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx", "doc", "html", "png", "jpg", "jpeg", "tiff", "bmp"])
    
    if uploaded_file is not None:
        # Display the uploaded file name
        st.write(f"Uploaded file: {uploaded_file.name}")
        
        # Save the uploaded file temporarily
        temp_file_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # Process the uploaded file
        try:
            # Update the processing message
            st.info("CPU executions are slower; processing on CPU might take some time...")
            results, output_dir = process_document(temp_file_path)
            
            if results:
                st.success("Document processed successfully!")
                
                # Display extracted results using dropdowns
                st.subheader("Extraction Results")
                
                with st.expander("Title"):
                    st.write(results.get("title", "No title found"))
                
                with st.expander("Extracted Table"):
                    if results.get("table"):
                        for i, row in enumerate(results["table"]):
                            st.write(f"Row {i+1}: {row}")
                    else:
                        st.write("No tables found.")
                
                with st.expander("Key-Value Pairs"):
                    if results.get("key_value_pairs"):
                        for key, value in results["key_value_pairs"].items():
                            st.write(f"{key}: {value}")
                    else:
                        st.write("No key-value pairs found.")
                
                with st.expander("Plain Text"):
                    st.text_area("Extracted Plain Text", value=results.get("plain_text", "No plain text found"), height=300)
                
                # Display annotated image if applicable
                annotated_image_path = os.path.join(output_dir, "annotated_result.jpg")
                if os.path.exists(annotated_image_path):
                    st.subheader("Annotated Image")
                    st.image(annotated_image_path, caption="Annotated Result", use_container_width=True)
                else:
                    st.write("No annotated image available.")
                
                # Output directory path
                st.write(f"Results saved in: {output_dir}")
            
            else:
                st.error("No results were extracted from the document.")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        # Cleanup the temporary file
        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

if __name__ == "__main__":
    main()
