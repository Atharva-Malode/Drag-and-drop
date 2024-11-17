# OCR and Face Clustering Project

## Overview
This repository contains two distinct tasks demonstrating the use of machine learning for OCR and facial clustering.

1. **OCR (Optical Character Recognition)**  
   Extracts structured information such as titles, key-value pairs, tables, and plain text from diverse document formats (HTML, Word, scanned documents, images, and text files) using **PaddleOCR**.  
   The extracted text is classified into categories such as *Legal*, *Medical*, and *Educational* using a zero-shot classification model.

2. **Facial Clustering**  
   A K-Means clustering model is trained using **FaceNet** to group human faces into clusters based on similarity. A pre-trained model is saved in a `.pkl` file for future testing. The dataset used includes images of celebrities.

---

## Task 1: OCR Document Extraction and Classification

### Features:
- Extracted structured data includes:
  - **Title**
  - **Key-Value Pairs**
  - **Tables**
  - **Plain Text**
- **Classification**:
  - The extracted text is classified into the following categories:
    - Legal
    - Medical
    - Educational

### Video Demos:
- **OCR Task**: Demonstration of text extraction from documents:  
  [Watch OCR Demo](https://drive.google.com/file/d/1aOz6URihUtgtxNkJF5flmWDEVfa2tuCf/view?usp=drive_link)

- **Classification Task**: Demonstration of text classification into predefined categories:  
  [Watch Classification Demo](https://drive.google.com/file/d/1Th4SJ4sIj7D_pN2EYzP3PxIYJ8LY0_Vo/view?usp=drive_link)

---

## Task 2: Facial Clustering with K-Means and FaceNet

### Features:
- **Model**: K-Means clustering algorithm.
- **Embedding**: Used **FaceNet** embeddings for similarity-based clustering.
- **Dataset**: 4 celebrity face images.
- **Output**:
  - Saved the trained model in a `.pkl` file for future testing.

### Video Demo:
- **Facial Clustering Task**: Demonstration of training and testing the K-Means clustering model:  
  [Watch Facial Clustering Demo](https://drive.google.com/file/d/1wyJ3oarfdOefrPDOO05KolXafurWG5oB/view?usp=drive_link)

---


