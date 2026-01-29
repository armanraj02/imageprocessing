import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# --- Define Your Input Image Path ---
# Replace 'path_to_your_image.jpg' with the actual path to one specific image file.
# Make sure to use the 'r' prefix for Windows paths!
input_image_path = r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (4).jpg'


# Check if the file exists
if not os.path.exists(input_image_path):
    print(f"Error: Image not found at {input_image_path}")
    print("Please update the 'input_image_path' variable with the correct file path.")
else:
    # 1. Read the image
    img = mpimg.imread(input_image_path)
    
    # 2. Get image dimensions (height, width, channels)
    h, w = img.shape[:2]
    
    # 3. Calculate the halfway points
    half_height = h // 2
    half_width = w // 2
    
    # 4. Use NumPy array slicing to extract the 4 quadrants
    # [start_row:end_row, start_column:end_column]
    quadrant_TL = img[:half_height, :half_width]       # Top-Left
    quadrant_TR = img[:half_height, half_width:]       # Top-Right
    quadrant_BL = img[half_height:, :half_width]       # Bottom-Left
    quadrant_BR = img[half_height:, half_width:]       # Bottom-Right
    
    # 5. Display the original and the four quadrants
    
    plt.figure("Original Image")
    plt.imshow(img)
    plt.title("Original")
    plt.axis('off')

    plt.figure("Top Left Quadrant")
    plt.imshow(quadrant_TL)
    plt.title("Top Left")
    plt.axis('off')

    plt.figure("Top Right Quadrant")
    plt.imshow(quadrant_TR)
    plt.title("Top Right")
    plt.axis('off')

    plt.figure("Bottom Left Quadrant")
    plt.imshow(quadrant_BL)
    plt.title("Bottom Left")
    plt.axis('off')

    plt.figure("Bottom Right Quadrant")
    plt.imshow(quadrant_BR)
    plt.title("Bottom Right")
    plt.axis('off')
    
    # Show all the pop-up windows
    plt.show()

