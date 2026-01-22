import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import cv2
import numpy as np

# 1. Load pre-trained model
model = ResNet50(weights='imagenet')

# 2. Load and prepare image
img = cv2.imread(r'c:\Users\Sahyadri\Pictures\Saved Pictures\images (5).jpg')
img_resized = cv2.resize(img, (224, 224))
x = np.expand_dims(img_resized, axis=0)
x = preprocess_input(x)

# 3. Predict and display
preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
