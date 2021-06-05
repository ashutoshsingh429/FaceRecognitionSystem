import cv2
import matplotlib.pyplot as plt

# Reading an image
img = cv2.imread('logo.png')
# This converts the image back to its original color scheme (RGB)
newImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.xlabel('We can observe that the R & B channels have swapped')
plt.imshow(img)
plt.show()
plt.imshow(newImg)
plt.show()