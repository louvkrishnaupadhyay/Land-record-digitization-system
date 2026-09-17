from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile


app = FastAPI(
    title="Land Record Digitization and Validation System",
    description="API for digitizing and validating land records.",
    version="0.2.0"
)


UPLOAD_DIR = Path("uploads")

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
}


@app.get("/")
def root():
    return {
        "message": "Land Record Digitization and Validation System API",
        "status": "running",
        "version": "0.2.0"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided."
        )

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Allowed types: PDF, JPG, JPEG, PNG."
        )

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    file_content = await file.read()

    with open(file_path, "wb") as buffer:
        buffer.write(file_content)

    return {
        "message": "Document uploaded successfully.",
        "filename": file.filename,
        "file_type": file_extension,
        "size_bytes": len(file_content)
    }