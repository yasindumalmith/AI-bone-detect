from fastapi import FastAPI
from app.api import upload, predict

app = FastAPI(title="Bone Fracture Detection System")

app.include_router(upload.router, prefix="/api")
app.include_router(predict.router, prefix="/api")

@app.get("/")
def health():
    return {"status": "Backend running"}
