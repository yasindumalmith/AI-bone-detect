from fastapi import APIRouter
from app.cnn.preprocess import preprocess_image
from app.cnn.model import model

router = APIRouter()

@router.post("/predict-fracture")
def predict(image_path: str):
    image = preprocess_image(image_path)

    with torch.no_grad():
        output = model(image)
        probability = torch.sigmoid(output).item()

    return {
        "fracture": probability > 0.5,
        "confidence": round(probability, 2)
    }
