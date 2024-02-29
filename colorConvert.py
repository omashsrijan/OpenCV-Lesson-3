import cv2
img=cv2.imread("avatar.png")

#HSV color model--- H:Hue, S:Saturation, V:Value
hsvImg=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV Image", hsvImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
