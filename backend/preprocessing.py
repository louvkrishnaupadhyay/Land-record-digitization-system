from pathlib import Path

import cv2


def preprocess_image(input_path: str, output_path: str) -> str:
    """
    Preprocess a land-record image for OCR.

    Processing steps:
    1. Read image
    2. Convert to grayscale
    3. Remove noise
    4. Apply adaptive thresholding
    5. Save processed image

    Args:
        input_path: Path to the original image.
        output_path: Path where the processed image will be saved.

    Returns:
        Path of the processed image.

    Raises:
        FileNotFoundError: If the input image does not exist.
        ValueError: If OpenCV cannot read the image.
    """

    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(
            f"Input image not found: {input_path}"
        )

    image = cv2.imread(str(input_file))

    if image is None:
        raise ValueError(
            f"Unable to read image: {input_path}"
        )

    # Step 1: Convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Remove small noise
    denoised = cv2.GaussianBlur(
        grayscale,
        (5, 5),
        0
    )

    # Step 3: Convert to black and white
    thresholded = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Make sure the output directory exists
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save processed image
    success = cv2.imwrite(
        str(output_file),
        thresholded
    )

    if not success:
        raise ValueError(
            f"Unable to save processed image: {output_path}"
        )

    return str(output_file)