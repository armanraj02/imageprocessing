import cv2
image=r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (3).jpg'
img=cv2.imread(image)
if img is None:
    print('Error')
else:
    cv2.imshow('Image Display',img)
    cv2.waitKey(0)
    cv2.distroyAllindows()