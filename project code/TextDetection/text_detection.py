from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
"""
import os
import cv2

#create our directory for the frames

if True:
    exit()
if not os.path.exists('image_frames1'):
    os.makedirs('image_frames1')

# create our video path
test_vid = cv2.VideoCapture('testvideo1.mp4')

# start our index or count for the frames
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
index=0
while test_vid.isOpened():
    ret,frame = test_vid.read()
    if not ret:
        break

#assign a name for our files
    name='./image_frames1/frame' + str(index) + '.png'

#assign our print statement
    print ('Extracting frames...' + name)
    cv2.imwrite(name, frame)
    demo = Image.open("image_frames1/frame" + str(index) + ".png")
    text = pytesseract.image_to_string(demo, lang = 'eng')
    print(text)
    print()
    index = index + 1
    if cv2.waitKey(10) & 0xFF == ord('a'):
        break

test_vid.release()
cv2.destroyAllWindows() # destroy all the opened windows
"""

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
demo = Image.open("image_frames/frame50.png")
text = pytesseract.image_to_string(demo, lang = 'eng')
print (text)

