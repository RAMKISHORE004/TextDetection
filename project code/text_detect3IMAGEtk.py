import pytesseract
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

def browseFiles():
    global a
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("PNG files","*.png*"),("all files","*.*")))
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    a=filename
    print(a)
def show():
    global a
    window1 = Tk()
    window1.title('My Files')
    window1.geometry("500x500")
    window1.config(background = "white")
    my_label = Label(window1,text=a)
    my_image=ImageTk.PhotoImage(Image.open(a))
    my_image_label=Label(image=my_image)
    my_label.grid(column = 1, row = 1)
    my_image_label.grid(column = 1,row = 2)
    window1.mainloop()
def work():
    print("work",a)
    #a='image.png'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img=cv2.imread(a)
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
                cv2.rectangle(img,(x,y),(w+x,h+y),(50,50,255),2)
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),2)
    print("work1",a)
    cv2.imshow("Result",img)
    cv2.waitKey(0)
    
	
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
a=""
#'image.png'
window = Tk()
window.title('File Explorer')
window.geometry("500x500")
window.config(background = "white")
label_file_explorer = Label(window,text = "File Explorer using Tkinter",width = 100, height = 4,fg = "blue")
button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_detect= Button(window,text = "Detect",command = work)
button_show= Button(window,text = "show",command = show)
button_exit = Button(window,text = "Exit",command = exit)
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_detect.grid(column = 1, row = 3)
button_show.grid(column = 1, row = 4)
button_exit.grid(column = 1,row = 5)
print("main",a)
window.mainloop()
