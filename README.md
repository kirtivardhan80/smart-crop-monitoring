# 🌿 Smart Crop Monitoring Framework

## 📌 Overview

This repository contains the implementation of **Regenerative AI for Sustainable Agriculture: A Smart Crop Monitoring Framework**, which integrates **Convolutional Neural Networks (CNN)** for plant disease detection and **NDVI (Normalized Difference Vegetation Index)** for field health analysis. The framework combines **IoT data, remote sensing, and edge/cloud AI deployment** to support precision agriculture and empower smallholder farmers.

---

## 🚀 Features

✅ Real-time plant disease detection using deep learning  
✅ NDVI heatmap generation from Sentinel-2 satellite bands  
✅ Streamlit web application for easy accessibility  
✅ Modular code structure with retraining notebooks  
✅ Compatible with edge devices for offline inference

---

## 🖥️ Demo

<div align="center">
  <img src="images/disease_detection_ui.png" width="400" alt="Disease Detection UI"/>
  <br/>
  <i>Disease detection panel in the Streamlit app.</i>
</div>

<div align="center">
  <img src="images/ndvi_example.png" width="400" alt="NDVI Heatmap"/>
  <br/>
  <i>NDVI heatmap generated from Sentinel-2 Red and NIR bands.</i>
</div>

---

## 📂 Project Structure

smart-crop-monitoring/
├── README.md
├── LICENSE
├── requirements.txt
├── app.py
├── ndvi_tif.py
├── train_plant_disease_cnn.ipynb
├── plant_disease_cnn_model.h5
├── label_map.json
├── dataset_split_script.py
├── PlantVillage_Split/
│ ├── train/
│ └── val/
└── images/
├── architecture_diagram.png
├── ndvi_example.png
└── disease_detection_ui.png


- **app.py**: Streamlit application main script.  
- **ndvi_tif.py**: NDVI computation logic for GeoTIFF bands.  
- **train_plant_disease_cnn.ipynb**: Jupyter notebook to train CNN on PlantVillage dataset.  
- **plant_disease_cnn_model.h5**: Trained CNN model weights.  
- **label_map.json**: Class label mappings.  
- **dataset_split_script.py**: Script to split dataset into train and val folders.  
- **images/**: Screenshots and diagrams used in the project and documentation.

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/smart-crop-monitoring.git
cd smart-crop-monitoring

