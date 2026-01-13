from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil, os, uuid

router = APIRouter()

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

@router.post("/upload-xray")
async def upload_xray(file: UploadFile = File(...)):
    # Validate file extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPG and PNG allowed.")

    os.makedirs("uploads/xrays", exist_ok=True)
    
    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}{ext}"
    file_path = f"uploads/xrays/{unique_filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"image_path": file_path}
