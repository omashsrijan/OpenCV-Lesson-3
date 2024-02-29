import cv2

img=cv2.imread("avatar.png")
cv2.imshow("Original Image",img)

#Use cvtColor() function to grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
