from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
import requests

# Example model - you can replace this with another model from Hugging Face
model_name = "google/vit-base-patch16-224"

# Load the processor and model
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Load an image (you can use your own image path)
url = "uncles_dog.jpg"
image = Image.open("uncles_dog.jpg")

# Preprocess image
inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

# Get predicted class
logits = outputs.logits
predicted_class_idx = logits.argmax(-1).item()

# Get class label
labels = model.config.id2label
print(f"Predicted class: {labels[predicted_class_idx]}")


#CNN MODEL :
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image

# Use a CNN model like ResNet-50
model_name = "microsoft/resnet-50"

# Load the processor and model
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Load local image
image = Image.open("dog.jpg")  # Ensure "dog.jpg" is in the same directory

# Preprocess image
inputs = processor(images=image, return_tensors="pt")

# Run inference
with torch.no_grad():
    outputs = model(**inputs)

# Get predicted class
logits = outputs.logits
predicted_class_idx = logits.argmax(-1).item()

# Get class label
labels = model.config.id2label
print(f"Predicted class: {labels[predicted_class_idx]}")