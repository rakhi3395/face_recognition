from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1280x690+0+0")
            self.root.title("face Recognition system")
            
            
            self.var_atten_id=StringVar()
            self.var_atten_roll=StringVar()
            self.var_atten_name=StringVar()
            self.var_atten_dep=StringVar()
            self.var_atten_time=StringVar()
            self.var_atten_date=StringVar()
            self.var_atten_attendance=StringVar()
            
            
        
            img = Image.open("assets/attandance1.jpg")
            img = img.resize((700,200),Image.ANTIALIAS)
            self.photoimg=ImageTk.PhotoImage(img)
            f_lbl=Label(self.root,image=self.photoimg)
            f_lbl.place(x=0,y=0,width=700,height=150)

            img1 = Image.open("assets/att.jpg")
            img1 = img1.resize((700,200),Image.ANTIALIAS)
            self.photoimg1=ImageTk.PhotoImage(img1)
            f_lbl=Label(self.root,image=self.photoimg1)
            f_lbl.place(x=700,y=0,width=700,height=150)

            # # bg image
            # img3 = Image.open("assets/facemask1.jpg")
            # img3 = img3.resize((1500,710),Image.ANTIALIAS)
            # self.photoimg3=ImageTk.PhotoImage(img3)
            # bg_img=Label(self.root,image=self.photoimg3)
            # bg_img.place(x=0,y=130,width=1530,height=710)

            title_lbl=Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="skyblue",fg="black")
            title_lbl.place(x=0,y=0,width=1280,height=45)
        
            main_frame=Frame(self.root, bd=2,bg="white")
            main_frame.place(x=5,y=195,width=1280,height=600)
        
        # left frame
            Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
            Left_frame.place(x=0,y=10,width=630,height=500)
        
            img_left = Image.open("assets/ai.jpg")
            img_left = img_left.resize((630,130),Image.ANTIALIAS)
            self.photoimg_left=ImageTk.PhotoImage(img_left)
        
            f_lbl=Label(Left_frame,image=self.photoimg_left)
            f_lbl.place(x=0,y=0,width=630,height=130)
        
            left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
            left_inside_frame.place(x=0,y=135,width=625,height=250)
        
        # labeled entry
        # attandance id
            attendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
            attendanceID_label.grid(row=0,column=0,padx=15,pady=5,sticky=W)
            attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
            attendanceID_entry.grid(row=0,column=1,padx=10,pady=5)
        
        # roll
            rollLabel=Label(left_inside_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
            rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)
            atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
            atten_roll.grid(row=0,column=3,pady=8)
        
        # department
            depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
            depLabel.grid(row=1,column=0)
            atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
            atten_dep.grid(row=1,column=1,pady=8)
        
        # name
            nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
            nameLabel.grid(row=1,column=2)
            atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
            atten_name.grid(row=1,column=3,pady=8)
        
        # date
            dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
            dateLabel.grid(row=2,column=0)
            atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
            atten_date.grid(row=2,column=1,pady=8)
         
        # time
            timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
            timeLabel.grid(row=2,column=2)
            atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
            atten_time.grid(row=2,column=3,pady=8)
        
        # attendance
            attendanceLabel=Label(left_inside_frame,text="Attendance Status",font=("comicsansns",11,"bold"),bg="white")
            attendanceLabel.grid(row=3,column=0)
        
            self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("comicsansns",11,"bold"),state="readonly")
            self.atten_status["values"]=("Status","Present","Absent")
            self.atten_status.current(0)
            self.atten_status.grid(row=3,column=1,pady=8)
        
        #Button
            btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame.place(x=0,y=200,width=620,height=36)
        
            import_btn=Button(btn_frame,text="IMPORT csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
            import_btn.grid(row=0,column=0)   
        
            update_btn=Button(btn_frame,text="UPDATE",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
            update_btn.grid(row=0,column=1)   
        
            export_btn=Button(btn_frame,text="EXPORT csv",command=self.exportCsv,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
            export_btn.grid(row=0,column=3)   
        
            reset_btn=Button(btn_frame,text="RESET",width=15,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
            reset_btn.grid(row=0,column=4)
        
        
        # right frame
            Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student_Details",font=("times new roman",12,"bold"))
            Right_frame.place(x=650,y=10,width=630,height=500)
        
            table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
            table_frame.place(x=5,y=5,width=600,height=450)
        
        #  scroll bar table
            Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
            Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
            self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
            Scroll_x.pack(side=BOTTOM,fill=X)
            Scroll_y.pack(side=RIGHT,fill=Y)
        
            Scroll_x.config(command=self.AttendanceReportTable.xview)
            Scroll_y.config(command=self.AttendanceReportTable.yview)
        
            self.AttendanceReportTable.heading("id",text="Attendence ID")
            self.AttendanceReportTable.heading("roll",text="Roll No.")
            self.AttendanceReportTable.heading("name",text="Name")
            self.AttendanceReportTable.heading("department",text="Department")
            self.AttendanceReportTable.heading("time",text="Time")
            self.AttendanceReportTable.heading("date",text="Date")
            self.AttendanceReportTable.heading("attendance",text="Attendance")
        
            self.AttendanceReportTable["show"]="headings"
            self.AttendanceReportTable.column("id",width=100)
        
            self.AttendanceReportTable.pack(fill=BOTH,expand=1)
            
            self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
    # fetch data
        
        def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
        
        #import csv
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)            
        
        #export csv
        def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("No Data","No Data Found to EXPORT",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"sucessfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
        def get_cursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            row=content['values']
            # print("rows:",row)
            self.var_atten_id.set(row[0])
            self.var_atten_roll.set(row[1])
            self.var_atten_name.set(row[2])
            self.var_atten_dep.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_attendance.set(row[6])
        
        
        def reset_data(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")
            
            
            
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()