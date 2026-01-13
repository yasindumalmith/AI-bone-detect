import torch

try:
    model = torch.load("models/fracture_cnn.pt", map_location="cpu")
    model.eval()
    print("✅ Real model loaded successfully.")
except Exception as e:
    print(f"⚠️ Model not found or error loading: {e}")
    print("🔄 Switching to MOCK MODEL mode.")

    class MockModel:
        def __call__(self, x):
            # Simulate a forward pass: return a random tensor with shape (1, 1)
            # representing a raw logit.
            return torch.randn(1, 1)
    
    model = MockModel()
