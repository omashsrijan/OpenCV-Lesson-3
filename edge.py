import cv2
img=cv2.imread("avatar.png")

#Setting parameter values
t_lower=50 #Lower Threshhold
t_upper=250 #Upper Threshhold

#Applying Canny Edge filter
edge=cv2.Canny(img,t_lower,t_upper)

cv2.imshow('original',img)
cv2.imshow('edge',edge)

cv2.waitKey(0)
cv2.destroyAllWindows