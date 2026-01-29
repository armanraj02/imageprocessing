import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os

# 1. Define your folder path (using 'r' for raw string)
folder_path = r'c:\Users\Sahyadri\Pictures\Saved Pictures'

# 2. Search for all files inside that folder
# os.path.join adds the necessary '\' and '*.*' searches for every file
search_pattern = os.path.join(folder_path, '*.*')
image_files = glob.glob(search_pattern)

# 3. Filter to ensure we only try to read actual files (not sub-folders)
image_files = [f for f in image_files if os.path.isfile(f)]

if not image_files:
    print(f"No files found in: {folder_path}")
else:
    print(f"Reading {len(image_files)} images from folder...")

    # 4. Display in a grid (e.g., 2 rows, 4 columns)
    cols = 4
    rows = (len(image_files) + cols - 1) // cols
    
    plt.figure(figsize=(16, 4 * rows))

    for i, file_path in enumerate(image_files):
        try:
            plt.subplot(rows, cols, i + 1)
            img = mpimg.imread(file_path) # Reads the file from the path
            plt.imshow(img)
            plt.title(os.path.basename(file_path), fontsize=8)
            plt.axis('off')
        except Exception as e:
            print(f"Skipping {file_path}: {e}")

    plt.tight_layout()
    plt.show()
