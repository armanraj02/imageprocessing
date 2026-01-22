import cv2
import glob
import os

# Define the directory path and supported image extensions
image_dir = r'c:\Users\Sahyadri\Pictures\Saved Pictures'
# Pattern to match all common image types in the directory
pattern = os.path.join(image_dir, '*.[jJpPbBtT]*') 

# Get a list of all image file paths
image_files = glob.glob(pattern)

if not image_files:
    print(f"No images found in the directory: {image_dir}")

# Loop through each image file
for file_path in image_files:
    # Read the image
    img = cv2.imread(file_path)
    
    if img is not None:
        # Display the image with its filename as the window title
        cv2.imshow(os.path.basename(file_path), img)
        
        # Wait for a key press before moving to the next image
        # You can also use cv2.waitKey(milliseconds) for automatic display duration
        cv2.waitKey(0) 
        
        # Close the current image window
        cv2.destroyAllWindows()
    else:
        print(f"Error reading image: {file_path}")

