
#importinng required module
import qrcode

#provide link to which you wanted to make QR Code
img = qrcode.make('https://intellectoglobal.com/')

#and Save it
img.save('intellecto.jpg')