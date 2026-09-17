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

## Structured Data Extraction

The OCR output is converted into structured land-record fields using a rule-based extraction engine.

Currently supported fields:

- Owner name
- Father's name
- Village
- District
- Survey number
- Area
- Area unit
- Land type

Implementation:

`backend/extraction.py`

## Land Record Validation

The system validates structured land-record data after OCR extraction.

Current validation checks include:

- Required field validation
- Owner name validation
- Survey number format validation
- Land area validation
- Area unit validation
- Land type validation

Validation results distinguish between:

- Errors
- Warnings
- Successfully validated fields

Implementation:

`backend/validation.py`

## Confidence Scoring

The system calculates an explainable confidence score using multiple signals:

- OCR confidence
- Required-field completeness
- Validation score
- Optional-field completeness

The overall score is mapped to:

- HIGH: 90–100
- MEDIUM: 70–89
- LOW: below 70

The confidence calculation is implemented in:

`backend/confidence.py`