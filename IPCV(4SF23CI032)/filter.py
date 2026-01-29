from PIL import Image,ImageFilter
img=Image.open(r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (3).jpg')
blur=img.filter(ImageFilter.BLUR)
blur.save('blurred.png')
blur.show()