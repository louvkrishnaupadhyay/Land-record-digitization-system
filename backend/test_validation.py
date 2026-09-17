from validation import validate_land_record


def print_result(title: str, result: dict):
    print(f"\n========== {title} ==========")

    print(f"Valid: {result['is_valid']}")

    print("\nErrors:")

    if result["errors"]:
        for error in result["errors"]:
            print(f"- {error}")
    else:
        print("- None")

    print("\nWarnings:")

    if result["warnings"]:
        for warning in result["warnings"]:
            print(f"- {warning}")
    else:
        print("- None")

    print("\nValidated Fields:")

    for field in result["validated_fields"]:
        print(f"- {field}")

    print("=" * 40)


# Test 1: Valid record
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

result = validate_land_record(valid_record)

print_result(
    "VALID RECORD",
    result
)


# Test 2: Missing fields
missing_record = {
    "owner_name": "Ram Kumar",
    "father_name": None,
    "village": None,
    "district": "Aizawl",
    "survey_number": "124/3",
    "area": 2.45,
    "area_unit": "hectares",
    "land_type": "Agricultural",
}

result = validate_land_record(missing_record)

print_result(
    "MISSING FIELDS",
    result
)


# Test 3: Invalid values
invalid_record = {
    "owner_name": "",
    "father_name": "Shyam Kumar",
    "village": "XYZ",
    "district": "Aizawl",
    "survey_number": "###",
    "area": -5,
    "area_unit": "unknown",
    "land_type": "Unknown",
}

result = validate_land_record(invalid_record)

print_result(
    "INVALID RECORD",
    result
)