from PIL import Image, ImageFilter

img = Image.open(r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (1).jpg')
# Apply a blur filter
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save('blurred_image.png')
blurred_img.show()
