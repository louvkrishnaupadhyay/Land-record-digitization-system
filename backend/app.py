from fastapi import FastAPI

app = FastAPI(
    title="Land Record Digitization and Validation System",
    description="API for digitizing and validating land records.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Land Record Digitization and Validation System API",
        "status": "running",
        "version": "0.1.0"
    }