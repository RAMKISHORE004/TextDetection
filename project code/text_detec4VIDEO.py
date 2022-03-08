import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
fonT_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture("testvideo12.mp4")

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open video")

cntr=0
while True:
    ret,frame = cap.read()
    cntr=cntr+1
    if cntr%20==0:
        try:
            imgH,imgW,_=frame.shape
        except:
            exit()
        x1,y1,w1,h1=0,0,imgH,imgW
        imgchar = pytesseract.image_to_string(frame, lang = 'eng')

        '''
        imgboxes=pytesseract.image_to_boxes(frame, lang = 'eng')
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
            cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
            cv2.putText(frame,boxes[0],(x,imgH-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
        '''
        imgboxes=pytesseract.image_to_data(frame, lang = 'eng')
        for box,boxes in enumerate(imgboxes.splitlines()):
            if box!=0:
                boxes = boxes.split()
                if(len(boxes)==12):
                    x,y,w,h = int(boxes[6]),int(boxes[7]),int(boxes[8]),int(boxes[9])
                    cv2.rectangle(frame,(x,y),(w+x,h+y),(0,0,255),3)
                    cv2.putText(frame,boxes[11],(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
         
        
        #cv2.putText(frame,imgchar,(x1+int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        #font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.imshow("Result",frame)
        print(cv2.waitKey(2))
        print(0xFF == ord('q'))
        if(cv2.waitKey(2)and 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows()
            break
cap.release()
cv2.destroyAllWindows()
            
