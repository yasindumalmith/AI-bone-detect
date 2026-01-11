from fastapi import APIRouter, UploadFile, File
import shutil, os

router = APIRouter()

@router.post("/upload-xray")
async def upload_xray(file: UploadFile = File(...)):
    os.makedirs("uploads/xrays", exist_ok=True)
    file_path = f"uploads/xrays/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"image_path": file_path}
