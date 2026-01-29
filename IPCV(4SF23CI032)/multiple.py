import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os

# 1. Define folder path
folder = r'C:\Users\Sahyadri\Pictures\Saved Pictures'

# 2. Get all valid image files
search_path = os.path.join(folder, '*')
all_files = glob.glob(search_path)
valid_extensions = ('.jpg', '.jpeg', '.png', '.jfif', '.bmp')
image_files = [f for f in all_files if f.lower().endswith(valid_extensions)]

if not image_files:
    print(f"No images found in: {folder}")
else:
    print(f"Found {len(image_files)} images. Opening all...")

    # 3. Loop through EVERY image (removed [:3] limit)
    for i, file_path in enumerate(image_files):
        plt.figure(f"Image {i+1}") # Creates a new window for every file
        try:
            img = mpimg.imread(file_path)
            plt.imshow(img)
            plt.title(os.path.basename(file_path))
            plt.axis('off')
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

    # 4. Display all windows at once
    plt.show()
