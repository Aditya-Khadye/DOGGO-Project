from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

# Load the Dog-Breed-120 model and processor
def load_model(model_name="prithivMLmods/Dog-Breed-120"):
    processor = AutoImageProcessor.from_pretrained(model_name)
    model = SiglipForImageClassification.from_pretrained(model_name)
    labels = model.config.id2label
    return processor, model, labels

# Predict dog breed
def predict(image: Image.Image, processor, model, labels):
    image = image.convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = labels[predicted_class_idx]

    # This model only predicts dog breeds, so it's always a dog
    return predicted_label, True
