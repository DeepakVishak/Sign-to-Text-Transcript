import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #GreyScale Image
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0) #Blured Image
imgCanny = cv2.Canny(img,100,100) #Canny Edge Detector
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #Dilation Image
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) #Eroded Image
cv2.imshow("GreyScale",imgGrey)
cv2.imshow("Blured",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilation",imgDialation)
cv2.imshow("Eroded",imgEroded)
cv2.waitKey(0)