import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape) #(462, 623, 3) (height,width,no of channels(BGR))
imgResize = cv2.resize(img,(300,200))

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Crop",imgCropped)
cv2.waitKey(0)