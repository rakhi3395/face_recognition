from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("face Recognition syetrm")
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        
        img_top = Image.open("assets/att.jpg")
        img_top = img_top.resize((1280,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1280,height=700)
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=700,height=700)
        
        img_top1 = Image.open("assets/rakhi.jpg")
        img_top1 = img_top1.resize((300,300),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=200,y=0,width=300,height=300)
        
        
        
        dev_label=Label(main_frame,text="Hello,",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=10,y=250)
        dev_label=Label(main_frame,text="This project was developed under the guidance of Mrs.vaishali tyagi,",font=("times new roman",11,"bold"),bg="white")
        dev_label.place(x=10,y=280)
        dev_label=Label(main_frame,text="who provided invaluable expertise and support throughout the",font=("times new roman",11,"bold"),bg="white")
        dev_label.place(x=10,y=310)
        dev_label=Label(main_frame,text="development process. Asst. Prof. VAISHALI TYAGI's guidance",font=("times new roman",11,"bold"),bg="white")
        dev_label.place(x=10,y=340)
        dev_label=Label(main_frame,text="was instrumental in ensuring that the project was completed on",font=("times new roman",11,"bold"),bg="white")
        dev_label.place(x=10,y=370)
        dev_label=Label(main_frame,text="time and to a high standard",font=("times new roman",11,"bold"),bg="white")
        dev_label.place(x=10,y=400)
        dev_label=Label(main_frame,text="TEAM:- RAKHI",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=10,y=430)
        
        
        
if __name__ == "__main__":
     root=Tk()
     obj=Developer(root)
     root.mainloop()