size=input("Select the size of your QR Code\n"
           "-Press 1,for A1 size\n"
           "-Press 2,for A2 size\n"
           "-Press 3,for A3 size\n "
           "-Press 4,for A4 size : ")
try:
    size=int(size)
    if size==1:
        a=59.4
        b=84.1
        
    if size==2:
        a=42
        b=59.4

    if size==3:
        a=29.7
        b=42
        
    else:
        a=21
        b=29.7

except Exception as e:
    print(f"Your input resulted in an error : {e} ")
    a=21
    b=29.7



text=input("Enter the url or txt message : ")

name=input("Enter the name of your barcode : ")
name=name+".png"

import qrcode as qr
import image #For formatting our image


qrr=qr.QRCode(version=8,#We can change version 1 to 40, more version means more kb
              error_correction=qr.constants.ERROR_CORRECT_H,#_H in this place we can write M,Q,L
              box_size=a,border=b)

qrr.add_data(text)
qrr.make(fit=True)
img=qrr.make_image(fill_color="black",back_color="white")
img.save(name) 
