from mimetypes import init
from multiprocessing import connection
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x790+0+0")
        self.root.title("face Recognition System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_name=StringVar()
        self.var_std_id=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        

        # bg img
        img=Image.open(r"C:\face recognition\college_images\center.png")
        img=img.resize((1400,830),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1500,height=830)

        main_frame=Frame(bg_img,bd=2,bg="sky blue")
        main_frame.place(x=90,y=40,width=1315,height=710)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        Left_frame.place(x=10,y=10,width=640,height=675)
    #--------------------------------------------------------------------
        #Course info
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",16,"bold"))
        current_course_frame.place(x=10,y=10,width=615,height=140)

             #dep
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",14,"bold"))
        dep_label.grid(row=0,column=0,padx=10,pady=15)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","ENTC","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

             #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",14,"bold"))
        course_label.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

             #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",14,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

            #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",14,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    #------------------------------------------------------------------------------
        #Student Class Information
        student_class_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Course Information",font=("times new roman",16,"bold"))
        student_class_frame.place(x=10,y=150,width=615,height=350)

            #Student Name
        studentName_label=Label(student_class_frame,text="Student Name",font=("times new roman",14,"bold"))
        studentName_label.grid(row=0,column=0,padx=10,pady=30,sticky=W)

        studentName_entry=ttk.Entry(student_class_frame,width=14,textvariable=self.var_std_name,font=("times new roman",16,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,sticky=W,pady=10)

            #Student ID
        studentId_label=Label(student_class_frame,text="Student ID",font=("times new roman",14,"bold"))
        studentId_label.grid(row=0,column=2,padx=5,pady=30,sticky=W)

        studentId_entry=ttk.Entry(student_class_frame,textvariable=self.var_std_id,width=10,font=("times new roman",16,"bold"))
        studentId_entry.grid(row=0,column=3,padx=5,sticky=W,pady=10)
        
            #roll no
        rollNo_label=Label(student_class_frame,text="Roll No",font=("times new roman",14,"bold"))
        rollNo_label.grid(row=1,column=0,padx=10,sticky=W)

        rollNo_entry=ttk.Entry(student_class_frame,textvariable=self.var_roll,width=14,font=("times new roman",16,"bold"))
        rollNo_entry.grid(row=1,column=1,padx=10,sticky=W)

            #DOB
        dob_label=Label(student_class_frame,text="DOB",font=("times new roman",14,"bold"))
        dob_label.grid(row=1,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(student_class_frame,textvariable=self.var_dob,width=10,font=("times new roman",16,"bold"))
        dob_entry.grid(row=1,column=3,padx=5,sticky=W,pady=10)

            #email
        email_label=Label(student_class_frame,text="Email",font=("times new roman",14,"bold"))
        email_label.grid(row=2,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(student_class_frame,textvariable=self.var_email,width=14,font=("times new roman",16,"bold"))
        email_entry.grid(row=2,column=1,padx=10,sticky=W)  

            #Phone no
        phoneNo_label=Label(student_class_frame,text="Phone No",font=("times new roman",14,"bold"))
        phoneNo_label.grid(row=2,column=2,padx=10,sticky=W)

        phoneNo_entry=ttk.Entry(student_class_frame,textvariable=self.var_phone,width=10,font=("times new roman",16,"bold"))
        phoneNo_entry.grid(row=2,column=3,padx=5,sticky=W,pady=10)

            #Class Division
        class_Div_label=Label(student_class_frame,text="Class Division",font=("times new roman",14,"bold"))
        class_Div_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        class_Div_combo=ttk.Combobox(student_class_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=17)
        class_Div_combo["values"]=("Select Division","Division A","Division B","Division C","Division D","Division E")
        class_Div_combo.current(0)
        class_Div_combo.grid(row=3,column=1,padx=10,sticky=W)

            #Gender
        gender_label=Label(student_class_frame,text="Gender",font=("times new roman",14,"bold"))
        gender_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(student_class_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=12)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=3,padx=5,sticky=W)
        
            #radio button
        
        radionBtn1=ttk.Radiobutton(student_class_frame,variable=self.var_radio1,text="Take A Photo Sample",value="Yes")
        radionBtn1.grid(row=4,column=0,padx=10,pady=10)

        
        radionBtn2=ttk.Radiobutton(student_class_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radionBtn2.grid(row=4,column=1,padx=10,pady=10)

            #teacher
        teacher_label=Label(student_class_frame,text="Teacher Name",font=("times new roman",14,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(student_class_frame,textvariable=self.var_teacher,width=10,font=("times new roman",16,"bold"))
        teacher_entry.grid(row=4,column=3,padx=5,sticky=W,pady=10)



 

    #------------------------------------------------------------------------- 

        #Buttons frame
        btn_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",16,"bold"))
        btn_frame.place(x=10,y=505,width=615,height=130)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        save_btn.grid(row=0,column=0,padx=15,pady=15)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        update_btn.grid(row=0,column=1,padx=10,pady=15)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        delete_btn.grid(row=0,column=2,padx=10,pady=15)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        reset_btn.grid(row=0,column=3,padx=10,pady=15)

        #frame 2 -------------------------------------------------------------
        take_photo_btn=Button(btn_frame,text="Take Photo Sample",command=self.captureImage,width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        take_photo_btn.grid(row=1,column=1,padx=10,pady=15)

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        update_photo_btn.grid(row=1,column=2,padx=10,pady=15)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
       
        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        Right_frame.place(x=670,y=10,width=630,height=675)    

            #searching system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",16,"bold"))
        search_frame.place(x=10,y=10,width=605,height=100)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="dark grey")
        search_label.grid(row=0,column=0,padx=10,sticky=W)
            
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",16,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W,pady=10)

        search_btn=Button(search_frame,text="Search",width=11,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        search_btn.grid(row=0,column=3,padx=7,pady=15)

        showAll_btn=Button(search_frame,text="Show All",width=11,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        showAll_btn.grid(row=0,column=4,padx=7,pady=15)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=120,width=605,height=470)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("name","id","div","roll","year","dep","course","sem","gender","dob","email","phone","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("name",text="Name")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("name",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        back_btn=Button(Right_frame,text="Back",width=17,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        back_btn.place(x=250,y=605)
        
    # function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or  self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Recquired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sanhita1416@",database="psp")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_std_name.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()                  
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    #fetchdata 
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sanhita1416@",database="psp")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
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

        self.var_std_name.set(data[0]),
        self.var_std_id.set(data[1]),
        self.var_div.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_year.set(data[4]),
        self.var_dep.set(data[5])
        self.var_course.set(data[6]),
        self.var_semester.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10])
        self.var_phone.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])

    # update btn
    def update_data(self):
        if self.var_dep.get()=="Select Department" or  self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Recquired",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sanhita1416@",database="psp")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set std_name=%s;div=%s;roll=%s;year=%s;dep=%s;course=%s;semester=%s;gender=%s;dob=%s;email=%s;phone=%s;teacher=%s;photosample=%s where std_id=%s",(
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))
                
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if not Update:
                        return                                                                                                                                                                  
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

     #delete btn
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be recquired",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sanhita1416@",database="psp")
                    my_cursor=conn.cursor()
                    sql="delete from student where std_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset btn
    def reset_data(self):
        self.var_std_name.set("")
        self.var_std_id.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_year.set("Select year")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_gender.set("Select Gender")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    #----------------------------------------------------------------------------------------------------------------------------------------
    def captureImage(self):
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "images/Newuser_."+"{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()
        messagebox.showinfo("Updated PhotoSample","PhotoSample updated succesfully...!",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

