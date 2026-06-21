# Model Card

# Plant Disease Detection Model

## Model Overview

This model is designed to classify plant diseases from leaf images and provide corresponding treatment recommendations.

The model uses Transfer Learning with a ResNet18 Convolutional Neural Network trained on the PlantVillage dataset.

---

## Model Details

| Property        | Value                            |
| --------------- | -------------------------------- |
| Model Name      | Plant Disease Detection Model    |
| Architecture    | ResNet18                         |
| Framework       | PyTorch                          |
| Learning Method | Transfer Learning                |
| Task            | Multi-Class Image Classification |
| Domain          | Agriculture                      |
| Input Type      | RGB Leaf Images                  |
| Output          | Disease Prediction               |

---

## Intended Use

### Primary Use Cases

* Agricultural disease identification
* Educational purposes
* Research projects
* Demonstration of AI applications in agriculture

### Intended Users

* Farmers
* Students
* Researchers
* AI/ML Practitioners
* Agricultural Technology Developers

---

## Dataset

### Dataset Name

PlantVillage Dataset

### Dataset Description

The PlantVillage dataset contains thousands of labeled images of healthy and diseased plant leaves.

The dataset is widely used as a benchmark for plant disease classification tasks.

---

## Input Requirements

### Accepted Input

* Plant leaf image
* RGB image
* Clear and focused image
* Supported image formats such as JPG and PNG

### Recommended Conditions

* Good lighting
* Minimal background clutter
* Single leaf visible
* Disease symptoms clearly visible

---

## Output

The model returns:

* Predicted disease class
* Confidence score
* Treatment recommendation

Example:

```json
{
  "prediction": "Tomato Early Blight",
  "confidence": 98.74
}
```

---

## Performance Considerations

Model performance depends on:

* Image quality
* Lighting conditions
* Similarity to training data
* Presence of visible disease symptoms

---

## Limitations

This model may perform poorly when:

* Images are blurry.
* Leaves are partially visible.
* Images contain multiple plants.
* Severe lighting variations exist.
* Diseases are not represented in the training dataset.

The system should not be used as a replacement for professional agricultural diagnosis.

---

## Ethical Considerations

This project is intended as a decision-support tool.

Predictions should be verified by agricultural experts before applying treatments that could impact crops or finances.

---

## Future Improvements

* Additional plant species.
* Larger datasets.
* Explainable AI visualizations.
* Disease severity estimation.
* Mobile deployment.
* Cloud inference services.

---

## Version Information

| Property     | Value            |
| ------------ | ---------------- |
| Version      | 1.0.0            |
| Status       | Production Ready |
| Last Updated | June 2026        |
