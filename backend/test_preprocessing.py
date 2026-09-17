from preprocessing import preprocess_image


input_path = "test_data/sample_land_record.jpg"
output_path = "test_data/processed_land_record.jpg"


result = preprocess_image(
    input_path,
    output_path
)

print(f"Processed image saved at: {result}")