from ocr_engine import extract_text


image_path = "test_data/processed_land_record.jpg"

text = extract_text(image_path)

print("\n========== OCR RESULT ==========\n")
print(text)
print("\n===============================\n")