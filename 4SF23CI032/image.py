import cv2

# Specify the path to your image file
image_path = r'c:\Users\Sahyadri\Pictures\Saved Pictures\images (5).jpg' 
img = cv2.imread(image_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to read. Check the path.")
else:
    cv2.imshow('Image Display', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
