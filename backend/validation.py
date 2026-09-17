import re


REQUIRED_FIELDS = [
    "owner_name",
    "village",
    "district",
    "survey_number",
    "area",
    "area_unit",
    "land_type",
]


SUPPORTED_AREA_UNITS = {
    "acre",
    "acres",
    "hectare",
    "hectares",
    "sq ft",
    "sq. ft.",
    "sq m",
    "sq. m.",
}


SUPPORTED_LAND_TYPES = {
    "agricultural",
    "residential",
    "commercial",
    "forest",
    "industrial",
}


def validate_required_fields(record: dict) -> list[str]:
    """
    Check whether all required fields contain values.

    Args:
        record: Structured land-record dictionary.

    Returns:
        List of validation errors.
    """

    errors = []

    for field in REQUIRED_FIELDS:
        value = record.get(field)

        if value is None or (
            isinstance(value, str) and not value.strip()
        ):
            errors.append(
                f"{field.replace('_', ' ').title()} is missing."
            )

    return errors


def validate_owner_name(owner_name: str | None) -> list[str]:
    """
    Validate the owner name.
    """

    errors = []

    if owner_name is None:
        return errors

    if len(owner_name.strip()) < 2:
        errors.append(
            "Owner name must contain at least 2 characters."
        )

    if not re.fullmatch(
        r"[A-Za-z\s.'-]+",
        owner_name.strip()
    ):
        errors.append(
            "Owner name contains invalid characters."
        )

    return errors


def validate_survey_number(survey_number: str | None) -> list[str]:
    """
    Validate the survey number format.
    """

    errors = []

    if survey_number is None:
        return errors

    pattern = r"^[A-Za-z0-9]+(?:[\/\-.][A-Za-z0-9]+)*$"

    if not re.fullmatch(pattern, survey_number.strip()):
        errors.append(
            "Survey number has an invalid format."
        )

    return errors


def validate_area(area) -> list[str]:
    """
    Validate land area.
    """

    errors = []

    if area is None:
        return errors

    if not isinstance(area, (int, float)):
        errors.append(
            "Area must be a numeric value."
        )
        return errors

    if area <= 0:
        errors.append(
            "Area must be greater than zero."
        )

    return errors


def validate_area_unit(area_unit: str | None) -> list[str]:
    """
    Validate the area unit.
    """

    errors = []

    if area_unit is None:
        return errors

    normalized_unit = area_unit.strip().lower()

    if normalized_unit not in SUPPORTED_AREA_UNITS:
        errors.append(
            f"Unsupported area unit: {area_unit}."
        )

    return errors


def validate_land_type(land_type: str | None) -> list[str]:
    """
    Validate land type.
    """

    errors = []

    if land_type is None:
        return errors

    normalized_type = land_type.strip().lower()

    if normalized_type not in SUPPORTED_LAND_TYPES:
        errors.append(
            f"Unsupported land type: {land_type}."
        )

    return errors


def validate_land_record(record: dict) -> dict:
    """
    Validate a structured land record.

    Args:
        record: Structured land-record dictionary.

    Returns:
        Validation result containing status, errors,
        warnings, and validated fields.
    """

    errors = []
    warnings = []
    validated_fields = []

    # Required fields
    required_errors = validate_required_fields(record)
    errors.extend(required_errors)

    # Owner name
    owner_errors = validate_owner_name(
        record.get("owner_name")
    )

    if owner_errors:
        errors.extend(owner_errors)
    elif record.get("owner_name") is not None:
        validated_fields.append("owner_name")

    # Survey number
    survey_errors = validate_survey_number(
        record.get("survey_number")
    )

    if survey_errors:
        errors.extend(survey_errors)
    elif record.get("survey_number") is not None:
        validated_fields.append("survey_number")

    # Area
    area_errors = validate_area(
        record.get("area")
    )

    if area_errors:
        errors.extend(area_errors)
    elif record.get("area") is not None:
        validated_fields.append("area")

    # Area unit
    unit_errors = validate_area_unit(
        record.get("area_unit")
    )

    if unit_errors:
        errors.extend(unit_errors)
    elif record.get("area_unit") is not None:
        validated_fields.append("area_unit")

    # Land type
    land_type_errors = validate_land_type(
        record.get("land_type")
    )

    if land_type_errors:
        errors.extend(land_type_errors)
    elif record.get("land_type") is not None:
        validated_fields.append("land_type")

    # Simple optional-field warnings
    if record.get("father_name") is None:
        warnings.append(
            "Father name was not provided."
        )

    if record.get("owner_name") is not None:
        validated_fields.append("owner_name")

    if record.get("village") is not None:
        validated_fields.append("village")

    if record.get("district") is not None:
        validated_fields.append("district")

    # Remove duplicates while preserving order
    validated_fields = list(dict.fromkeys(validated_fields))

    return {
        "is_valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "validated_fields": validated_fields,
    }