from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from config import DB_PASSWORD, NO_OF_IMAGE
import time
import os
# from mtcnn import MTCNN
class employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition syetrm")
        
        #------varibale-------
        self.var_dep=StringVar() 
        # self.var_year=StringVar()        
        self.var_name=StringVar()        
        self.var_emp_id=StringVar()        
        # self.var_roll=StringVar()        
        self.var_email_id=StringVar()        
        self.var_gender=StringVar()        
        # self.var_course=StringVar() 
        self.var_phone=StringVar()          
               
        img = Image.open("assets/student1.jpg")
        img = img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        img1 = Image.open("assets/students.jpg")
        img1 = img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=550,y=0,width=500,height=150)
        
        img2 = Image.open("assets/student1.jpg")
        img2 = img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1100,y=0,width=500,height=150)
        
        # bg image
        img3 = Image.open("assets/facemask1.jpg")
        img3 = img3.resize((1500,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="skyblue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1530,height=600)
        
        # left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="employee_Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=40,y=10,width=700,height=650)
        
        img_left = Image.open("assets/st.jpg")
        img_left = img_left.resize((700,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=690,height=130)
        
        # department frame
        department_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current department information",font=("times new roman",12,"bold"))
        department_frame.place(x=5,y=130,width=690,height=110)
        
        # Department
        dep_label=Label(department_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(department_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","HR","IT","Finance","Management", "Automation")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        
        # Employee Details
        class_Student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Employee Personal information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=240,width=690,height=300)
        
        # employee id
        employeeID_label=Label(class_Student_frame,text="Employee ID:",font=("times new roman",12,"bold"))
        employeeID_label.grid(row=0,column=0,padx=10,sticky=W)
        employeeID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_emp_id,width=20,font=("times new roman",12,"bold"))
        employeeID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        # employee name
        employeeName_label=Label(class_Student_frame,text="Employee Name:",font=("times new roman",12,"bold"))
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        employeeName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # phone
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"))
        phone_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        # gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("other","Male","Female",)
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        
        # email
        email_label=Label(class_Student_frame,text="Email ID:",font=("times new roman",13,"bold"))
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email_id,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        # radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        # radiobtn2.grid(row=6,column=1)
        
        #Button
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=150,width=685,height=36)
        
        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)   
        
        update_btn=Button(btn_frame,text="UPDATE",command=self.Update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)   
        
        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)   
        
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4)   
        
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=180,width=685,height=36)
        
        take_photo_btn=Button(btn_frame1,command=self.start_camera,text="Take photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0) 
        
        update_photo_btn=Button(btn_frame1,text="Update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1) 
        
        # right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student_Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=700,height=580)
        img_Right = Image.open("assets/student.jpg")
        img_Right = img_Right.resize((700,130),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)
        f_lbl=Label(Right_frame,image=self.photoimg_Right)
        f_lbl.place(x=5,y=0,width=690,height=130)
        
        # search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=680,height=80)
        
        search_label=Label(search_frame,text="Search by:-",width=12,font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="SEARCH",width=9,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        
        showAll_btn=Button(search_frame,text="SHOW ALL",width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)
        
        # table fram
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=680,height=250)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","name","emp_id","email_id","gender","phone"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        # self.student_table.heading("course",text="Course")
        # self.student_table.heading("year",text="Year")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("emp_id",text="Emp ID")
        # self.student_table.heading("roll",text="Roll")
        self.student_table.heading("email_id",text="Email ID")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="phone")
     
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        # self.student_table.column("course",width=100)
        # self.student_table.column("year",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("emp_id",width=100)
        # self.student_table.column("roll",width=100)
        self.student_table.column("email_id",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
       
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        # self.mtcnn = MTCNN()
        self.data_dir = "data"
        self.cap = None
        self.frame = None
        # self.show_frame()
        # Camera feed label
        self.camera_label = Label(self.root)
        self.camera_label.pack()
        self.capture_image_btn = Button(self.root, text="Capture Image", command=self.generate_dataset)
        self.capture_image_btn.place(x=10, y=40)
        self.capture_image_btn.pack_forget()
        
#----------function data--------
    def add_data(self):  
        print("clicked on save button")
        print(self.var_dep.get(), self.var_name.get(), self.var_emp_id.get(), self.var_email_id.get(), self.var_gender.get(), self.var_phone.get())
        if self.var_radio1.get()=="":
            messagebox.showerror("Error","Please Take a photo sample",parent=self.root)
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_emp_id.get()=="" or self.var_email_id.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password=DB_PASSWORD,database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_emp_id.get(),
                                                                        self.var_name.get(),
                                                                        self.var_dep.get(),
                                                                        self.var_email_id.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_phone.get()
                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    #   fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password=DB_PASSWORD,database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_emp_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_email_id.set(data[3]),
        self.var_gender.set(data[4]),
        self.var_phone.set(data[5])
        
        # update function
        
    def Update_data(self):
        if self.var_dep.get()=="select Department" or self.var_name.get()=="" or self.var_emp_id.get()=="" or self.var_email_id.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this employee details",parent=self.root)
                if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password=DB_PASSWORD,database="face_recognition")
                        my_cursor=conn.cursor()
                        querry = "update employee set dep='{}',name='{}',email_id='{}',gender='{}',Phone='{}' where  emp_id = '{}'".format(self.var_dep.get(),
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_email_id.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_emp_id.get())
                        my_cursor.execute(querry)
                else:
                    if not Update:
                     return
                messagebox.showinfo("Success","Employee details successfully Update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
        #delet button
    def delete_data(self):
        if self.var_emp_id.get()=="":
                messagebox.showerror("Error","employee id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    con = mysql.connector.connect(host="localhost",user="root",password=DB_PASSWORD,database="face_recognition")
                    curser = con.cursor()
                    emp_id = self.var_emp_id.get()
                    querry2 = "DELETE FROM employee WHERE emp_id='%s'"%(emp_id)
                    curser.execute(querry2)
                    x = self.student_table.selection()[0]
                    self.student_table.delete(x)

                    con.commit() 
                    count = curser.execute("select count(emp_id) from employee")


                else:
                    if not delete:
                        return
                for i in range(NO_OF_IMAGE):
                    try:
                        os.remove(f'data/user_{emp_id}_{i}.jpg')
                    except:
                        pass
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                print(es)
                
                
# reset
    
    def reset_data(self):
            self.var_name.set(""),  
            self.var_email_id.set(""),
            self.var_gender.set("Other"),
            self.var_phone.set(""),
            self.var_emp_id.set("")
            
    def start_camera(self):
        try:
            self.cap = cv2.VideoCapture(0)
            self.show_frame()

            
            self.capture_image_btn.pack()

            self.root.bind('q', self.close_camera)
        except Exception as e:
            print(e)

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.frame = frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)
            self.camera_label.imgtk = frame
            self.camera_label.configure(image=frame)
            self.camera_label.after(10, self.show_frame)
    def close_camera(self):
        if self.cap.isOpened():
            self.cap.release()
        # Hide the camera frame or label, assuming self.camera_label is the widget displaying the camera feed
        self.camera_label.pack_forget()
 
            
# generate data set or take photo sample 
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_emp_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                print("code is generating the dataset for id:", self.var_emp_id.get())
                conn=mysql.connector.connect(host="localhost",username="root",password=DB_PASSWORD,database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from face_recognition.employee where emp_id={};".format(self.var_emp_id.get()))
                myresult=my_cursor.fetchall()
                if self.frame is not None:
                    id = self.var_emp_id.get()
                    if not os.path.exists(os.path.join(self.data_dir,id)):
                        # If it doesn't exist, create the folder
                        os.makedirs(os.path.join(self.data_dir,id))
                    count = len(os.listdir(os.path.join(self.data_dir, id)))
                    cv2.imwrite(f'data/{id}/{count}.jpg', self.frame)
                    messagebox.showinfo("Result", "Image captured and saved!", parent=self.root)
                else:
                    messagebox.showerror("Error", "Start the camera feed before capturing an image.", parent=self.root)
            except Exception as es:
                print(es)
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                
                
        
                   
if __name__ == "__main__":
     root=Tk()
     obj=employee(root)
     root.mainloop()