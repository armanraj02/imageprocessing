import cv2
from pathlib import Path

# 1. Define folder path
image_dir = Path(r'c:\Users\Sahyadri\Pictures\Saved Pictures')
# 2. Get list of all image files (.jpg, .png, etc.)
image_files = list(image_dir.glob('*.jpg')) + list(image_dir.glob('*.png'))

for img_path in image_files:
    img = cv2.imread(str(img_path))
    if img is not None:
        # Each window MUST have a unique name to appear separately
        cv2.imshow(f"Image: {img_path.name}", img)

# Keep all windows open until you press ANY key
print("Press any key to close all windows...")
cv2.waitKey(0) 
cv2.destroyAllWindows()
