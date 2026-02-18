# Custom Image Classification with CNN (Project #07)

The seventh project in my **AI/ML Learning Path**. This project focuses on building a Convolutional Neural Network (CNN) from scratch to classify images into distinct categories.

## 📌 Overview
This project demonstrates the fundamental architecture of Deep Learning for Computer Vision. By manually defining layers, I explore how spatial hierarchies are learned by a model, moving from low-level edges to high-level object features.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** TensorFlow / Keras
* **Libraries:** NumPy, Matplotlib (for visualization), OpenCV
* **Architecture:** Sequential CNN

## 🏗️ Model Architecture
The model is built using the following layers:
1. **Conv2D:** Applies a set of learnable filters to the input image to create feature maps.
2. **Activation (ReLU):** Introduces non-linearity into the network.
3. **Max Pooling:** Reduces the spatial dimensions (width and height) of the feature maps, reducing computational load and preventing overfitting.
4. **Flattening:** Converts the 2D feature maps into a 1D vector.
5. **Dense (Fully Connected):** Interprets the features to perform the final classification.
6. **Softmax/Sigmoid:** Outputs the probability for each class.

## ⚙️ Training Process
- **Optimizer:** Adam / SGD (Specify which one you used)
- **Loss Function:** Categorical Crossentropy / Binary Crossentropy
- **Validation:** Monitoring loss and accuracy curves to ensure the model generalizes well to unseen data.

## 🚀 Quick Start
1. **Install Dependencies:**
   ```bash
   pip install tensorflow matplotlib numpy opencv-python
2. **Create Dataset**
3. **Run Training**
   ```bash
   python train.py
4. **Run Testing**
   ```bash
   python test.py
*Progress: From using pre-trained weights to building custom architectures.*
