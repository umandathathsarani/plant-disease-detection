# 🌿 Plant Disease Detection & Diagnosis System

### Enterprise-Grade Deep Learning Pipeline & Web Application

> An end-to-end Artificial Intelligence system that identifies plant diseases from leaf images and provides instant treatment recommendations using a fine-tuned ResNet18 Convolutional Neural Network (CNN), FastAPI backend, and interactive web interface.

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-success">
  <img src="https://img.shields.io/badge/Python-3.11+-blue">
  <img src="https://img.shields.io/badge/PyTorch-2.x-red">
  <img src="https://img.shields.io/badge/FastAPI-Latest-green">
  <img src="https://img.shields.io/badge/CNN-ResNet18-orange">
  <img src="https://img.shields.io/badge/Dataset-PlantVillage-brightgreen">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-yellow">
  <img src="https://img.shields.io/badge/License-MIT-purple">
</p>

---

## 📖 Overview

Plant diseases are one of the leading causes of agricultural losses worldwide. Early detection can significantly reduce crop damage and improve productivity.

This project presents a complete Deep Learning-powered Plant Disease Detection and Diagnosis System capable of classifying plant diseases from leaf images and providing actionable treatment recommendations.

The system leverages Transfer Learning using ResNet18 trained on the PlantVillage dataset, enabling accurate predictions while maintaining computational efficiency.

The project demonstrates the complete machine learning lifecycle:

* Data Exploration
* Data Preprocessing
* Model Training
* Model Evaluation
* Model Deployment
* Real-Time Inference
* Web Application Integration

---

## 📑 Table of Contents

* Overview
* Features
* Project Highlights
* Machine Learning Pipeline
* System Architecture
* Dataset
* Supported Diseases
* Technology Stack
* Project Structure
* Installation
* Running the Application
* API Documentation
* User Interface
* Model Information
* Future Improvements
* Author
* License

---

# ✨ Features

## 🔍 Disease Detection

* Upload leaf images for instant disease analysis
* Detect healthy and diseased plants
* Real-time predictions
* Confidence-based classification

## 🧠 Deep Learning Powered

* ResNet18 Convolutional Neural Network
* Transfer Learning approach
* Optimized inference performance
* High accuracy classification

## ⚡ FastAPI Backend

* Lightweight REST API
* Fast prediction response times
* Production-ready deployment architecture

## 💊 Treatment Recommendations

* Disease-specific management strategies
* Preventive actions
* Treatment suggestions

## 🎨 Interactive User Interface

* Responsive design
* Dynamic Hogwarts-themed styling
* Smooth animations
* Mobile-friendly layout

---

# 🎯 Project Highlights

### Machine Learning

✔ Transfer Learning using ResNet18

✔ Multi-class Image Classification

✔ Image Preprocessing Pipeline

✔ Data Augmentation Techniques

✔ Real-Time Inference

### Software Engineering

✔ FastAPI REST API

✔ Frontend-Backend Integration

✔ Modular Project Structure

✔ Git Version Control

✔ Production-Oriented Design

---

# 🔄 Machine Learning Pipeline

The project follows a complete end-to-end machine learning workflow.

```text
PlantVillage Dataset
        │
        ▼
Data Exploration
        │
        ▼
Data Cleaning
        │
        ▼
Data Augmentation
        │
        ▼
Image Preprocessing
        │
        ▼
Transfer Learning
(ResNet18)
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Export (.pth)
        │
        ▼
FastAPI Deployment
        │
        ▼
Real-Time Prediction
```

---

# 🏗️ System Architecture

```text
User Uploads Leaf Image
            │
            ▼
Frontend Interface
(HTML/CSS/JS)
            │
            ▼
FastAPI Backend
            │
            ▼
Image Preprocessing
            │
            ▼
ResNet18 CNN Model
            │
            ▼
Disease Prediction
            │
            ▼
Treatment Recommendation
            │
            ▼
Results Displayed
```

---

# 🌱 Dataset

The model is trained using the PlantVillage dataset, a publicly available benchmark dataset for plant disease classification.

### Dataset Characteristics

| Property      | Value                      |
| ------------- | -------------------------- |
| Dataset       | PlantVillage               |
| Task          | Multi-Class Classification |
| Input Type    | RGB Images                 |
| Domain        | Agriculture                |
| Learning Type | Supervised Learning        |
| Model         | ResNet18                   |

The dataset contains thousands of labeled plant leaf images representing healthy and diseased conditions.

---

# 🍃 Supported Plant Conditions

The model can classify multiple plant conditions including:

* Healthy Leaves
* Early Blight
* Late Blight
* Bacterial Spot
* Leaf Mold
* Septoria Leaf Spot
* Target Spot
* Mosaic Virus
* Yellow Leaf Curl Virus
* Powdery Mildew

and additional disease categories included in the training dataset.

---

# 🛠️ Technology Stack

## Machine Learning

* PyTorch
* Torchvision
* NumPy
* Pillow

## Backend

* FastAPI
* Uvicorn

## Frontend

* HTML5
* CSS3
* JavaScript

## Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 📂 Project Structure

```text
plant-disease-detection
│
├── app
│   ├── main.py
│   ├── plant_disease_model.pth
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── favicon.png
│
├── assets
│   ├── theme-hogwarts.png
│   ├── theme-gryffindor.png
│   ├── theme-slytherin.png
│   ├── theme-ravenclaw.png
│   └── theme-hufflepuff.png
│
├── data
│   └── raw
│       └── PlantVillage
│
├── notebooks
│   ├── 00_eda_visualization.ipynb
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_real_time_detection.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 📚 Notebook Workflow

## 00_eda_visualization.ipynb

* Dataset exploration
* Class distribution analysis
* Data visualization
* Sample image inspection

## 01_data_preprocessing.ipynb

* Image resizing
* Normalization
* Data augmentation
* Dataset preparation

## 02_model_training.ipynb

* Transfer learning implementation
* ResNet18 fine-tuning
* Training and validation
* Model evaluation

## 03_real_time_detection.ipynb

* Model loading
* Prediction testing
* Real-time inference validation

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/umandathathsarani/plant-disease-detection.git

cd plant-disease-detection
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## Start FastAPI Server

```bash
cd app

uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## Open Frontend

Simply open:

```text
app/index.html
```

in your web browser.

---

# 🔌 API Documentation

## POST /predict

Upload a leaf image and receive a disease prediction.

### Sample Response

```json
{
  "prediction": "Tomato Early Blight",
  "confidence": 98.74,
  "treatment": "Apply a copper-based fungicide and remove infected leaves."
}
```

---

# 🎨 User Interface

The application includes a unique Hogwarts-inspired theme system.

## 🏰 Hogwarts Theme

Default magical theme.

```html
assets/theme-hogwarts.png
```

## 🦁 Gryffindor Theme

Inspired by bravery and courage.

```html
assets/theme-gryffindor.png
```

## 🐍 Slytherin Theme

Inspired by ambition and leadership.

```html
assets/theme-slytherin.png
```

## 🦅 Ravenclaw Theme

Inspired by wisdom and creativity.

```html
assets/theme-ravenclaw.png
```

## 🦡 Hufflepuff Theme

Inspired by loyalty and hard work.

```html
assets/theme-hufflepuff.png
```

---

# 📸 Screenshots

## Hogwarts Theme

![Hogwarts Theme](assets/theme-hogwarts.png)

## Gryffindor Theme

![Gryffindor Theme](assets/theme-gryffindor.png)

## Slytherin Theme

![Slytherin Theme](assets/theme-slytherin.png)

## Ravenclaw Theme

![Ravenclaw Theme](assets/theme-ravenclaw.png)

## Hufflepuff Theme

![Hufflepuff Theme](assets/theme-hufflepuff.png)

---

# 📊 Model Information

| Property            | Value             |
| ------------------- | ----------------- |
| Architecture        | ResNet18          |
| Framework           | PyTorch           |
| Learning Method     | Transfer Learning |
| Dataset             | PlantVillage      |
| Classification Type | Multi-Class       |
| Deployment          | FastAPI           |
| Inference           | Real-Time         |

---

# 🚧 Future Improvements

* Mobile Application Development
* Cloud Deployment
* Docker Containerization
* CI/CD Integration
* Explainable AI Visualizations (Grad-CAM)
* Additional Plant Species Support
* Disease Severity Detection
* Offline Prediction Capability
* Multi-Language Support

---

# 👨‍💻 Author

## Umanda Thathsarani

Bachelor of Science (Hons) in Information Technology

Specialized in Artificial Intelligence

### Connect With Me

GitHub: https://github.com/umandathathsarani

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

---

# 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
