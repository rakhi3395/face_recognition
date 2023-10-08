from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x690+0+0")
        self.root.title("face Recognition syetrm")
        
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        
        img_top = Image.open("assets/help.jpg")
        img_top = img_top.resize((1280,690),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1280,height=680)
        
        # dev_label=Label(f_lbl,text="Email : saurabh19-cs@sanskar.org",font=("times new roman",12,"bold"),bg="white")
        # dev_label.place(x=550,y=260)
        dev_label=Label(f_lbl,text="Email : rakhi19-cs@sanskar.org",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=560,y=300)
        
        
if __name__ == "__main__":
     root=Tk()
     obj=Help(root)
     root.mainloop()