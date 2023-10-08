from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from time import strftime
import cv2
import os
import numpy as np
import face_recognition as face_recognition
import csv
import glob
import uuid
from config import DB_PASSWORD
class face_detection:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition syetrm")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # 1st image
        
        img_top = Image.open("assets/saurabh.jpeg")
        img_top = img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=800,height=700)
        
        
        # 2nd image
        
        img_bottom = Image.open("assets/recognition.jpg")
        img_bottom = img_bottom.resize((650,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=700,y=55,width=800,height=700)
        
        # button
        
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=300,y=620,width=200,height=40) 
        
        
        
        # attendance
    def mark_attendance(self,emp_id,email_id,name,dep):
        current_date = datetime.now().date()
        # print("current_date:",current_date)
        conn = mysql.connector.connect(host="localhost", username="root", password=DB_PASSWORD, database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute(f"SELECT attendance_id FROM face_recognition.attendance WHERE emp_id = {emp_id} AND date='{current_date}'")
        fetched_data = my_cursor.fetchone()
        if fetched_data:
            # handle checkout case
            attendance_id = fetched_data[0]
            checkout_time = datetime.now()
            my_cursor.execute(f"UPDATE attendance SET checkout_time = '{checkout_time}' WHERE attendance_id = '{attendance_id}'")
            conn.commit()
            conn.close()

        else:
            # handle checkin date
            attendance_id = str(uuid.uuid4())
            checkin_time = datetime.now()
            insert_query = "INSERT INTO attendance (attendance_id, emp_id, date, email_id, name, dep, checkin_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (attendance_id, emp_id, current_date, email_id, name, dep, checkin_time)
            my_cursor.execute(insert_query, data)
            conn.commit()
            conn.close()
        
    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("models/classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        is_mark_attendance = False
        previous_id = -1
        while True:
            ret, img = video_cap.read()
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = faceCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                emp_id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password=DB_PASSWORD, database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute(f"SELECT emp_id, email_id, name, dep FROM employee WHERE emp_id = {emp_id}")
                matched_data = my_cursor.fetchone()
                if matched_data:
                    if previous_id!=matched_data[0]:
                        is_mark_attendance = False
                        previous_id = matched_data[0]
                        # print("matched_data:", matched_data[0])
                conn.close()
                
                if matched_data is not None and confidence > 50:
                    # print("is_mark_attendance:",is_mark_attendance)
                    emp_id, email_id, name, dep = matched_data[0], matched_data[1], matched_data[2], matched_data[3]
                    cv2.putText(img, f"emp_id:{emp_id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"email_id:{email_id}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"name:{name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"department:{dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    if not is_mark_attendance:
                        self.mark_attendance(emp_id, email_id, name, dep)
                        is_mark_attendance = True
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    is_mark_attendance = False
            
            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        video_cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
     root=Tk()
     obj=face_detection(root)
     root.mainloop()