from extraction import extract_land_record


sample_text = """
Name of Owner - Ram Kumar
Father's Name: Shyam Kumar
Village: XYZ
District - Aizawl
Survey Number: 124/3
Area: 2.45 acres
Type of Land: Agricultural
"""


record = extract_land_record(sample_text)


print("\n========== EXTRACTED LAND RECORD ==========\n")

for field, value in record.items():
    print(f"{field}: {value}")

print("\n============================================\n")