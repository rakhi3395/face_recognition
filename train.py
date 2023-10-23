from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition syetrm")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top = Image.open("assets/22.jpg")
        img_top = img_top.resize((1530,420),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=420)
        
        # button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=399,width=1530,height=60)
        
        img_bottom = Image.open("assets/23.jpg")
        img_bottom = img_bottom.resize((1530,320),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=460,width=1530,height=320)
        self.face_recognition_model = load_model("models/facenet_keras.h5")
        
    def train_classifier(self):        
        
        # Train the classifier and save
            
        # Data directory with labeled subdirectories for each person
        data_dir = "data"

        # Collect labeled face embeddings and corresponding person IDs
        embeddings = []
        labels = []

        for person_dir in os.listdir(data_dir):
            for image_file in os.listdir(os.path.join(data_dir, person_dir)):
                image_path = os.path.join(data_dir, person_dir, image_file)
                img = Image.open(image_path).convert('RGB')
                img = img.resize((160, 160))
                face_array = np.array(img) / 255.0  # Normalize
                embeddings.append(face_recognition_model.predict(np.expand_dims(face_array, axis=0))
                labels.append(person_dir)

        # Convert labels to integer IDs using LabelEncoder
        label_encoder = LabelEncoder()
        labels = label_encoder.fit_transform(labels)

        # Train a classifier (SVM)
        classifier = SVC(C=1, kernel='linear', probability=True)
        classifier.fit(embeddings, labels)

        # Save the trained classifier
        from joblib import dump
        dump(classifier, 'classifier.pkl')
    
            
        
if __name__ == "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()