import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read the images (replace with your image paths)
img1 = mpimg.imread(r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (1).jpg')
img2 = mpimg.imread(r'c:\Users\Sahyadri\Pictures\Saved Pictures\download (2).jpg')

# Create a figure and a grid of subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2)

# Display the first image in the first subplot
axes[0].imshow(img1)
axes[0].set_title('Image 1')
axes[0].axis('off')

# Display the second image in the second subplot
axes[1].imshow(img2)
axes[1].set_title('Image 2')
axes[1].axis('off')

# Adjust layout and display the figure
plt.tight_layout()
plt.show()
