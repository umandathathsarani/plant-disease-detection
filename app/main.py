from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io
import os

app = FastAPI(title="Plant Disease Detection API")

# Allow our frontend (index.html) to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# We will read the class names dynamically from your data folder just like in the notebook
data_dir = '../data/raw/PlantVillage'
class_names = sorted(os.listdir(data_dir))
num_classes = len(class_names)

# 1. Initialize Model (We do this once when the server starts)
model = models.resnet18(weights=None)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, num_classes)

# Try to load the model (it will load the new one once your notebook finishes!)
model_path = 'plant_disease_model.pth'
if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    print("Model loaded successfully!")
else:
    print("Waiting for model to be trained...")

# 2. Define Image Transformations
inference_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# 3. Create the Prediction Endpoint
@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    # Read the uploaded image file
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    
    # Preprocess the image
    input_tensor = inference_transforms(image).unsqueeze(0).to(device)
    
    # Make prediction
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        confidence, predicted_idx = torch.max(probabilities, 0)
        
    predicted_class = class_names[predicted_idx.item()]
    
    # Return the result as JSON
    return {
        "disease": predicted_class,
        "confidence": round(confidence.item() * 100, 2)
    }

@app.get("/")
def read_root():
    return {"message": "Plant Disease API is running!"}