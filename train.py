from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import numpy as np
import cv2
import os
from mtcnn import MTCNN
from deepface.basemodels import VGGFace
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition syetrm")
        self.data_dir="data"
        
        
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
        # Initialize variables
        self.mtcnn = MTCNN()
        self.embeddings = {}
        self.model_path = "models/embeddings.npy"
        self.img_size = (224,224)
        self.model = VGGFace.loadModel()
    def train_classifier(self):
        for employee_folder in os.listdir(self.data_dir):

            # Load employee photos from the provided folder
            for filename in os.listdir(os.path.join(self.data_dir,employee_folder)):
                if filename.endswith(".jpg"):
                    img_path = os.path.join(os.path.join(self.data_dir,employee_folder), filename)
                    # print(img_path)
                    img = cv2.imread(img_path)
                    # Extract faces from the image, even if a face is not detected (enforce_detection=False)
                    detected_faces = self.mtcnn.detect_faces(img)
                
                    # if detected_faces is not None and len(detected_faces) > 0:
                    # print(len(detected_faces))
                    for face in detected_faces:
                        # Extract facial embeddings
                        x, y, w, h = face['box']
                        confidence = face['confidence']
                        if confidence>0.7:
                            face_img = img[y:y+h, x:x+w]
                            face_img = cv2.resize(face_img, self.img_size)

                            # print("face_img:",face_img)
                            face_img = face_img / 255.0  # Normalize the image

                            # Add batch dimension
                            face_img = np.expand_dims(face_img, axis=0)
                            embedding = self.model.predict(face_img)
                            self.embeddings[employee_folder]=embedding
        
        np.save(self.model_path, self.embeddings)
        # print("xxxxxxxxx")
        # print(len(self.face_images))
        # print(self.labels)
        # labels = self.label_encoder.fit_transform(self.labels)
        # label_mapping  = {}
        # for i in range(len(labels)):
        #     label_mapping[int(labels[i])] = self.labels[i]
        # with open('models/label_mapping.json', 'w') as f:
        #     json.dump(label_mapping, f)
        # # print(labels)
        # # # One-hot encode the labels using to_categorical
        # # labels = to_categorical(labels, num_classes=len(np.unique(labels)))

        # # Split the dataset into training and validation sets
        # X_train, X_val, y_train, y_val = train_test_split(self.face_images, labels, test_size=0.2, random_state=42)
        # # Load the pre-trained VGGFace model
        # base_model = VGG16(weights='imagenet', include_top=False)
        # print("y_train:",y_train)
        # # Add custom classification layers
        # x = base_model.output
        # x = GlobalAveragePooling2D()(x)
        # x = Dense(1024, activation='relu')(x)
        # predictions = Dense(len(np.unique(labels)), activation='softmax')(x)

        # model = Model(inputs=base_model.input, outputs=predictions)
        # # Compile the model
        # model.compile(optimizer=Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # # Create data generators for training and validation
        # train_data_generator = ImageDataGenerator(rescale=1.0/255.0)
        # val_data_generator = ImageDataGenerator(rescale=1.0/255.0)

        # # Convert the lists to arrays
        # X_train = np.array(X_train)
        # y_train = np.array(y_train)
        # X_val  = np.array(X_val)
        # y_val = np.array(y_val)

        # train_generator = train_data_generator.flow(X_train, y_train, batch_size=32)
        # val_generator = val_data_generator.flow(X_val, y_val, batch_size=32)

        # # Fine-tune the model on your dataset
        # model.fit(train_generator, validation_data=val_generator, epochs=10)

        # # Save the fine-tuned model for recognition
        # model.save('models/fine_tuned_model.h5')
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!!")
    
            
        
if __name__ == "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()