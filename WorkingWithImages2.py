# Simple program to read and show an image using opecv
import cv2

img = cv2.imread('logo.png')
# To read an image in gray scale
gray = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('My Logo', img)
cv2.imshow('My Gray Logo', gray)

# waitKey species the time after which the window must be destroyed
# '0' means infinite time
# But if we input say '250'.....then the image would disappear afer 250 milliseconds
cv2.waitKey(0)
cv2.destroyAllWindows()