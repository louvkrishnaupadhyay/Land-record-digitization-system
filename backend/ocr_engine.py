from pathlib import Path

import pytesseract
from PIL import Image


# Windows fallback path.
# If Tesseract is already available in PATH,
# this path is not required.
TESSERACT_PATH = Path(
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

if TESSERACT_PATH.exists():
    pytesseract.pytesseract.tesseract_cmd = str(TESSERACT_PATH)


def extract_text(image_path: str) -> str:
    """
    Extract text from an image using Tesseract OCR.

    Args:
        image_path: Path to the image that should be processed.

    Returns:
        Extracted text as a string.

    Raises:
        FileNotFoundError: If the image does not exist.
        ValueError: If the image cannot be opened.
    """

    image_file = Path(image_path)

    if not image_file.exists():
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    try:
        image = Image.open(image_file)
    except Exception as exc:
        raise ValueError(
            f"Unable to open image: {image_path}"
        ) from exc

    text = pytesseract.image_to_string(image)

    return text.strip()