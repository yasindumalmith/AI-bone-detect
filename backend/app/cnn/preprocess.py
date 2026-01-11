import cv2
import torch

def preprocess_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = torch.tensor(img).unsqueeze(0).unsqueeze(0)
    return img
