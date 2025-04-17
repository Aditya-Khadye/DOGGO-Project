import streamlit as st
from PIL import Image
from doggy import load_model, predict
import asyncio
import sys

if sys.platform == "darwin":
    try:
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    except Exception as e:
        print(f"Failed to set event loop policy: {e}")

# Load model once
def get_model():
    return load_model()

st.title("🐶 Dog Image Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload an image of a dog", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Load model and make prediction
    processor, model, labels = get_model()
    predicted_label = predict(image, processor, model, labels)

    st.markdown(f"### 🧠 Predicted Class: **{predicted_label}**")
