import re
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """
    Preprocess the text by removing special characters, tokenizing, removing stopwords, and lemmatizing.
    """
    # Step 1: Convert text to lowercase
    text = text.lower()

    # Step 2: Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Step 3: Tokenize text
    tokens = word_tokenize(text)

    # Step 4: Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Step 5: Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Rejoin tokens into a single cleaned string
    cleaned_text = ' '.join(lemmatized_tokens)
    return cleaned_text

def classify_document(file_path):
    """
    Classify the document at the given file path into Document Type, Topic/Subject, and Relevance categories.
    """
    # Load the zero-shot classification model
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    try:
        # Read the plain text from the specified file
        with open(file_path, 'r') as file:
            doc_text = file.read()
        
        # Preprocess the text
        cleaned_text = preprocess_text(doc_text)

        # Define candidate labels for classification
        type_labels = ["Invoice", "Contract", "Resume", "Research Paper"]
        topic_labels = ["Finance", "Legal", "Medical", "Education"]
        relevance_labels = ["Priority", "Sensitive", "General Information"]

        # Perform zero-shot classification
        type_result = classifier(cleaned_text, candidate_labels=type_labels, multi_label=False)
        topic_result = classifier(cleaned_text, candidate_labels=topic_labels, multi_label=False)
        relevance_result = classifier(cleaned_text, candidate_labels=relevance_labels, multi_label=False)

        # Extracting only the labels and scores
        result = {
            "Document Type": {
                "label": type_result['labels'][0],
                "score": type_result['scores'][0]
            },
            "Topic/Subject": {
                "label": topic_result['labels'][0],
                "score": topic_result['scores'][0]
            },
            "Relevance": {
                "label": relevance_result['labels'][0],
                "score": relevance_result['scores'][0]
            }
        }

        return result

    except FileNotFoundError:
        return {"Error": "The specified file path is invalid or the file does not exist."}

# Example usage:
file_path = 'ocr_output/salesinvoice2_20241117_210625/extracted_text.txt'
results = classify_document(file_path)
print(results)
