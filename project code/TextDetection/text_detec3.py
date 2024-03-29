import pytesseract
import cv2
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread('image.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#plt.imshow(img)

#text = pytesseract.image_to_string(img, lang = 'eng')
#print(text)

#t1=pytesseract.image_to_boxes(img, lang = 'eng')
#print(t1)
"""
hImg,wImg,_=img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b=b.split(' ')
    #print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,255,255),2)
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
"""
hImg,wImg,_=img.shape
boxes = pytesseract.image_to_data(img)
for t,b in enumerate(boxes.splitlines()):
    if t!=0:
        #print(b)
        b=b.split()
        #print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,255),2)
            cv2.putText(img,b[11],(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
            
cv2.imshow("Result",img)
cv2.waitKey(0)
