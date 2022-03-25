import pytesseract
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

def browseFiles():
    global a
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("PNG files","*.png*"),("all files","*.*")))
    a=filename
    print(a)
    window1 = Tk()
    window1.title('Browse')
    window1.geometry("300x200")
    window1.config(background = "white")
    label1 = Label(window1,text = "Image Selected",width = 30,height = 4,font=("Arial",20))
    label1.pack(side='left')
    window1.mainloop()
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename)
def show():
    global a
    if a=="":
        window1 = Tk()
        window1.title('Show')
        window1.geometry("300x200")
        window1.config(background = "white")
        label1 = Label(window1,text = "No Image Selected",width = 30,height = 4,font=("Arial",20))
        label1.pack(side='left')
        window1.mainloop()
    window1 = Tk()
    window1.title('Show')
    window1.geometry("300x200")
    window1.config(background = "white")
    label1 = Label(window1,text = "Continue to Detect",width = 30,height = 4,font=("Arial",20))
    label1.pack(side='left')
    imgi=Image.open(a)
    reimg=imgi.resize((500,300),Image.ANTIALIAS)
    my_image=ImageTk.PhotoImage(reimg)
    my_image_label1=Label(image=my_image).pack()
    window1.mainloop()
def work():
    print("work",a)
    #a='image.png'
    if a=="":
        window1 = Tk()
        window1.title('My Files')
        window1.geometry("300x200")
        window1.config(background = "white")
        label1 = Label(window1,text = "No Image Selected",width = 30,height = 4,font=("Arial",20))
        label1.pack(side='left')
        window1.mainloop()
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
    
def use():
    window.destroy()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
a=""
#'image.png'
window = Tk()
window.title('File Explorer')
window.geometry("700x700")
window.config(background = "orange")
"""
frame1=Frame(window)
username_l=Label(frame1,text='User Name : ',font=("Ariel",16),bg='#ff8484')
username_l.pack(side='left')
username_f=Entry(frame1,width=20,font=("Ariel",16))
username_f.pack(side='left')
frame1.pack()
waste1=Frame(window,bg='#ff8484')
lab_waste=Label(waste1,text=' ',bg='#ff8484',).pack(fill='x')
waste1.pack(fill='x')
"""
frame1=Frame(window)
label_file_explorer = Label(frame1,text = "Text Detection And Recognition in Images",bg='white',width = 80, height = 4,fg = "blue",font=("Arial bold",20))
label_file_explorer.pack(side='left')
frame1.pack()

waste1=Frame(window,bg='#ff8484')
lab_waste=Label(waste1,text=' ',bg='orange',).pack(fill='x')
waste1.pack(fill='x')

frame2=Frame(window,bg='#b5651d')
label_browse = Label(frame2,text = "Choose an Image ::",width = 30,height = 4,bg='#b5651d',font=("Arial",14))
label_browse.pack(side='left')
button_explore = Button(frame2,text = "Browse Files",command = browseFiles,font=("Arial",16))
button_explore.pack(side='left')
frame2.pack()

waste2=Frame(window,bg='#ff8484')
lab_waste1=Label(waste2,text=' ',bg='orange',).pack(fill='x')
waste2.pack(fill='x')

frame3=Frame(window)
button_detect= Button(frame3,text = "Detect",command = work,font=("Arial",16))
button_detect.pack(side='left')
labeled = Label(frame3,text = "  ",bg='orange',width = 10,height = 2,font=("Arial",14))
labeled.pack(side='left')
button_show= Button(frame3,text = "show",command = show,font=("Arial",16))
button_show.pack(side='left')
frame3.pack()

waste3=Frame(window,bg='#ff8484')
lab_waste=Label(waste3,text=' ',bg='orange',).pack(fill='x')
waste3.pack(fill='x')

frame4=Frame(window)
button_exit = Button(frame4,text = "Exit",command = use,font=("Arial",16))
button_exit.pack(side='left')
frame4.pack()

waste4=Frame(window,bg='#ff8484')
lab_waste=Label(waste4,text=' ',bg='orange',).pack(fill='x')
waste4.pack(fill='x')

print("main",a)
window.mainloop()
