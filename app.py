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

st.title("🐶 Dog Breed Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    processor, model, labels = get_model()
    label, is_dog = predict(img, processor, model, labels)

    if is_dog:
        st.success(f"✅ This is a dog! Breed: {label}")
    else:
        st.warning(f"❌ This does not appear to be a dog. Predicted: {label}")
