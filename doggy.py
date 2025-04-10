from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# Load model and processor once
def load_model(model_name="microsoft/resnet-50"):
    processor = AutoImageProcessor.from_pretrained(model_name)
    model = AutoModelForImageClassification.from_pretrained(model_name)
    labels = model.config.id2label
    return processor, model, labels

# Predict label from image
def predict(image: Image.Image, processor, model, labels):
    image = image.convert("RGB")  # Ensure RGB
    inputs = processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = labels[predicted_class_idx]
    return predicted_label