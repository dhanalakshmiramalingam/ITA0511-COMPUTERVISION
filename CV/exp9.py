import cv2
path ="C:/Users/USER/Desktop/mycv.jpg"
src = cv2.imread(path)
image = cv2.rotate(src, cv2.ROTATE_180)
img = cv2.resize(image,(600,600))
cv2.imshow("Image", img)
cv2.waitKey(0)
