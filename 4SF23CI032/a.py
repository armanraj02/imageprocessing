from PIL import Image

img = Image.open(r'c:\Users\Sahyadri\Pictures\Saved Pictures\images (4).jpg')
# Convert to grayscale
grayscale_img = img.convert('L') # 'L' mode for grayscale
grayscale_img.save('grayscale_image.png')
grayscale_img.show()
