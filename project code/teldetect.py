import pytesseract
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

a=pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
imgi=Image.open("immggtel.png")
boxes = pytesseract.image_to_string(imgi,lang='tel',config=a)
text=boxes.replace(" ","   ")
#print(text)
for t,b in enumerate(boxes.splitlines()):
    if t!=-1:
        #print(b)
        b=b.split()
        print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            print(b[11])
            cv2.rectangle(img,(x,y),(w+x,h+y),(50,50,255),2)
            fontpath = "Gidugu.ttf"
            font = ImageFont.truetype(fontpath, 12)
            img_pil = Image.fromarray(imgi)
            draw = ImageDraw.Draw(img_pil)
            #draw.text((x, y-5), b[11], font = font, fill = (0, 255, 255,2 ))
            #cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(img,b[1],(x,y-5),font,0.5,(0,255,255),2)

#cv2.imshow("Result",imgi)
cv2.waitKey(0)

"""

import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = np.zeros((200,400,3),np.uint8)
b,g,r,a = 0,255,0,0

## Use cv2.FONT_HERSHEY_XXX to write English.
text = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime()) 
cv2.putText(img,  text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (b,g,r), 1, cv2.LINE_AA)

## Use simsum.ttc to write Chinese.
fontpath = "Gidugu.ttf"     
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 100),  "చెట్లను   రక్షిద్దాం   జంతువుల   ఆశ్రయం", font = font, fill = (b, g, r, a))
img = np.array(img_pil)

## Display 
cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()
cv2.imwrite("res.png", img)
"""

