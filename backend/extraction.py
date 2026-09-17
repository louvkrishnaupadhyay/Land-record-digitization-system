import re


def extract_field(text: str, patterns: list[str]) -> str | None:
    """
    Extract a single field from OCR text using multiple patterns.

    Args:
        text: Raw OCR text.
        patterns: Regular-expression patterns for the field.

    Returns:
        Extracted value or None if the field is not found.
    """

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.MULTILINE
        )

        if match:
            return match.group(1).strip()

    return None


def extract_land_record(text: str) -> dict:
    """
    Convert OCR text into a structured land-record dictionary.

    Args:
        text: Raw text extracted from a land-record document.

    Returns:
        Dictionary containing extracted land-record fields.
    """

    owner_name = extract_field(
        text,
        [
            r"Owner\s*Name\s*[:\-]\s*(.+)",
            r"Name\s*of\s*Owner\s*[:\-]\s*(.+)",
        ]
    )

    father_name = extract_field(
        text,
        [
            r"Father\s*Name\s*[:\-]\s*(.+)",
            r"Father'?s\s*Name\s*[:\-]\s*(.+)",
        ]
    )

    village = extract_field(
        text,
        [
            r"Village\s*[:\-]\s*(.+)",
        ]
    )

    district = extract_field(
        text,
        [
            r"District\s*[:\-]\s*(.+)",
        ]
    )

    survey_number = extract_field(
        text,
        [
            r"Survey\s*(?:No|Number)\s*[:\-]\s*([A-Za-z0-9\/\-.]+)",
            r"Survey\s*[:\-]\s*([A-Za-z0-9\/\-.]+)",
        ]
    )

    area_value = extract_field(
        text,
        [
            r"Area\s*[:\-]\s*([0-9]+(?:\.[0-9]+)?)",
        ]
    )

    area_unit = extract_field(
        text,
        [
            r"Area\s*[:\-]\s*[0-9]+(?:\.[0-9]+)?\s*(hectares?|acres?|sq\.?\s*ft\.?|sq\.?\s*m(?:eters?)?)",
        ]
    )

    land_type = extract_field(
        text,
        [
            r"Land\s*Type\s*[:\-]\s*(.+)",
            r"Type\s*of\s*Land\s*[:\-]\s*(.+)",
        ]
    )

    area = None

    if area_value is not None:
        area = float(area_value)

    return {
        "owner_name": owner_name,
        "father_name": father_name,
        "village": village,
        "district": district,
        "survey_number": survey_number,
        "area": area,
        "area_unit": area_unit,
        "land_type": land_type,
    }