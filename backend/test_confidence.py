from confidence import calculate_confidence


# --------------------------------------------------
# Test 1: High confidence record
# --------------------------------------------------

valid_record = {
    "owner_name": "Ram Kumar",
    "father_name": "Shyam Kumar",
    "village": "XYZ",
    "district": "Aizawl",
    "survey_number": "124/3",
    "area": 2.45,
    "area_unit": "hectares",
    "land_type": "Agricultural",
}

valid_validation = {
    "is_valid": True,
    "errors": [],
    "warnings": [],
    "validated_fields": [
        "owner_name",
        "father_name",
        "village",
        "district",
        "survey_number",
        "area",
        "area_unit",
        "land_type",
    ],
}

result = calculate_confidence(
    valid_record,
    valid_validation,
    92
)

print("\n========== TEST 1 ==========")
print(result)


# --------------------------------------------------
# Test 2: Medium/low confidence record
# --------------------------------------------------

incomplete_record = {
    "owner_name": "Ram Kumar",
    "father_name": None,
    "village": None,
    "district": "Aizawl",
    "survey_number": "124/3",
    "area": 2.45,
    "area_unit": "hectares",
    "land_type": None,
}

incomplete_validation = {
    "is_valid": False,
    "errors": [
        "Village is missing.",
        "Land type is missing.",
    ],
    "warnings": [
        "Father name was not provided.",
    ],
    "validated_fields": [
        "owner_name",
        "district",
        "survey_number",
        "area",
        "area_unit",
    ],
}

result = calculate_confidence(
    incomplete_record,
    incomplete_validation,
    70
)

print("\n========== TEST 2 ==========")
print(result)


# --------------------------------------------------
# Test 3: Invalid OCR score
# --------------------------------------------------

try:
    calculate_confidence(
        valid_record,
        valid_validation,
        120
    )
except ValueError as error:
    print("\n========== TEST 3 ==========")
    print(f"Correctly rejected invalid OCR score: {error}")