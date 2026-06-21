from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io
import os

app = FastAPI(title="Plant Disease Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

data_dir = '../data/raw/PlantVillage'
class_names = sorted(os.listdir(data_dir))
num_classes = len(class_names)

disease_info = {
    "Pepper__bell___Bacterial_spot": "Use copper-based bactericides. Ensure good air circulation and avoid overhead watering.",
    "Pepper__bell___healthy": "Your pepper plant looks perfectly healthy! Keep up the good work.",
    "Potato___Early_blight": "Remove infected leaves. Apply a copper-based fungicide. Practice crop rotation.",
    "Potato___healthy": "Your potato plant is healthy. Maintain proper watering and fertilization.",
    "Potato___Late_blight": "Apply fungicides containing chlorothalonil or copper. Destroy severely infected plants.",
    "Tomato_Target_Spot": "Remove old leaves to improve airflow. Apply fungicides if the infection is severe.",
    "Tomato_Tomato_mosaic_virus": "No cure exists. Remove and destroy infected plants immediately. Wash hands and tools.",
    "Tomato_Tomato_YellowLeaf__Curl_Virus": "Control whitefly populations (the primary vector). Use insecticidal soaps.",
    "Tomato_Bacterial_spot": "Apply copper fungicides. Avoid working with plants when they are wet.",
    "Tomato_Early_blight": "Prune lower leaves, mulch around the base, and apply appropriate fungicides.",
    "Tomato_healthy": "This tomato plant is thriving! Maintain consistent watering.",
    "Tomato_Late_blight": "Apply preventative fungicides. Avoid overhead watering and keep foliage dry.",
    "Tomato_Leaf_Mold": "Improve air circulation, prune crowded branches, and reduce humidity.",
    "Tomato_Septoria_leaf_spot": "Remove diseased leaves. Mulch the base of the plant to prevent soil splash.",
    "Tomato_Spider_mites_Two_spotted_spider_mite": "Spray with water to dislodge mites, or use neem oil and insecticidal soap."
}

model = models.resnet18(weights=None)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, num_classes)

model_path = 'plant_disease_model.pth'
if os.path.exists(model_path):
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    print("Model loaded successfully!")

inference_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    
    input_tensor = inference_transforms(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        confidence, predicted_idx = torch.max(probabilities, 0)
        
    predicted_class = class_names[predicted_idx.item()]
    
    treatment_advice = disease_info.get(predicted_class, "Consult a local agricultural extension for specific treatments.")
    
    return {
        "disease": predicted_class,
        "confidence": round(confidence.item() * 100, 2),
        "treatment": treatment_advice 
    }

@app.get("/")
def read_root():
    return {"message": "Plant Disease API is running!"}