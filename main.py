from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
from sre_constants import SUCCESS
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("face Recognition System")

    
        # bg img
        img=Image.open(r"C:\face recognition\college_images\center.png")
        img=img.resize((1400,830),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1380,height=800)

        #button1
        img1=Image.open(r"C:\face recognition\college_images\profile.jpeg")
        img1=img1.resize((160,160),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=1240,y=30,width=160,height=160)
       
        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1240,y=195,width=160,height=30)

        #button2
        img2=Image.open(r"C:\face recognition\college_images\face.jpeg")
        img2=img2.resize((160,160),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.photoimg2,command=self.checkPerson,cursor="hand2")
        b2.place(x=1035,y=220,width=160,height=160)
       
        b2_1=Button(bg_img,text="Face Recognition",command=self.checkPerson,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=1035,y=385,width=160,height=30)

        #button3
        img3=Image.open(r"C:\face recognition\college_images\developer001.jpeg")
        img3=img3.resize((160,160),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b3.place(x=1240,y=410,width=160,height=160)
       
        b3_1=Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=1240,y=575,width=160,height=30)

        #button4
        img4=Image.open(r"C:\face recognition\college_images\pic7.jpeg")
        img4=img4.resize((160,160),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b4.place(x=1035,y=580,width=160,height=160)
       
        b4_1=Button(bg_img,text="Photos ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1035,y=745,width=160,height=30)


    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)

    def checkPerson(self):

        path = 'images'
        images = []
        personNames = []
        myList = os.listdir(path)
        print(myList)
        for cu_img in myList:
            current_Img = cv2.imread(f'{path}/{cu_img}')
            images.append(current_Img)
            personNames.append(os.path.splitext(cu_img)[0])
        print(personNames)


        def faceEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        def attendance(name):
            with open('Attendance.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    time_now = datetime.now()
                    tStr = time_now.strftime('%H:%M:%S')
                    dStr = time_now.strftime('%D/%m/%Y')
                    f.writelines(f'\n{name},{tStr},{dStr}')


        encodeListKnown = faceEncodings(images)
        print('All Encodings Complete!!!')

        cap = cv2.VideoCapture(0)

        while True:
            SUCCESS, frame = cap.read()
            faces = cv2.resize(frame,(0,0),None,0.25,0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = face_recognition.face_locations(faces)
            encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

            for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = personNames[matchIndex].upper()
                    # print(name)
                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    attendance(name)

            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) == 13:
                cv2.imshow('Webcam', frame)
                
            if cv2.waitKey(1) == 27:
                cap.release()
                cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


  