# Land-record-digitization-system
AI-powered system for digitizing, extracting, validating, and verifying land records using OCR, confidence scoring, privacy auditing, and GIS technologies.

## Current Features

### Document Upload

The backend currently supports uploading land-record documents in the following formats:

- PDF
- JPG
- JPEG
- PNG

Uploaded files are stored locally during development and are excluded from version control.

## OCR Processing

The system uses Tesseract OCR to extract text from preprocessed land-record images.

Current pipeline:

1. Document upload
2. Image preprocessing
3. OCR text extraction

The OCR implementation is located in:

`backend/ocr_engine.py`