from PIL import Image
img=Image.open(r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (1).jpg')
gray=img.convert('L')
gray.save('gray.png')
gray.show()