import pywhatkit as kit
import cv2
import email

kit.text_to_handwritting('Hey There Im Vignesh here !')
save_to ='handwritting.png'

img = cv2.imread('handwritting.png')
cv2.imshow('Text to Handwritting',img)
cv2.waitkey(0)
cv2.destroyAllWindows()