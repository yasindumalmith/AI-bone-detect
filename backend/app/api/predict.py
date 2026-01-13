from fastapi import APIRouter, HTTPException
from app.cnn.preprocess import preprocess_image
from app.cnn.model import model
import torch

router = APIRouter()

@router.post("/predict-fracture")
def predict(image_path: str):
    try:
        # Check if file exists to avoid downstream errors if possible, 
        # though preprocess checks it too.
        image = preprocess_image(image_path)

        with torch.no_grad():
            output = model(image)
            probability = torch.sigmoid(output).item()

        return {
            "fracture": probability > 0.5,
            "confidence": round(probability, 2)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
