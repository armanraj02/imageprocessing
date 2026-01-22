import cv2
import numpy as np
from pathlib import Path
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

# 1. Initialize the ResNet50 model
model = ResNet50(weights='imagenet')

# 2. Path to your folder (use '.' for the current directory)
image_folder = Path(r'c:\Users\Sahyadri\Pictures\Saved Pictures')
image_files = list(image_folder.glob('*.jpg')) + list(image_folder.glob('*.png'))

# 3. Read and Prepare all images
processed_images = []
valid_filenames = []

for img_path in image_files:
    img = cv2.imread(str(img_path))
    if img is not None:
        # Resize to 224x224 as required by ResNet50
        img_resized = cv2.resize(img, (224, 224))
        # Convert BGR (OpenCV) to RGB (Model Expectation)
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        processed_images.append(img_rgb)
        valid_filenames.append(img_path.name)

# 4. Convert list to a single 4D Batch Array: (NumImages, 224, 224, 3)
image_batch = np.array(processed_images)
image_batch = preprocess_input(image_batch)

# 5. Run recognition on the entire batch at once
predictions = model.predict(image_batch)
results = decode_predictions(predictions, top=1)

# 6. Display Results
for i, name in enumerate(valid_filenames):
    _, label, confidence = results[i][0]
    print(f"Image: {name} | Recognized as: {label} ({confidence*100:.2f}%)")
