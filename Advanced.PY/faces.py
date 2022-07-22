import cv2
import sys

cascpath = "haarcascade_frontalface_default.xml" 
imgpath = "C:/Users/ELCOT/Documents/Advanced.PY/img1.jpg" 

type(imgpath)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascpath)
image = cv2.imread(imgpath,1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print (f"Found {len(faces)} faces!")

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)