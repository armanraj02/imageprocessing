from PIL import Image

img = Image.open(r'c:\Users\Sahyadri\Pictures\Saved Pictures\download.jpg')
# Rotate 90 degrees clockwise
rotated_img = img.rotate(90, expand=True) 
rotated_img.save('rotated_image.png')
rotated_img.show()
