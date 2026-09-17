from typing import Any


REQUIRED_FIELDS = [
    "owner_name",
    "village",
    "district",
    "survey_number",
    "area",
    "area_unit",
    "land_type",
]

OPTIONAL_FIELDS = [
    "father_name",
]


def calculate_field_completeness(record: dict) -> float:
    """
    Calculate the percentage of required fields that are present.

    Returns:
        Score from 0 to 100.
    """

    if not REQUIRED_FIELDS:
        return 100.0

    completed_fields = 0

    for field in REQUIRED_FIELDS:
        value = record.get(field)

        if value is not None:
            if not isinstance(value, str) or value.strip():
                completed_fields += 1

    return (completed_fields / len(REQUIRED_FIELDS)) * 100


def calculate_optional_completeness(record: dict) -> float:
    """
    Calculate the percentage of optional fields that are present.

    Returns:
        Score from 0 to 100.
    """

    if not OPTIONAL_FIELDS:
        return 100.0

    completed_fields = 0

    for field in OPTIONAL_FIELDS:
        value = record.get(field)

        if value is not None:
            if not isinstance(value, str) or value.strip():
                completed_fields += 1

    return (completed_fields / len(OPTIONAL_FIELDS)) * 100


def calculate_validation_score(validation_result: dict) -> float:
    """
    Convert validation results into a score from 0 to 100.

    Errors reduce the score significantly.
    Warnings reduce the score slightly.
    """

    errors = validation_result.get("errors", [])
    warnings = validation_result.get("warnings", [])

    if errors:
        error_penalty = min(len(errors) * 20, 100)
    else:
        error_penalty = 0

    warning_penalty = min(len(warnings) * 5, 25)

    score = 100 - error_penalty - warning_penalty

    return max(score, 0.0)


def calculate_confidence(
    record: dict,
    validation_result: dict,
    ocr_score: float,
) -> dict:
    """
    Calculate the overall confidence score of a land record.

    Args:
        record: Structured land-record data.
        validation_result: Result from the validation engine.
        ocr_score: OCR confidence score from 0 to 100.

    Returns:
        Detailed confidence result.
    """

    if not 0 <= ocr_score <= 100:
        raise ValueError(
            "OCR score must be between 0 and 100."
        )

    completeness_score = calculate_field_completeness(
        record
    )

    optional_score = calculate_optional_completeness(
        record
    )

    validation_score = calculate_validation_score(
        validation_result
    )

    overall_score = (
        (ocr_score * 0.40)
        + (completeness_score * 0.25)
        + (validation_score * 0.25)
        + (optional_score * 0.10)
    )

    overall_score = round(
        max(0.0, min(overall_score, 100.0)),
        2
    )

    if overall_score >= 90:
        level = "HIGH"
    elif overall_score >= 70:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "overall_score": overall_score,
        "confidence_level": level,
        "components": {
            "ocr_score": round(ocr_score, 2),
            "required_field_completeness": round(
                completeness_score,
                2
            ),
            "validation_score": round(
                validation_score,
                2
            ),
            "optional_field_completeness": round(
                optional_score,
                2
            ),
        },
    }