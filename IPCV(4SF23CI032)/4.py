import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# --- Define Your Input Image Path ---
# Replace this with the path to one specific image file on your computer.
input_image_path = r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (1).jpg'


if not os.path.exists(input_image_path):
    print(f"Error: Image not found at {input_image_path}")
else:
    # 1. Read the image and get dimensions
    img = mpimg.imread(input_image_path)
    h, w = img.shape[:2]
    half_height, half_width = h // 2, w // 2
    
    # 2. Extract quadrants
    quadrant_TL = img[:half_height, :half_width]
    quadrant_TR = img[:half_height, half_width:]
    quadrant_BL = img[half_height:, :half_width]
    quadrant_BR = img[half_height:, half_width:]
    
    # 3. Create a single figure with a 3x2 grid layout
    # We use 3 rows and 2 columns for a better visual fit
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 15))
    
    # 4. Place the Original image (spanning 2 columns)
    axes[0, 0].imshow(img)
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis('off')
    # Hide the second spot in the top row since the original spans both
    axes[0, 1].axis('off') 

    # 5. Place the four quadrants in the remaining 2 rows
    axes[1, 0].imshow(quadrant_TL)
    axes[1, 0].set_title("Top-Left Quadrant")
    axes[1, 0].axis('off')

    axes[1, 1].imshow(quadrant_TR)
    axes[1, 1].set_title("Top-Right Quadrant")
    axes[1, 1].axis('off')

    axes[2, 0].imshow(quadrant_BL)
    axes[2, 0].set_title("Bottom-Left Quadrant")
    axes[2, 0].axis('off')

    axes[2, 1].imshow(quadrant_BR)
    axes[2, 1].set_title("Bottom-Right Quadrant")
    axes[2, 1].axis('off')
    
    # 6. Adjust layout and display the single window
    plt.tight_layout()
    plt.show()
