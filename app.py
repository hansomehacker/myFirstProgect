import streamlit as st
import numpy as np
import PIL import Image
import joblib
import requests
import io

st.set_page_config(page_title="Handwritten Digit Recognition", page_icon="✍️")
st.title("✍️ Handwritten Digit Recognition")
st.write("Upload a handwritten digit image and AI will try to recognize it.")
# Simple model loading with fallback
@st.cache_resource
def load_model():
  try:
    # Try to load pre-trained model
    # Using sklearn's built-in digits dataset
    from sklearn.datasets import load_digits
    from sklearn.neural network import MLPClassifier
    from sklearn.model_selection import train_test_split
    digits = load_digits()
    X = digits.images.reshape((len(digits.images), -1)) / 16.0
    y = digits.target
    X_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, random_state=42)
    model = MLPClassifier(
      hidden_layer_sizes=(100,),
      max_iter=100,
      random_state=42
    )
    model.fit(X_train, y_train)
    return model
  except Exception as e:
    st.error(f"Model loading error: {e}")
    return None
    
model = load_model()


if model is None:
  st.warning("Could not load model. Using fallback recognition.")
else:
  st.success("Model loaded successfully!")

# File uploader uploaded_file
st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
# Display the uploaded image
image
Image.open(uploaded_file)
st.image(image, caption='Uploaded Image', use_column_width=True)
