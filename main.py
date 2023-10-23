from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from  employee import employee
import os
from train import Train
from face_recognition import face_detection
from attendance import Attendance
from developer import Developer
from help import Help
from camera_open import CameraApp 
import tkinter as tk


# class face_Recognition_system:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("face Recognition system")
        
#         img = Image.open("assets/facemask1.jpg")
#         img = img.resize((500,150),Image.ANTIALIAS)
#         self.photoimg=ImageTk.PhotoImage(img)
#         f_lbl=Label(self.root,image=self.photoimg)
#         f_lbl.place(x=0,y=0,width=500,height=150)
#         img1 = Image.open("assets/face1.jpg")
#         img1 = img1.resize((150,150),Image.ANTIALIAS)
#         self.photoimg1=ImageTk.PhotoImage(img1)
#         f_lbl=Label(self.root,image=self.photoimg1)
#         f_lbl.place(x=500,y=0,width=150,height=150)
        
#         img2 = Image.open("assets/face2.jpg")
#         img2 = img2.resize((300,150),Image.ANTIALIAS)
#         self.photoimg2=ImageTk.PhotoImage(img2)
#         f_lbl=Label(self.root,image=self.photoimg2)
#         f_lbl.place(x=650,y=0,width=150,height=150)
        
#         img0 = Image.open("assets/face3.jpg")
#         img0 = img0.resize((300,150),Image.ANTIALIAS)
#         self.photoimg0=ImageTk.PhotoImage(img0)
#         f_lbl=Label(self.root,image=self.photoimg0)
#         f_lbl.place(x=800,y=0,width=150,height=150) 
        
#         img01 = Image.open("assets/face22.jpg")
#         img01= img01.resize((500,150),Image.ANTIALIAS)
#         self.photoimg01=ImageTk.PhotoImage(img01)
#         f_lbl=Label(self.root,image=self.photoimg01)
#         f_lbl.place(x=920,y=0,width=150,height=150) 
        
#         img00 = Image.open("assets/facemask.jpg")
#         img00= img00.resize((500,500),Image.ANTIALIAS)
#         self.photoimg00=ImageTk.PhotoImage(img00)
#         f_lbl=Label(self.root,image=self.photoimg00)
#         f_lbl.place(x=1050,y=0,width=500,height=150)
        
#         img3 = Image.open("assets/face6.jpg")
#         img3 = img3.resize((1530,710),Image.ANTIALIAS)
#         self.photoimg3=ImageTk.PhotoImage(img3)
#         bg_img=Label(self.root,image=self.photoimg3)
#         bg_img.place(x=0,y=150,width=1530,height=710)
        
#         title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE And MANAGEMENT  SYSTEM  SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1530,height=50)
        
#         # student button
#         img4 = Image.open("assets/students.jpg")
#         img4 = img4.resize((200,200),Image.ANTIALIAS)
#         self.photoimg4=ImageTk.PhotoImage(img4)
        
#         b1=Button(bg_img,image=self.photoimg4,command=self.employee_details,cursor="hand2")
#         b1.place(x=100,y=60,width=200,height=200)
        
#         b1_1=Button(bg_img,text="Employee details",command=self.employee_details,cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=100,y=220,width=200,height=50)
        
#         # detect face
        
#         img5 = Image.open("assets/facedetect.jpg")
#         img5 = img5.resize((200,200),Image.ANTIALIAS)
#         self.photoimg5=ImageTk.PhotoImage(img5)
#         b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
#         b1.place(x=320,y=60,width=200,height=200)
        
#         b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=320,y=220,width=200,height=50)
        
#         # attandace
        
#         img6 = Image.open("assets/attendance.jpg")
#         img6 = img6.resize((200,200),Image.ANTIALIAS)
#         self.photoimg6=ImageTk.PhotoImage(img6)
#         b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
#         b1.place(x=550,y=60,width=200,height=200)
        
#         b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=550,y=220,width=200,height=50)
        
#         # help
#         img7 = Image.open("assets/help.jpg")
#         img7 = img7.resize((200,200),Image.ANTIALIAS)
#         self.photoimg7=ImageTk.PhotoImage(img7)
#         b1=Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.help_data)
#         b1.place(x=780,y=60,width=200,height=200)
        
#         b1_1=Button(bg_img,text="HELP DESK",cursor="hand2", command=self.help_data, font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=780,y=220,width=200,height=50)
        
#         # train face
#         img8 = Image.open("assets/train.jpg")
#         img8 = img8.resize((200,200),Image.ANTIALIAS)
#         self.photoimg8=ImageTk.PhotoImage(img8)
#         b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
#         b1.place(x=100,y=300,width=200,height=200)
        
#         b1_1=Button(bg_img,text="TRAIN FACE",cursor="hand2",command=self.train_data,font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=100,y=480,width=200,height=50)
        
#         # Photo
#         img9 = Image.open("assets/pic.jpg")
#         img9 = img9.resize((200,200),Image.ANTIALIAS)
#         self.photoimg9=ImageTk.PhotoImage(img9)
#         b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
#         b1.place(x=320,y=300,width=200,height=200)
        
#         b1_1=Button(bg_img,text="PHOTO",cursor="hand2",command=self.open_img,font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=320,y=480,width=200,height=50)
        
#         # developer
#         img10 = Image.open("assets/developer.jpg")
#         img10 = img10.resize((200,200),Image.ANTIALIAS)
#         self.photoimg10=ImageTk.PhotoImage(img10)
#         b1=Button(bg_img,image=self.photoimg10,cursor="hand2", command=self.developer_data)
#         b1.place(x=550,y=300,width=200,height=200)
        
#         b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data, font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=550,y=480,width=200,height=50)
        
#         #exit
        
#         img11 = Image.open("assets/exit.jpg")
#         img11 = img11.resize((200,200),Image.ANTIALIAS)
#         self.photoimg11=ImageTk.PhotoImage(img11)
#         b1=Button(bg_img,image=self.photoimg11,cursor="hand2", command=self.iExit)
#         b1.place(x=780,y=300,width=200,height=200)
        
#         b1_1=Button(bg_img,text="EXIT",cursor="hand2", command=self.iExit, font=("times new roman",16,"bold"),bg="darkblue",fg="red")
#         b1_1.place(x=780,y=480,width=200,height=50)
        
        
#     def open_img(self):
#         os.startfile("data")
        
#     def iExit(self):
#         self.iExit=messagebox.askyesno("Face Recognition","Are you sure to EXIT",parent=self.root)
#         if self.iExit >0:
#             self.root.destroy()
#         else:
#             return
        
        
#     #fun butn
#     def employee_details(self):
#         self.new_window=Toplevel(self.root)
#         self.app=employee(self.new_window)
        
#     def train_data(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Train(self.new_window)
    
#     def face_data(self):
#         self.new_window=Toplevel(self.root)
#         self.app=face_detection(self.new_window)
        
#     def attendance_data(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Attendance(self.new_window)

#     def developer_data(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Developer(self.new_window)
        
#     def help_data(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Help(self.new_window)


            
# if __name__ == "__main__":
#      root=Tk()
#      obj=face_Recognition_system(root)
#      root.mainloop()


class face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title(" Aver solution face Recognition system")
        
    # def camera_open(self):
    #     # Implement the logic to open the camera or perform other actions
    #     print("Opening camera...")

        img3 = Image.open("assets/WelcomeFR.png")
        img3 = img3.resize((1300,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1300,height=700)
        
        title_lbl=Label(bg_img,text="FACE REGONTION SYSTEM",font=("times new roman",20,"bold",),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1300,height=20)
        
      

        #Pesonal details
        b1_1=Button(bg_img,text="Register Person",command=self.employee_details,cursor="hand2",font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=30,width=200,height=100)
        
        #train data set
        b1_1=Button(bg_img,text="Train face",cursor="hand2",command=self.train_data,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=130,width=200,height=100)
        #photo
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=230,width=200,height=100)
       
        b1_1=Button(bg_img,text="Face detector",cursor="hand2",command=self.face_data,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=330,width=200,height=100)
        
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=430,width=200,height=100)
        # camera open
        b1_1=Button(bg_img,text="Open camera",cursor="hand2",command=self.camera_open,font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=710,width=200,height=80)

        #about company
        b1_1=Button(bg_img,text="About company",cursor="hand2",command=self.developer_data, font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=530,width=200,height=100)
        
        # b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.camera_open, font=("times new roman", 16, "bold"), bg="darkblue", fg="white")

        
        b1_1=Button(bg_img,text="Help",cursor="hand2", command=self.help_data, font=("times new roman",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=630,width=200,height=85)

        # b1_2 = Button(self.root, text="Camera", cursor="hand2", command=self.camera_open_app, font=("times new roman", 16, "bold"), bg="darkblue", fg="white")
        # b1_2.place(x=0, y=530, width=200, height=100)


        copyright_label = tk.Label(root, text=" Copyright \u00A9 2023 Aver solutions group", font=("times new roman", 12),bg="white")
        copyright_label.place(x=1270, y=760)
        
        b1_1=Button(bg_img,text="EXIT",cursor="hand2", command=self.iExit, font=("times new roman",16,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=1400,y=700,width=80,height=40)
        


    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure to EXIT",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
        
    #fun butn
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=employee(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_detection(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def camera_open(self):
        self.new_window=Toplevel(self.root)
        self.app=CameraApp(self.new_window)
            
if __name__ == "__main__":
     root=Tk()
     obj=face_Recognition_system(root)
     root.mainloop()



