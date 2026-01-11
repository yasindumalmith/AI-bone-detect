import torch

model = torch.load("models/fracture_cnn.pt", map_location="cpu")
model.eval()
