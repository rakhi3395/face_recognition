import tkinter as tk
import mysql.connector
from tkinter import messagebox
import cv2
from datetime import datetime
import uuid
from config import DB_PASSWORD
from mtcnn import MTCNN

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Camera App")
        self.master.geometry("800x500+300+100")
        self.create_ui()
        # self.faceCascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("models/classifier.xml")
        self.detector = MTCNN()

    def create_ui(self):
        # Frame for the form
        form_frame = tk.Frame(self.master, bg="skyblue")
        form_frame.place(x=0, y=0, width=1530, height=790)

        register_label = tk.Label(form_frame, text="CAMERA FORM", font=("times new roman", 20, "bold"), fg="darkblue", bg="skyblue")
        register_label.place(x=30, y=20)

        # Labels and entry fields for camera name and IP with larger font size
        tk.Label(form_frame, text="Camera Name:", font=("Arial", 14), bg="skyblue").place(x=50, y=80)
        self.camera_name_entry = tk.Entry(form_frame, font=("Arial", 13))
        self.camera_name_entry.place(x=200, y=80)

        tk.Label(form_frame, text="Camera IP:", font=("Arial", 14), bg="skyblue").place(x=50, y=120)
        self.camera_ip_entry = tk.Entry(form_frame, font=("Arial", 13))
        self.camera_ip_entry.place(x=200, y=120)

        # Blue-colored Save button with larger font size
        save_button = tk.Button(form_frame, text="Save", command=self.save_camera, bg="blue", fg="white", font=("Arial", 12))
        save_button.place(x=260, y=150)

        # Green-colored Preview button with larger font size
        open_camera_button = tk.Button(form_frame, text="Open Camera", command=self.open_camera, bg="green", fg="white", font=("Arial", 12))
        open_camera_button.place(x=50, y=240)

        # Listbox to display saved cameras
        self.camera_listbox = tk.Listbox(form_frame, font=("Arial", 10))
        self.camera_listbox.place(x=50, y=274, width=330, height=150)


        preview_button = tk.Button(self.master, text="Preview", command=self.preview_camera, bg="yellow", font=("Arial", 12))
        preview_button.pack()
        preview_button.place(x=180, y=240)

        # Dictionary to store camera names as keys and IP addresses as values
        self.camera_dict = {}

        # Load initial camera data
        self.load_camera_data()

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


    def save_camera(self):
        # Get camera name and IP from the entry fields
        camera_name = self.camera_name_entry.get().strip()
        camera_ip = self.camera_ip_entry.get().strip()
        if camera_ip=="localhost" or camera_ip == "127.0.0.1":
            camera_ip = 0
        if camera_name and (camera_ip or camera_ip==0):  # Check if fields are not empty
            # Attempt to open the camera stream to check if it's working
            cap = cv2.VideoCapture(camera_ip)
            if cap.isOpened():
                # If the camera is working, save its details in the database
                self.save_to_database(camera_name, camera_ip)
                cap.release()  # Release the camera

                # Clear entry fields and reload camera data
                self.camera_name_entry.delete(0, tk.END)
                self.camera_ip_entry.delete(0, tk.END)
                self.load_camera_data()
            else:
                cap.release()  # Release the camera
                messagebox.showerror("Error", "Unable to open the camera. Please check the camera IP.")
        else:
            messagebox.showerror("Error", "Camera Name and IP cannot be empty!")


    def load_camera_data(self):
        # Retrieve camera names and IPs from the database and populate the listbox and dictionary
        conn = mysql.connector.connect(host="localhost", username="root", password=DB_PASSWORD, database="face_recognition")
        cursor = conn.cursor()
        select_query = "SELECT camera_name, camera_ip FROM cameras"
        cursor.execute(select_query)
        cameras = cursor.fetchall()
        self.camera_listbox.delete(0, tk.END)
        self.camera_dict.clear()
        for camera in cameras:
            camera_name, camera_ip = camera
            self.camera_listbox.insert(tk.END, camera_name)
            self.camera_dict[camera_name] = camera_ip
        conn.close()

    def open_camera(self):
        # Get the selected camera name from the listbox
        selected_camera_name = self.camera_listbox.get(self.camera_listbox.curselection())

        # Get the corresponding IP address from the dictionary
        camera_ip = self.camera_dict.get(selected_camera_name)
        print("face_recognition started")
        # Open the selected camera stream
        # check if local camera
        if camera_ip=="0":
            camera_ip=0
        cap = cv2.VideoCapture(camera_ip)
        is_mark_attendance = False
        previous_id = -1
        # Define the ROI (Region of Interest) boundaries
        roi_x, roi_y, roi_width, roi_height = 100, 100, 700, 500
        while True:
            ret, img = cap.read()
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # features = self.faceCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)
            faces = self.detector.detect_faces(img)
            for face in faces:
                # Check if the face coordinates are within the ROI
                x, y, w, h = face['box']
                confidence = face['confidence']
                if confidence > 0.5:  # Adjust the threshold as needed
                    if roi_x <= x and x + w <= roi_x + roi_width and roi_y <= y and y + h <= roi_y + roi_height:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Draw green rectangle on the face
                        emp_id, predict = self.clf.predict(gray_image[y:y + h, x:x + w])
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
            
            # Draw a red rectangle around the ROI
            cv2.rectangle(img, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 0, 255), 3)

            cv2.imshow("Welcome To Face Recognition", img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

    def preview_camera(self):
        # Get the selected camera name from the listbox
        selected_camera_name = self.camera_listbox.get(self.camera_listbox.curselection())
        # Get the corresponding IP address from the dictionary
        camera_ip = self.camera_dict.get(selected_camera_name)
        width, height = 600, 500
        # Open the selected camera stream in a preview window
        preview_window = tk.Toplevel(self.master)
        preview_window.title(f"Preview: {selected_camera_name}")
        preview_window.geometry(f"{width}x{height}")
        print("camera ip:", camera_ip)
        # check if local camera
        if camera_ip=="0":
            camera_ip=0
        print("camera ip:",camera_ip)
        cap = cv2.VideoCapture(camera_ip)
        while True:
            ret, frame = cap.read()
            cv2.imshow(f"Preview: {selected_camera_name}", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def save_to_database(self, camera_name, camera_ip):
        # Establish a MySQL connection and save camera details in the database
        conn = mysql.connector.connect(host="localhost", username="root", password=DB_PASSWORD, database="face_recognition")
        cursor = conn.cursor()
        insert_query = "INSERT INTO cameras (camera_name, camera_ip) VALUES (%s, %s)"
        data = (camera_name, camera_ip)
        cursor.execute(insert_query, data)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()