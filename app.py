import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
from ndvi_tif import calculate_ndvi_from_tif
import matplotlib.pyplot as plt
import json

# Load trained model
model = tf.keras.models.load_model("plant_disease_cnn_model.h5")

# Load class label map
with open("label_map.json") as f:
    label_map = json.load(f)
index_to_label = {v: k for k, v in label_map.items()}

st.title("🌿 Smart Crop Monitoring System")

# Section 1: Plant Disease Detection
st.header("📷 Plant Disease Detection")
img_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

if img_file:
    img = Image.open(img_file).convert("RGB").resize((128, 128))
    st.image(img, caption="Uploaded Leaf Image", use_column_width=True)

    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)
    predicted_index = int(np.argmax(pred))
    predicted_label = index_to_label[predicted_index]
    st.success(f"✅ Predicted Disease: {predicted_label}")

# Section 2: NDVI Estimation from Sentinel-2 .tif
st.header("🛰️ NDVI Estimation from Sentinel-2")

red_tif = st.file_uploader("Upload Red Band (B04) .tif", type=["tif"], key="red")
nir_tif = st.file_uploader("Upload NIR Band (B08) .tif", type=["tif"], key="nir")

if red_tif and nir_tif:
    with open("red_band.tif", "wb") as f:
        f.write(red_tif.read())
    with open("nir_band.tif", "wb") as f:
        f.write(nir_tif.read())

    ndvi_raw, ndvi_norm = calculate_ndvi_from_tif("red_band.tif", "nir_band.tif")

    st.image(ndvi_norm, caption="🌱 NDVI Heatmap", clamp=True, channels="GRAY", use_column_width=True)

    st.markdown(f"**NDVI Range:** {ndvi_raw.min():.2f} to {ndvi_raw.max():.2f}")
