
from tkinter import*
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from time import strftime 
from datetime import datetime
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


def home():
    nav_text=Label(root,text='Home',font=('times new roman',15,'bold'),bg='#636466',fg='white',width=15)
    nav_text.place(relx=0.01,rely=0.005)
    #slideshow
    img1=ImageTk.PhotoImage(Image.open("tasveer/campus4.jpeg").resize((1365,480)))
    img2=ImageTk.PhotoImage(Image.open("tasveer/student-life.jpg").resize((1365,480)))
    img3=ImageTk.PhotoImage(Image.open("tasveer/campus12.jpeg").resize((1365,480)))
    img4=ImageTk.PhotoImage(Image.open("tasveer/Campus-1.jpg").resize((1365,480)))
    img5=ImageTk.PhotoImage(Image.open("tasveer/student.jpeg").resize((1365,480)))
    
    #label for slide
    l=Label()
    l.place(relx=0,rely=0.31)
    #funtion for slideshow
    # using recursion to slide to next image
    

    # function to change to next image
    def move():
        global z
        if z == 6:
            z = 1
        if z == 1:
            l.config(image=img1)
        elif z == 2:
            l.config(image=img2)
        elif z == 3:
            l.config(image=img3)
        elif z == 4:
            l.config(image=img4)
        elif z == 5:
            l.config(image=img5)
        z = z+1
        root.after(2000, move)

    # calling the function
    move()

def student_func():
    nav_text=Label(root,text='Student Details',font=('times new roman',15,'bold'),bg='#636466',fg='white',width=15)
    nav_text.place(relx=0.01,rely=0.005)
    #backend
    #variables
    var_dept=StringVar()
    var_course=StringVar()
    var_year=StringVar()
    var_sem=StringVar()
    var_stdID=StringVar()
    var_stdName=StringVar()
    var_div=StringVar()
    var_rollno=StringVar()
    var_gender=StringVar()
    var_dob=StringVar()
    var_email=StringVar()
    var_mobile=StringVar()
    var_add=StringVar()
    var_tsp=StringVar()
         
    def save_func():
        if var_stdID.get()=='' or var_stdName.get()=='' or var_div.get()=='Select Division' or var_rollno.get()=='':
            messagebox.showerror('Error','All Fields are Required!!!')
        else:
            try:
                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()
                db_cursor.execute(' INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(   var_dept.get(), 
                    var_course.get(),
                    var_year.get(),
                    var_sem.get(),
                    var_stdID.get(),
                    var_stdName.get(),
                    var_div.get(),
                    var_rollno.get(),
                    var_gender.get(),
                    var_dob.get(),
                    var_email.get(),
                    var_mobile.get(),
                    var_add.get(),
                    var_tsp.get(),
                ))  
                conn.commit()
                fetch_data()
                conn.close()

                messagebox.showinfo('Saved','Student Details Saved Successfully ')
            except Exception as e:
                messagebox.showerror('Error',f'Due to {e}')
    
    #fetch data into table 
    def fetch_data():
        conn=sqlite3.connect('Student_DB.db')
        db_cursor=conn.cursor()
        db_cursor.execute('SELECT * FROM student')
        Data=db_cursor.fetchall()
        if len(Data)!=0:
            table.delete(* table.get_children())
            for i in Data:
                table.insert('',END,values=i)
            conn.commit()
            conn.close()
#cursor to the table
    def cursor_func(event):
        cursor_focus=table.focus()
        content=table.item(cursor_focus)
        data=content['values']
        var_dept.set(data[0]),
        var_course.set(data[1]),
        var_year.set(data[2]),
        var_sem.set(data[3]),
        var_stdID.set(data[4]),
        var_stdName.set(data[5]),
        var_div.set(data[6]),
        var_rollno.set(data[7]),
        var_gender.set(data[8]),
        var_dob.set(data[9]),
        var_email.set(data[10]),
        var_mobile.set(data[11]),
        var_add.set(data[12]),
        var_tsp.set(data[13])

#update function
    def updata():
        if var_stdID.get()=='' or var_stdName.get()=='' or var_div.get()=='Select Division' or var_rollno.get()=='':
            messagebox.showerror('Error','All Fields are Required!!!')
        else:
            try:
                Update=messagebox.askyesno('Update!!!',f'Do you want to update student detail of {var_stdID.get()}?')
                if Update>0:
                    conn=sqlite3.connect('Student_DB.db')
                    db_cursor=conn.cursor()
                    db_cursor.execute(" UPDATE student SET Department=?, Course=?, Year=?, Semister=?, Student_Name=?, Division=?,Rollno=?, Gender=?, DOB=?,Email=?, Mobile=?, Address=?,PhotoSample=? WHERE StudentID=?",(   var_dept.get(), var_course.get(),var_year.get(),var_sem.get(),var_stdName.get(),var_div.get(),var_rollno.get(),var_gender.get(),var_dob.get(),var_email.get(),var_mobile.get(),var_add.get(),var_tsp.get(),var_stdID.get(),
                ))  
                else:
                    if  not Update:
                        return
                messagebox.showinfo('Updated',f'{var_stdID.get()} student detail Successfully Updated.')
                conn.commit()
                fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error',f'Due to {e}')

#delete data function
    def delta():
        if var_stdID.get()=='':
            messagebox.showerror('Error','StudentID no.  Required!!!')
        else:
            try:
                delete=messagebox.askyesno('Delete!!!',f'Do you want to delete student detail of {var_stdID.get()}?')
                if delete>0:
                    conn=sqlite3.connect('Student_DB.db')
                    db_cursor=conn.cursor()
                    db_cursor.execute('DELETE  FROM student WHERE StudentID=? ',(var_stdID.get(),))
                else:
                    if not delete:
                        return
                messagebox.showinfo('Deleted',f'{var_stdID.get()} student detail Successfully Deleted.')
                conn.commit()
                fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error',f'Due to {e}')
                
#reset function
    def reset():
        var_dept.set('Select Department') 
        var_course.set('Select Course')
        var_year.set('Select Year')
        var_sem.set('Select Semister')
        var_stdID.set('')
        var_stdName.set('')
        var_div.set('Select Division')
        var_rollno.set(''),
        var_gender.set('Select Gender ')
        var_dob.set('')
        var_email.set('')
        var_mobile.set('')
        var_add.set('')
        var_tsp.set('')



#generating data set
    def generate():
        if var_stdID.get()=='' or var_stdName.get()=='' or var_div.get()=='Select Division' or var_rollno.get()=='':
            messagebox.showerror('Error','All Fields are Required!!!')
        else:
            try:
                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()
                db_cursor.execute('SELECT * FROM student ')
                myresult=db_cursor.fetchall()
                id=0    
                for x in myresult:
                    id+=1
                db_cursor.execute('UPDATE student SET Department=?, Course=?, Year=?, Semister=?, Student_Name=?, Division=?,Rollno=?, Gender=?, DOB=?,Email=?, Mobile=?, Address=?,PhotoSample=? where StudentID=?',(
                    var_dept.get(), 
                    var_course.get(),
                    var_year.get(),
                    var_sem.get(),
                    var_stdName.get(),
                    var_div.get(),
                    var_rollno.get(),
                    var_gender.get(),
                    var_dob.get(),
                    var_email.get(),
                    var_mobile.get(),
                    var_add.get(),
                    var_tsp.get(),
                    var_stdID.get()==id+1,
                    ))
                conn.commit()
                fetch_data()
                # reset()
                conn.close()


                face_classifer=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifer.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimun neighbour=5
                    for(x,y,w,h) in faces:
                        

                        face_cropped=img[y:y+h,x:x+w]
                        
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path='data/user.'+var_stdID.get()+'.'+str(img_id)+'.jpg'
                        cv2.imwrite(file_name_path,face)
                        # print(var_stdID.get(),'hey')
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(123,123,123),2)
                        cv2.imshow('Cropped Face',face)
                

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                reset()
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result','Generating Data Sets completed')
            except Exception as e:
                messagebox.showerror('Error',f'Due to {e}')
            

    #main frame
    mainframe=Frame( root,bd=4,bg='#636466',relief=SUNKEN,borderwidth=3)
    mainframe.place(relx=0.0,rely=0.308,width=1365,height=485)

    #left frame
    left_frame=LabelFrame(mainframe,text='Student Registration',bd=3,fg='#9f1c33',font=('times new roman',15),borderwidth=3,relief=RAISED)
    left_frame.place(relx=0.005,rely=0.02,width=610,height=465)

    #current course
    lu_frame=LabelFrame(left_frame,text="Current Course",borderwidth=2,font=('times new roman',13),fg='#9f1c33',relief=SUNKEN)
    lu_frame.place(relx=0.01,rely=0.0,width=590,height=110)

    #department
    dep_lbl=Label(lu_frame,text="Department : ",font=('times new roman',12))
    dep_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)

    dep_cb=ttk.Combobox(lu_frame,font=('times new roman',12),state='readonly',width=17,textvariable=var_dept)
    dep_cb['values']=('Select Department','Computer','IT','Civil','Electrical','Mechnical')
    dep_cb.current(0)
    dep_cb.grid(row=0,column=1,padx=2.5,pady=7.5,sticky=W)

    #course
    course_lbl=Label(lu_frame,text="Course : ",font=('times new roman',12))
    course_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=W)

    course_cb=ttk.Combobox(lu_frame,font=('times new roman',12),state='readonly',width=17,textvariable=var_course)
    course_cb['values']=('Select Course ','FE','SE','TE','BE')
    course_cb.current(0)
    course_cb.grid(row=0,column=3,padx=2.5,pady=7.5,sticky=W)

    #year
    year_lbl=Label(lu_frame,text="Year : ",font=('times new roman',12))
    year_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)

    year_cb=ttk.Combobox(lu_frame,font=('times new roman',12),state='readonly',width=17,textvariable=var_year)
    year_cb['values']=('Select Year','2020-21','2021-22','2022-23','2023-24','2025-26')
    year_cb.current(0)
    year_cb.grid(row=1,column=1,padx=2.5,pady=7.5,sticky=W)

    #semister
    sem_lbl=Label(lu_frame,text="Semister : ",font=('times new roman',12))
    sem_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=W)

    sem_cb=ttk.Combobox(lu_frame,font=('times new roman',12),state='readonly',width=17,textvariable=var_sem)
    sem_cb['values']=('Select Semister','1','2','3','4','5','6','7','8')
    sem_cb.current(0)
    sem_cb.grid(row=1,column=3,padx=2.5,pady=7.5,sticky=W)

    #student class info
    ll_frame=LabelFrame(left_frame,text="Student Class Information",borderwidth=2,font=('times new roman',12),fg='#9f1c33',relief=SUNKEN)
    ll_frame.place(relx=0.01,rely=0.265 ,width=590,height=230)

    #studentID
    sutID_lbl=Label(ll_frame,text="StudentID no. : ",font=('times new roman',12))
    sutID_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)

    sutID_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_stdID)
    sutID_tb.grid(row=0,column=1,padx=2.5,pady=7.5,sticky=W)

    #student name
    sutname_lbl=Label(ll_frame,text="Student Name : ",font=('times new roman',12))
    sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)

    sutname_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_stdName)
    sutname_tb.grid(row=0,column=3,padx=2.5,pady=7.5,sticky=W)

    #class division
    cd_lbl=Label(ll_frame,text="Class Division : ",font=('times new roman',12))
    cd_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)

    cd_cb=ttk.Combobox(ll_frame,font=('times new roman',12),state='readonly',width=17,textvariable=var_div)
    cd_cb['values']=('Select Division','A','B','C')
    cd_cb.current(0)
    cd_cb.grid(row=1,column=1,padx=2.5,pady=7.5,sticky=W)

    #roll nno.
    Rollno_lbl=Label(ll_frame,text="Roll no.: ",font=('times new roman',12))
    Rollno_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=E)

    Rollno_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_rollno)
    Rollno_tb.grid(row=1,column=3,padx=2.5,pady=7.5)

    #gender
    gen_lbl=Label(ll_frame,text="Gender : ",font=('times new roman',12))
    gen_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)

    gen_cb=ttk.Combobox(ll_frame,font=('times new roman',12),state='readonly',width=17,textvariable=var_gender)
    gen_cb['values']=('Select Gender','Male','Female','Other')
    gen_cb.current(0)
    gen_cb.grid(row=2,column=1,padx=2.5,pady=7.5,sticky=W)

    #DOB    
    DOB_lbl=Label(ll_frame,text="DOB (dd,mm,yy): ",font=('times new roman',12))
    DOB_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)

    DOB_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_dob)
    DOB_tb.grid(row=2,column=3,padx=2.5,pady=7.5,sticky=W)

    #email
    email_lbl=Label(ll_frame,text="Email: ",font=('times new roman',12))
    email_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=W)

    email_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_email)
    email_tb.grid(row=3,column=1,padx=2.5,pady=7.5,sticky=W)

    #mobile no.
    Mobile_lbl=Label(ll_frame,text="Mobile: ",font=('times new roman',12))
    Mobile_lbl.grid(row=3,column=2,padx=2.5,pady=7.5,sticky=E)

    Mobile_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_mobile)
    Mobile_tb.grid(row=3,column=3,padx=2.5,pady=7.5,sticky=W)

    #address
    add_lbl=Label(ll_frame,text="Address: ",font=('times new roman',12))
    add_lbl.grid(row=4,column=0,padx=2.5,pady=7.5,sticky=W)

    add_tb=Entry(ll_frame,font=('times new roman',12),width=18,textvariable=var_add)
    add_tb.grid(row=4,column=1,padx=2.5,pady=7.5,sticky=W)

    #take photo sample
    tps_rad=Radiobutton(ll_frame,text='Take Photo Sample',value='Yes',variable=var_tsp)
    tps_rad.grid(row=4,column=2)
    
    #no photo sample
    nps_rad=Radiobutton(ll_frame,text='No Photo Sample',value='No',variable=var_tsp)
    nps_rad.grid(row=4,column=3)
    

    #button fram
    lbut_frame=Frame(left_frame,borderwidth=2,relief=SUNKEN)
    lbut_frame.place(relx=0.01,rely=0.8,width=590,height=40)

    llbut_frame=Frame(left_frame,borderwidth=2,relief=SUNKEN)
    llbut_frame.place(relx=0.01,rely=0.89,width=590,height=40)
    
    # save button
    save_but=Button(lbut_frame,text='Save',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=14,borderwidth=5,command=save_func)
    save_but.grid(row=0,column=0)
    
    # update button
    Update_but=Button(lbut_frame,text='Update',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=15,borderwidth=5,command=updata)
    Update_but.grid(row=0,column=1)
    
    # Delete button
    Delete_but=Button(lbut_frame,text='Delete',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=15,borderwidth=5,command=delta)
    Delete_but.grid(row=0,column=2)
    
    # Reset button
    Reset_but=Button(lbut_frame,text='Reset',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=14,borderwidth=5,command=reset)
    Reset_but.grid(row=0,column=3)

    #add photo button
    Aps_but=Button(llbut_frame,text='Add Photo Sample',font=('times new roman',12),fg='white',bg='#9f1c33',bd=6,relief=RAISED,cursor='hand2',width=31,borderwidth=5,command=generate)
    Aps_but.grid(row=0,column=0)
    
    #update photo button
    Ups_but=Button(llbut_frame,text='Update Photo Sample',font=('times new roman',12),fg='white',bg='#9f1c33',bd=7,relief=RAISED,cursor='hand2',width=31,borderwidth=5)
    Ups_but.grid(row=0,column=1)

    #right frame
    right_frame=LabelFrame(mainframe,text='Student Details',bd=3,fg='#9f1c33',font=('times new roman',15),relief=RAISED,borderwidth=3)
    right_frame.place(relx=0.46,rely=0.02,width=723,height=465)
    
    #search frame
    ru_frame=LabelFrame(right_frame,text="View Student Details & Search Stystem",borderwidth=2,font=('times new roman',13),fg='#9f1c33',relief=SUNKEN)
    ru_frame.place(relx=0.01,rely=0.0,width=690,height=80)

    search_label=Label(ru_frame,text='Search by',font=('times new roman',12))
    search_label.grid(row=0,column=0,padx=10, pady=10)

    search_cb=ttk.Combobox(ru_frame,font=('times new roman',12),state='readonly',width=17)
    search_cb['values']=('Select','StudentID no.','Roll no.','Mobile no.')
    search_cb.current(0)
    search_cb.grid(row=0,column=1,padx=10,pady=10)

    search_tb=Entry(ru_frame,font=('times new roman',12),width=17)
    search_tb.grid(row=0,column=2,padx=10,pady=10)

    search_but=Button( ru_frame,text='Search',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=8,borderwidth=3)
    search_but.grid(row=0,column=3,padx=10,pady=10)

    showall_but=Button( ru_frame,text='Show All',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=8,borderwidth=3)
    showall_but.grid(row=0,column=4,padx=5,pady=10)

    #table frame
    rl_frame=Frame(right_frame,borderwidth=2,relief=SUNKEN)
    rl_frame.place(relx=0.01,rely=0.2,width=690,height=330)

    #x scrol
    x_scrol=ttk.Scrollbar(rl_frame,orient=HORIZONTAL)
    x_scrol.pack(side=BOTTOM,fill=X)

    #y scrol
    y_scrol=ttk.Scrollbar(rl_frame,orient=VERTICAL)
    y_scrol.pack(side=RIGHT,fill=Y)

    #table
    table=ttk.Treeview(rl_frame,columns=('dep','course','year','sem','ID','name','div','roll','gender','dob','email','mob','add','photo'),xscrollcommand=x_scrol.set,yscrollcommand=y_scrol.set)

    #scrol config with table
    x_scrol.config(command= table.xview)
    y_scrol.config(command= table.yview)

    #table heading
    table.heading('dep',text='Department')
    table.heading('course',text='Course')
    table.heading('year',text='Year')
    table.heading('sem',text='Semister')
    table.heading('ID',text='ID_no.')
    table.heading('name',text='Name')
    table.heading('div',text='Division')
    table.heading('roll',text='Roll_no.')
    table.heading('gender',text='Gender')
    table.heading('dob',text='DOB')
    table.heading('email',text='Email')
    table.heading('mob',text='Mobile_no.')
    table.heading('add',text='Address')
    table.heading('photo',text='PhotoSampleStatus')
    table['show']='headings'

    table.column('dep',width=100)
    table.column('course',width=100)
    table.column('year',width=100)
    table.column('sem',width=100)
    table.column('ID',width=100)
    table.column('name',width=100)
    table.column('div',width=100)
    table.column('roll',width=100)
    table.column('gender',width=100)
    table.column('dob',width=100)
    table.column('email',width=100)
    table.column('mob',width=100)
    table.column('add',width=100)
    table.column('photo',width=100)

    table.pack(fill=BOTH,expand=1)
    table.bind('<ButtonRelease>',cursor_func)
    fetch_data()

def face_func():
    ask=messagebox.askyesno('Face Detector','Click "Yes" if want to create new atendance sheet.\n Click "No" if want to select existing Sheet',parent=root)
    if ask>0:
        name = askstring('Attendance Sheet', 'Enter Subject or Class: ')
        file_name=name+'.csv'
        open(file_name,'w')
    else:
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=root)

        
    def mark_attandance(i,r,n,d):
        
        with open(file_name,'r+',newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((','))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list)and (d not in name_list)):
                now= datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f'\n{i},{r},{n},{d},{dtString},{d1},Present')

    def draw_boundary(img,face_classifier,scaleFactor, minNeighbors,color,text,lbph):
        # print(img)
        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Priyanka",gray_image)
        features=face_classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
        coord=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=lbph.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()

                db_cursor.execute('SELECT Student_Name from student WHERE StudentID='+str(id))
                n=db_cursor.fetchone()
                n='+'.join(n)

                db_cursor.execute('SELECT Rollno from student WHERE StudentID='+str(id))
                r=db_cursor.fetchone()
                r='+'.join(r)

                db_cursor.execute('SELECT Department from student WHERE StudentID='+str(id))
                d=db_cursor.fetchone()
                d='+'.join(d)

                db_cursor.execute('SELECT StudentID from student WHERE StudentID='+str(id))
                i=db_cursor.fetchone()
                i='+'.join(i)


                if confidence >77:
                        cv2.putText(img,f"Student ID:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        mark_attandance(i,r,n,d)
                else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
        return coord

    def recognize(img,lbph,face_classifer):
        coord=draw_boundary(img,face_classifer,1.1,10,(255,255,255),'Face',lbph)
        return img

    face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    lbph=cv2.face.LBPHFaceRecognizer_create()
    lbph.read('classifier.xml')

    video_cap=cv2.VideoCapture(0)
    while True:
            ret,img=video_cap.read()
            img=recognize(img,lbph,face_classifier)
            cv2.imshow('Welcome to Face Recognition',img)

            if cv2.waitKey(1)==13:
                    break
    video_cap.release()
    cv2.destroyAllWindows() 

    



def atten_func():
    #variables
    var_Adept=StringVar()
    var_AstdID=StringVar()
    var_AstdName=StringVar()
    var_Arollno=StringVar()
    var_Atime=StringVar()
    var_Adate=StringVar()
    var_Astatus=StringVar()
    mydata=[]
    

    def fetchData(rows):
        AttendanceReportTable.delete(* AttendanceReportTable.get_children())
        for i in rows:
            AttendanceReportTable.insert("",END,values=i)
    def cursor_Atten(event):
        cursor_focus=AttendanceReportTable.focus()
        content=AttendanceReportTable.item(cursor_focus)
        data=content['values']
        
        var_AstdID.set(data[0]),
        var_Arollno.set(data[1]),
        var_AstdName.set(data[2]),
        var_Adept.set(data[3]),
        var_Atime.set(data[4]),
        var_Adate.set(data[5]),
        var_Astatus.set(data[6]),

    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=root)

    def import_csv():
        global mydata
        mydata=[]
        
        with open(fln,'r') as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            fetchData(mydata)
        
    
    def export_csv():
        try:
            if len(mydata)<1:
                messagebox.showerror('No Data',' No Data found to Export!',parent=root)
                return False
            flnex=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=root)
            with open(flnex,mode='w',newline="") as myfile:
                csvwrite=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo('Result','Data Exported to'+os.path.basename(flnex)+'Successfully ')
        except Exception as e:
                messagebox.showerror('Error',f'Due to {e}')

    def updatecsv():
            print(str(var_AstdID.get()),type(var_AstdID.get()))
            for i in mydata:
                if len(i)>0:
                    if i[0]==var_AstdID.get():
                        i[0],i[1],i[2],i[3],i[4],i[5],i[6]=var_AstdID.get(),var_Arollno.get(),var_AstdName.get(),var_Adept.get(),var_Atime.get(),var_Adate.get(),var_Astatus.get()
                        print(mydata)
            try:
                with open(fln,mode='w',newline="") as myfile:
                    csvwrite=csv.writer(myfile,delimiter=',')
                    for i in mydata:
                        csvwrite.writerow(i)
                    messagebox.showinfo('Result','File '+os.path.basename(fln)+' Updated Successfully ')
                    fetchData(mydata)
            except Exception as e:
                messagebox.showerror('Error',f'Due to {e}')

            # messagebox.showinfo('Result','Updated Successfully ')        


    def reset_csv():
        var_AstdID.set(''),
        var_Arollno.set(''),
        var_AstdName.set(''),
        var_Adept.set(''),
        var_Atime.set(''),
        var_Adate.set(''),
        var_Astatus.set(''),
        


    #nav tag
    nav_text=Label(text='Attendance',font=('times new roman',15,'bold'),bg='#636466',fg='white',width=15)
    nav_text.place(relx=0.01,rely=0.005)

    #main frame
    mainframe=Frame(bd=4,bg='#636466',relief=SUNKEN,borderwidth=3)
    mainframe.place(relx=0.0,rely=0.308,width=1365,height=485)

    #left frame
    left_frame=LabelFrame(mainframe,text='Student Attendance Details',bd=3,fg='#9f1c33',font=('times new roman',15),borderwidth=3,relief=RAISED)
    left_frame.place(relx=0.005,rely=0.02,width=610,height=465)

    #left upper frame 9321999651
    lu_frame=LabelFrame(left_frame,borderwidth=2,font=('times new roman',12),fg='#9f1c33',relief=SUNKEN)
    lu_frame.place(relx=0.01,rely=0.025 ,width=590,height=160)
    

    #AttendanceID
    sutID_lbl=Label(lu_frame,text="AttendanceID : ",font=('times new roman',12))
    sutID_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)

    sutID_tb=Entry(lu_frame,font=('times new roman',12),width=18,textvariable=var_AstdID)
    sutID_tb.grid(row=0,column=1,padx=2.5,pady=7.5,sticky=W)

    #student name
    sutname_lbl=Label(lu_frame,text="Student Name : ",font=('times new roman',12))
    sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)

    sutname_tb=Entry(lu_frame,font=('times new roman',12),width=18,textvariable=var_AstdName)
    sutname_tb.grid(row=0,column=3,padx=2.5,pady=7.5,sticky=E)

    #department
    dep_lbl=Label(lu_frame,text="Department : ",font=('times new roman',12))
    dep_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)


    dep_cb=ttk.Combobox(lu_frame,font=('times new roman',12),width=17,textvariable=var_Adept)
    dep_cb['values']=('Computer','IT','Civil','Electrical','Mechnical')
    # dep_cb.current(0)
    dep_cb.grid(row=1,column=1,padx=2.5,pady=7.5,sticky=W)
    

    #roll nno.
    Rollno_lbl=Label(lu_frame,text="Roll no.: ",font=('times new roman',12))
    Rollno_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=E)

    Rollno_tb=Entry(lu_frame,font=('times new roman',12),width=18,textvariable=var_Arollno)
    Rollno_tb.grid(row=1,column=3,padx=2.5,pady=7.5,sticky=E)

    #time
    time_lbl=Label(lu_frame,text="Time : ",font=('times new roman',12))
    time_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)

    time_cb=Entry(lu_frame,font=('times new roman',12),width=18,textvariable=var_Atime)
    time_cb.grid(row=2,column=1,padx=2.5,pady=7.5,sticky=W)

    #date
    date_lbl=Label(lu_frame,text="Date : ",font=('times new roman',12))
    date_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)

    date_tb=Entry(lu_frame,font=('times new roman',12),width=18,textvariable=var_Adate)
    date_tb.grid(row=2,column=3,padx=2.5,pady=7.5,sticky=E)

    #Attandance atatus
    a_status_lbl=Label(lu_frame,text="Attendance Status : ",font=('times new roman',12))
    a_status_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=E)

    a_status_cb=ttk.Combobox(lu_frame,font=('times new roman',12),width=17,textvariable=var_Astatus)
    a_status_cb['values']=('Present','Absent')
    a_status_cb.grid(row=3,column=1,padx=2.5,pady=7.5,sticky=E)
    # a_status_cb.current(0)


    #left middle frame
    lm_frame=Frame(left_frame,borderwidth=2,relief=SUNKEN)
    lm_frame.place(relx=0.01,rely=0.41,width=590,height=205)
    #slideshow
    img1=ImageTk.PhotoImage(Image.open("tasveer/campus4.jpeg").resize((590,205)))
    img2=ImageTk.PhotoImage(Image.open("tasveer/student-life.jpg").resize((590,205)))
    img3=ImageTk.PhotoImage(Image.open("tasveer/campus12.jpeg").resize((590,205)))
    img4=ImageTk.PhotoImage(Image.open("tasveer/Campus-1.jpg").resize((590,205)))
    img5=ImageTk.PhotoImage(Image.open("tasveer/student.jpeg").resize((590,205)))
    
    #label for slide
    l=Label(lm_frame)
    l.place(relx=0,rely=0)
    #funtion for slideshow
    # using recursion to slide to next image
    

    # function to change to next image
    def move():
        global z
        if z == 6:
            z = 1
        if z == 1:
            l.config(image=img1)
        elif z == 2:
            l.config(image=img2)
        elif z == 3:
            l.config(image=img3)
        elif z == 4:
            l.config(image=img4)
        elif z == 5:
            l.config(image=img5)
        z = z+1
        root.after(2000, move)

    # calling the function
    move()

    #left lower frame
    ll_frame=Frame(left_frame,borderwidth=2,relief=SUNKEN)
    ll_frame.place(relx=0.01,rely=0.9,width=590,height=40)
    # importcsv button
    importcsv_but=Button(ll_frame,text='Import CSV',font=('times new roman',12),fg='white', bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=5,command=import_csv)
    importcsv_but.grid(row=0,column=0,padx=2,pady=0)
    # exportcsv button
    exportcsv_but=Button(ll_frame,text='Export CSV',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=5,command=export_csv)
    exportcsv_but.grid(row=0,column=1,padx=4,pady=0)
    # update button
    Update_but=Button(ll_frame,text='Update',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=5,command=updatecsv)
    Update_but.grid(row=0,column=2,padx=4,pady=0)
    # Reset button
    Reset_but=Button(ll_frame,text='Reset',font=('times new roman',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=5,command=reset_csv)
    Reset_but.grid(row=0,column=3,padx=4,pady=0)

    #right frame
    right_frame=LabelFrame(mainframe,text='Student Details',bd=3,fg='#9f1c33',font=('times new roman',15),relief=RAISED,borderwidth=3)
    right_frame.place(relx=0.46,rely=0.02,width=723,height=465)

    #table frame
    rl_frame=Frame(right_frame,borderwidth=2,relief=SUNKEN)
    rl_frame.place(relx=0.01,rely=0.025,width=700,height=420)
    #x scrol
    x_scrol=ttk.Scrollbar(rl_frame,orient=HORIZONTAL)
    x_scrol.pack(side=BOTTOM,fill=X)

    #y scrol
    y_scrol=ttk.Scrollbar(rl_frame,orient=VERTICAL)
    y_scrol.pack(side=RIGHT,fill=Y)

     #table
    AttendanceReportTable=ttk.Treeview(rl_frame,columns=('ID','roll','name','dep','time','date','attendance'),xscrollcommand=x_scrol.set,yscrollcommand=y_scrol.set)

    #scrol config with table
    x_scrol.config(command= AttendanceReportTable.xview)
    y_scrol.config(command= AttendanceReportTable.yview)

        #table heading
    AttendanceReportTable.heading('ID',text='Attendance ID.')
    AttendanceReportTable.heading('roll',text='Roll_no.')
    AttendanceReportTable.heading('name',text='Name')
    AttendanceReportTable.heading('dep',text='Department')
    AttendanceReportTable.heading('time',text='Time')
    AttendanceReportTable.heading('date',text='Date')
    AttendanceReportTable.heading('attendance',text='Attendance')

    AttendanceReportTable['show']='headings'
    AttendanceReportTable.column('dep',width=100)
    AttendanceReportTable.column('ID',width=100)
    AttendanceReportTable.column('name',width=100)
    AttendanceReportTable.column('date',width=100)
    AttendanceReportTable.column('roll',width=100)
    AttendanceReportTable.column('time',width=100)
    AttendanceReportTable.column('attendance',width=100)
    AttendanceReportTable.pack(fill=BOTH,expand=1)
    fetchData(mydata)

    AttendanceReportTable.bind('<ButtonRelease>',cursor_Atten)

    





def train_func():
    data_dir=('data')
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    faces=[]
    ids=[]
    for image in path:
        img=Image.open(image).convert('L')
        imageNp=np.array(img,'uint8')
        id=int(os.path.split(image)[1].split('.')[1])

        faces.append(imageNp)
        ids.append(id)
        cv2.imshow('Training',imageNp)
        cv2.waitKey(1)==13
    ids=np.array(ids)


    #classifier
    lbph=cv2.face.LBPHFaceRecognizer_create()
    lbph.train(faces,ids)
    lbph.write('classifier.xml')
    cv2.destroyAllWindows()
    messagebox.showinfo('Result','Trainning Datasets Completed!!!')

        
def photo_func():
    # os.startfile('data')
    os.system(r'xdg-open  data')

def exit():
    exit=messagebox.askyesno('Face Recognition','Are you sure Exit this project',parent=root)
    if exit>0:
        root.destroy()
    else:
        return

def nav(root):
    #navigation
    nav=Label( root,bg='#636466',width=1530,height=2)
    nav.place(relx=0,rely=0)
    def time():
        str=strftime('%H:%M:%S %p')
        time_lbl.config(text=str)
        time_lbl.after(1000,time)
    #nav_button
    # Dev_but=Button( root,text='Developer',font=('times new roman',14),fg='white',bg='#636466',relief=RAISED,cursor='hand2',width=10)
    # Dev_but.place(relx=0.74,rely=0.0)
    # help_but=Button( root,text='Help Desk',font=('times new roman',14),fg='white',bg='#636466',relief=RAISED,cursor='hand2',width=10)
    # help_but.place(relx=0.82,rely=0.0)
    time_lbl=Label(root,font=('times new roman',14),fg='White',bg='#636466',width=10)
    time_lbl.place(relx=0.83,rely=0.01)
    time()
    exit_but=Button( root,text='Exit',font=('times new roman',14),fg='white',bg='#636466',relief=RAISED,cursor='hand2',width=10,command=exit)
    exit_but.place(relx=0.91,rely=0.0)
    #logo
    
    #college name
    col_name=Label( root,text='D Y Patil Institute Of Engineering and Technology',font=('times new roman',30,'bold'),bg='white')
    col_name.place(relx=0.21,rely=0.07,relwidth=0.65,relheight=0.065)
    ambi_name=Label( root,text='Ambi, Pune',font=('times new roman',20,'bold'),bg='white')
    ambi_name.place(relx=0.47,rely=0.14,relwidth=0.1,relheight=0.03)
    #subtitle
    subtitle=Label( root,text='Face Recognition System',font=('times new roman',25,'bold'),bg='white')
    subtitle.place(relx=0.39,rely=0.18)
    # #red line
    redline=Frame( root,bg='#9f1c33',width=1530,height=40)
    redline.place(relx=0,rely=0.25)
    #home
    home()
    home_but=Button( redline,text='Home',command=home,font=('times new roman',14),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=10,borderwidth=2,bd=3)
    home_but.grid(row=0,column=0,padx=55)

    sd_but=Button( redline,text='Student Details',command=student_func,font=('times new roman',14),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=10,borderwidth=2,bd=3)
    sd_but.grid(row=0,column=1,padx=55)
    # #face Recognizer
    faced_but=Button( redline,text='Face Recognizer',font=('times new roman',14),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=10,borderwidth=2,command=face_func,bd=3)
    faced_but.grid(row=0,column=3,padx=55)
    # #attendance
    atten_but=Button( redline,text='Attendance',font=('times new roman',14),fg='white',bg='#9f1c33',bd=3,relief=RAISED,cursor='hand2',width=10,borderwidth=2,command=atten_func)
    atten_but.grid(row=0,column=5,padx=55)
    # #train
    train_but=Button( redline,text='Train Data',font=('times new roman',14),fg='white',bg='#9f1c33',bd=3,relief=RAISED,cursor='hand2',width=10,borderwidth=2,command=train_func)
    train_but.grid(row=0,column=7,padx=55)
    # #Photos
    photo_but=Button( redline,text='Photos',font=('times new roman',14),command=photo_func,fg='white',bd=3,bg='#9f1c33',relief=RAISED,cursor='hand2',width=10,borderwidth=2)
    photo_but.grid(row=0,column=9,padx=55)

if __name__=='__main__':
    root=Tk()
    root.geometry('1365x705+0+0')
    root.title('Face Recognition System')
    root.configure(bg='white')
    root.resizable(False,False)
    logo=ImageTk.PhotoImage(Image.open("tasveer/Logo.jpg"))
    logo_lable=Label( root,image=logo,border=0,borderwidth=0,cursor='hand2')
    logo_lable.place(relx=0.02,rely=0.07,relwidth=0.18,relheight=0.14)
    logo_lable.bind('<Button-1>', lambda x: webbrowser.open_new('https://dypatiluniversitypune.edu.in/school-of-engineering-ambi.php'))
    z=1
    nav(root)
    

    root.mainloop()
