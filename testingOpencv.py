import cv2

img = cv2.imread('logo.png')
gray = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.imshow('gray', gray)

# Wait for any key before image disappears
# '0' means infinite time
# But if we input say '250'.....then the image would disappear afer 250 milliseconds
cv2.waitKey(0)
cv2.destroyAllWindows()