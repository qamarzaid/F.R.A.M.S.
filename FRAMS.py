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
import platform
from tkcalendar import DateEntry
z=1
def main():
    root=Toplevel(auth)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_width,screen_height)
    root.geometry(f'{screen_width}x725')
    root.iconbitmap(r'C:\Users\zaid\Desktop\FRAMS\fram_icon.ico')
    root.title('F.R.A.M.S')
    root.configure(bg='white')
    root.resizable(False,False)
    logo=ImageTk.PhotoImage(Image.open("tasveer/Logo.jpg"))
    logo_lable=Label( root,image=logo,border=0,borderwidth=0,cursor='hand2')
    logo_lable.place(relx=0.02,rely=0.09,relwidth=0.18,relheight=0.12)
    logo_lable.bind('<Button-1>', lambda x: webbrowser.open_new('https://dypatiluniversitypune.edu.in/school-of-engineering-ambi.php'))
    def home(root=root):
        nav=Frame( root,bg='#636466',width=1100,height=35)
        nav.place(relx=0,rely=0)
        nav_text=Label(nav,text='> Home',font=('Tw Cen MT',14),bg='#636466',fg='white')
        nav_text.place(relx=0.01,rely=0.05)
            #slideshow
        img1=ImageTk.PhotoImage(Image.open("tasveer/campus4.jpeg").resize((1365,480)))
        img2=ImageTk.PhotoImage(Image.open("tasveer/student-life.jpg").resize((1365,480)))
        img3=ImageTk.PhotoImage(Image.open("tasveer/campus12.jpeg").resize((1365,480)))
        img4=ImageTk.PhotoImage(Image.open("tasveer/Campus-1.jpg").resize((1365,480)))
        img5=ImageTk.PhotoImage(Image.open("tasveer/student.jpeg").resize((1365,480)))
        
        #label for slide
        l=Label(root)
        l.place(relx=0,rely=0.3)
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

    def student_func(root=root):
        nav=Frame( root,bg='#636466',width=1100,height=35)
        nav.place(relx=0,rely=0)
        nav_text=Label(nav,text='> Student Detail',font=('Tw Cen MT',14),bg='#636466',fg='white')
        nav_text.place(relx=0.01,rely=0.05)
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
        var_searchcb=StringVar()
        var_searchtb=StringVar()
        
        try:
            conn=sqlite3.connect('Student_DB.db')
            db_cursor=conn.cursor()
            db_cursor.execute('SELECT * FROM student')
            Data=db_cursor.fetchall()
            var_stdID.set(str(len(Data)+1))
            var_rollno.set(str(100+len(Data)+1))
            var_tsp.set('No')
                    #bol(f'Error, Due to {e}')
        except:
            pass
            
        def validate():
            if var_dept.get()=='Select Department' or var_course.get()=='Select Course' or var_year.get()=='Select Year' or var_sem.get()=='Select Semister' or var_stdName.get()=='' or var_div.get()=='Select Division' or var_gender.get()=='Select Gender' or var_dob.get()=='' or var_email.get()[-4:]!='.com' or var_email.get()=='' or len(var_mobile.get())!=10 or var_mobile=='' or var_add.get()=='' :

                if var_dept.get()=='Select Department':
                    dep_lbl=Label(lu_frame,text="Department : ",font=('Tw Cen MT',12),fg='red')
                    dep_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)
                else:
                    dep_lbl=Label(lu_frame,text="Department : ",font=('Tw Cen MT',12,))
                    dep_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)
                    
                if var_course.get()=='Select Course':
                    course_lbl=Label(lu_frame,text="Course : ",font=('Tw Cen MT',12),fg='red')
                    course_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=W)
                else:
                    course_lbl=Label(lu_frame,text="Course : ",font=('Tw Cen MT',12))
                    course_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=W)

                if var_year.get()=='Select Year':
                    year_lbl=Label(lu_frame,text="Year : ",font=('Tw Cen MT',12),fg='red')
                    year_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)
                else:
                    year_lbl=Label(lu_frame,text="Year : ",font=('Tw Cen MT',12))
                    year_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)

                if var_sem.get()=='Select Semister':
                    sem_lbl=Label(lu_frame,text="Semister : ",font=('Tw Cen MT',12),fg='red')
                    sem_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=W)
                else:
                    sem_lbl=Label(lu_frame,text="Semister : ",font=('Tw Cen MT',12))
                    sem_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=W)

                if var_stdName.get()=='':
                    sutname_lbl=Label(ll_frame,text="Student Name : ",font=('Tw Cen MT',12),fg='red')
                    sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)
                else:
                    sutname_lbl=Label(ll_frame,text="Student Name : ",font=('Tw Cen MT',12))
                    sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)

                if var_div.get()=='Select Division':
                    cd_lbl=Label(ll_frame,text="Class Division : ",font=('Tw Cen MT',12),fg='red')
                    cd_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)
                else:
                    cd_lbl=Label(ll_frame,text="Class Division : ",font=('Tw Cen MT',12))
                    cd_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)

                if var_gender.get()=='Select Gender':
                    gen_lbl=Label(ll_frame,text="Gender : ",font=('Tw Cen MT',12),fg='red')
                    gen_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)
                else:
                    gen_lbl=Label(ll_frame,text="Gender : ",font=('Tw Cen MT',12))
                    gen_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)

                if var_dob.get()=='':
                    DOB_lbl=Label(ll_frame,text="DOB (dd/mm/yy): ",font=('Tw Cen MT',12),fg='red')
                    DOB_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)
                else:
                    DOB_lbl=Label(ll_frame,text="DOB (dd/mm/yy): ",font=('Tw Cen MT',12))

                    DOB_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)

                if var_email.get()[-4:]!='.com' or var_email.get()=='':
                    email_lbl=Label(ll_frame,text="Email: ",font=('Tw Cen MT',12),fg='red')
                    email_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=W)
                else:
                    email_lbl=Label(ll_frame,text="Email: ",font=('Tw Cen MT',12))
                    email_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=W)

                if len(var_mobile.get())!=10 or var_mobile=='':
                    Mobile_lbl=Label(ll_frame,text="Mobile: ",font=('Tw Cen MT',12),fg='red')
                    Mobile_lbl.grid(row=3,column=2,padx=2.5,pady=7.5,sticky=E)
                else:
                    Mobile_lbl=Label(ll_frame,text="Mobile: ",font=('Tw Cen MT',12))
                    Mobile_lbl.grid(row=3,column=2,padx=2.5,pady=7.5,sticky=E)

                if var_add.get()=='':
                    add_lbl=Label(ll_frame,text="Address: ",font=('Tw Cen MT',12),fg='red')
                    add_lbl.grid(row=4,column=0,padx=2.5,pady=7.5,sticky=W)
                else:
                    add_lbl=Label(ll_frame,text="Address: ",font=('Tw Cen MT',12))
                    add_lbl.grid(row=4,column=0,padx=2.5,pady=7.5,sticky=W)
    
                messagebox.showerror('Error','Please Enter Highlighted Field Accuratety')
                       
            else:
                dep_lbl=Label(lu_frame,text="Department : ",font=('Tw Cen MT',12,))
                dep_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)
                course_lbl=Label(lu_frame,text="Course : ",font=('Tw Cen MT',12))
                course_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=W)
                year_lbl=Label(lu_frame,text="Year : ",font=('Tw Cen MT',12))
                year_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)
                sem_lbl=Label(lu_frame,text="Semister : ",font=('Tw Cen MT',12))
                sem_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=W)
                sutname_lbl=Label(ll_frame,text="Student Name : ",font=('Tw Cen MT',12))
                sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)
                cd_lbl=Label(ll_frame,text="Class Division : ",font=('Tw Cen MT',12))
                cd_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)
                gen_lbl=Label(ll_frame,text="Gender : ",font=('Tw Cen MT',12))
                gen_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)
                DOB_lbl=Label(ll_frame,text="DOB (dd/mm/yy): ",font=('Tw Cen MT',12))
                DOB_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)
                email_lbl=Label(ll_frame,text="Email: ",font=('Tw Cen MT',12))
                email_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=W)
                Mobile_lbl=Label(ll_frame,text="Mobile: ",font=('Tw Cen MT',12))
                Mobile_lbl.grid(row=3,column=2,padx=2.5,pady=7.5,sticky=E)
                add_lbl=Label(ll_frame,text="Address: ",font=('Tw Cen MT',12))
                add_lbl.grid(row=4,column=0,padx=2.5,pady=7.5,sticky=W)
                register_func()
            
        def register_func():    
                if var_stdID.get()=='' or var_stdName.get()==''  or var_rollno.get()=='':
                    messagebox.showerror('Error','StudentID, Student Name, Roll no. id required!!!')
                else:
                    try:
                        conn=sqlite3.connect('Student_DB.db')
                        db_cursor=conn.cursor()
                        db_cursor.execute(' INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(   var_dept.get(), 
                            var_course.get(),
                            var_year.get(),
                            var_sem.get(),
                            var_stdID.get(),
                            var_stdName.get().title(),
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
            var_searchcb.set('Select')
            var_searchtb.set('')
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
            if var_stdID.get()=='' or var_stdName.get()==''  or var_rollno.get()=='':
                    messagebox.showerror('Error','StudentID, Student Name, Roll no. id required!!!')      
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
                    messagebox.showinfo('Updated',f'Student details of {var_stdID.get()} Updated Successfully .')
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

                    if os.path.isfile('data/user.'+var_stdID.get()+'.1.jpg'):
                        for i in range(1,101):
                            file = 'data/user.'+var_stdID.get()+'.'+str(i)+'.jpg'
                            os.remove(file)
                            messagebox.showinfo('Deleted',f'Student details of {var_stdID.get()}  Deleted Successfully.')
                    conn.commit()
                    fetch_data()
                    conn.close()
                except Exception as e:
                    messagebox.showerror('Error',f'Due to {e}')
                    
    #reset function
        def reset():
            try:
                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()
                db_cursor.execute('SELECT * FROM student')
                Data=db_cursor.fetchall()
                var_stdID.set(str(len(Data)+1))
                var_rollno.set(str(100+len(Data)+1))
            except:
                pass
            var_dept.set('Select Department') 
            var_course.set('Select Course')
            var_year.set('Select Year')
            var_sem.set('Select Semister')
            var_stdID.set(str(len(Data)+1))
            var_stdName.set('')
            var_div.set('Select Division')
            var_rollno.set(str(100+len(Data)+1)),
            var_gender.set('Select Gender ')
            var_dob.set('')
            var_email.set('')
            var_mobile.set('')
            var_add.set('')
            var_tsp.set('No')

        def generate_photo():
            conn=sqlite3.connect('Student_DB.db')
            db_cursor=conn.cursor()
            db_cursor.execute('UPDATE student SET PhotoSample = "Yes" WHERE StudentID=? ',(var_stdID.get()))
            conn.commit()
            fetch_data()
            conn.close()

            face_classifer=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifer.detectMultiScale(gray,1.3,5)
                for(x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w]                 
                    return face_cropped

            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,myframe=cap.read()
                if face_cropped(myframe) is not None:
                    img_id+=1
                    Face=cv2.resize(face_cropped(myframe),(450,450))
                    face=cv2.cvtColor(Face,cv2.COLOR_BGR2GRAY)
                    file_name_path='data/user.'+var_stdID.get()+'.'+str(img_id)+'.jpg'
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(Face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(123,123,123),2)
                    cv2.imshow('Cropped Face',Face)

                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
            reset()
            cap.release()
            cv2.destroyAllWindows()

        def add_photo():
            if var_stdID.get()=='' or var_stdName.get()==''  or var_rollno.get()=='':
                    messagebox.showerror('Error','StudentID, Student Name, Roll no. id required!!!')
            else:
                try:
                    generate_photo()
                    messagebox.showinfo('Result','Generating Data Sets completed')
                except Exception as e:
                    messagebox.showerror('Error',f'Due to {e}')
        
        def update_photo():
            if var_stdID.get()=='' or var_stdName.get()==''  or var_rollno.get()=='':
                    messagebox.showerror('Error','StudentID, Student Name, Roll no. id required!!!')                    
            else:
                try:
                    for i in range(1,101):
                        file = 'data/user.'+var_stdID.get()+'.'+str(i)+'.jpg'
                        os.remove(file)
                    generate_photo()
                    messagebox.showinfo('Result','Data Sets Updated Successfully')
                except Exception as e:
                    messagebox.showerror('Error',f'Due to {e}')

        def search():
            if var_searchcb.get()=='Select':
                search_label=Label(ru_frame,text='Search by',font=('Tw Cen MT',12),fg='red')
                search_label.grid(row=0,column=0,padx=10, pady=10)
                messagebox.showerror('Error','All Fields are Required!!!')
            else:
                search_label=Label(ru_frame,text='Search by',font=('Tw Cen MT',12))
                search_label.grid(row=0,column=0,padx=10, pady=10)
                try:
                    conn=sqlite3.connect('Student_DB.db')
                    db_cursor=conn.cursor()
                    if var_searchcb.get()=='StudentID no.':
                        db_cursor.execute("SELECT * FROM student WHERE StudentID=?",(   var_searchtb.get(), ))
                    elif var_searchcb.get()=='Roll no.':
                        db_cursor.execute("SELECT * FROM student WHERE Rollno=?",(   var_searchtb.get(), ))
                    elif var_searchcb.get()=='Mobile no.':
                        db_cursor.execute("SELECT * FROM student WHERE Mobile=?",(   var_searchtb.get(), ))
                    else:
                        return
                    Data=db_cursor.fetchall()
                    if len(Data)!=0:
                        table.delete(* table.get_children())
                        for i in Data:
                            table.insert('',END,values=i)
                        conn.commit()
                        conn.close()
                    else:
                        messagebox.showerror('Error','Given '+var_searchcb.get()+': '+ var_searchtb.get()+' is not found')

                except Exception as e:
                    messagebox.showerror('Error',f'Due to {e}')
                
        #main frame
        mainframe=Frame( root,bd=4,bg='#636466',relief=SUNKEN,borderwidth=3)
        mainframe.place(relx=0.0,rely=0.3,width=1365,height=485)

        #left frame
        left_frame=LabelFrame(mainframe,text='Student Registration',bd=3,fg='#9f1c33',font=('Tw Cen MT',15),borderwidth=3,relief=RAISED)
        left_frame.place(relx=0.007,rely=0.01,width=610,height=465)

        #current course
        lu_frame=LabelFrame(left_frame,text="Current Course",borderwidth=2,font=('Tw Cen MT',13),fg='#9f1c33',relief=SUNKEN)
        lu_frame.place(relx=0.01,rely=0.0,width=590,height=105)

        #department
        dep_lbl=Label(lu_frame,text="Department : ",font=('Tw Cen MT',12))
        dep_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)

        dep_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_dept)
        dep_cb['values']=('Select Department','Computer','IT','Civil','Electrical','Mechnical')
        dep_cb.current(0)
        dep_cb.grid(row=0,column=1,padx=2.5,pady=7.5,sticky=W)

        #course
        course_lbl=Label(lu_frame,text="Course : ",font=('Tw Cen MT',12))
        course_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=W)

        course_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_course)
        course_cb['values']=('Select Course','FE','SE','TE','BE')
        course_cb.current(0)
        course_cb.grid(row=0,column=3,padx=2.5,pady=7.5,sticky=W)

        #year
        year_lbl=Label(lu_frame,text="Year : ",font=('Tw Cen MT',12))
        year_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)

        year_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_year)
        year_cb['values']=('Select Year','2020-21','2021-22','2022-23','2023-24','2025-26')
        year_cb.current(0)
        year_cb.grid(row=1,column=1,padx=2.5,pady=7.5,sticky=W)

        #semister
        sem_lbl=Label(lu_frame,text="Semister : ",font=('Tw Cen MT',12))
        sem_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=W)

        sem_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_sem)
        sem_cb['values']=('Select Semister','1','2','3','4','5','6','7','8')
        sem_cb.current(0)
        sem_cb.grid(row=1,column=3,padx=2.5,pady=7.5,sticky=W)

        #student class info
        ll_frame=LabelFrame(left_frame,text="Student Class Information",borderwidth=2,font=('Tw Cen MT',12),fg='#9f1c33',relief=SUNKEN)
        ll_frame.place(relx=0.01,rely=0.24 ,width=590,height=230)

        #studentID
        sutID_lbl=Label(ll_frame,text="StudentID no. : ",font=('Tw Cen MT',12))
        sutID_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)

        sutID_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_stdID)
        sutID_tb.grid(row=0,column=1,padx=2.5,pady=7.5,sticky=W)

        #student name
        sutname_lbl=Label(ll_frame,text="Student Name : ",font=('Tw Cen MT',12))
        sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)

        sutname_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_stdName)
        sutname_tb.grid(row=0,column=3,padx=2.5,pady=7.5,sticky=W)

        #class division
        cd_lbl=Label(ll_frame,text="Class Division : ",font=('Tw Cen MT',12))
        cd_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)

        cd_cb=ttk.Combobox(ll_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_div)
        cd_cb['values']=('Select Division','A','B','C')
        cd_cb.current(0)
        cd_cb.grid(row=1,column=1,padx=2.5,pady=7.5,sticky=W)

        #roll nno.
        Rollno_lbl=Label(ll_frame,text="Roll no.: ",font=('Tw Cen MT',12))
        Rollno_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=E)

        Rollno_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_rollno)
        Rollno_tb.grid(row=1,column=3,padx=2.5,pady=7.5,sticky=W)

        #gender
        gen_lbl=Label(ll_frame,text="Gender : ",font=('Tw Cen MT',12))
        gen_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)

        gen_cb=ttk.Combobox(ll_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_gender)
        gen_cb['values']=('Select Gender','Male','Female','Other')
        gen_cb.current(0)
        gen_cb.grid(row=2,column=1,padx=2.5,pady=7.5,sticky=W)

        #DOB    
        DOB_lbl=Label(ll_frame,text="DOB : ",font=('Tw Cen MT',12))
        DOB_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)

        # DOB_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_dob)
        DOB_tb=DateEntry(ll_frame,selectmode='day',font=('Tw Cen MT',12),width=14,textvariable=var_dob)

        DOB_tb.grid(row=2,column=3,padx=2.5,pady=7.5)

        #email
        email_lbl=Label(ll_frame,text="Email: ",font=('Tw Cen MT',12))
        email_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=W)

        email_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_email)
        email_tb.grid(row=3,column=1,padx=2.5,pady=7.5,sticky=W)

        #mobile no.
        Mobile_lbl=Label(ll_frame,text="Mobile: ",font=('Tw Cen MT',12))
        Mobile_lbl.grid(row=3,column=2,padx=2.5,pady=7.5,sticky=E)

        Mobile_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_mobile)
        Mobile_tb.grid(row=3,column=3,padx=2.5,pady=7.5,sticky=W)

        #address
        add_lbl=Label(ll_frame,text="Address: ",font=('Tw Cen MT',12))
        add_lbl.grid(row=4,column=0,padx=2.5,pady=7.5,sticky=W)

        add_tb=Entry(ll_frame,font=('Tw Cen MT',12),width=16,textvariable=var_add)
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
        
        # register button
        register_but=Button(lbut_frame,text='Register',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=16,borderwidth=5,command=validate)
        register_but.place(relx=0.0,rely=0.0)
        
        # update button
        Update_but=Button(lbut_frame,text='Update',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=16,borderwidth=5,command=updata)
        Update_but.place(relx=0.25,rely=0.0)
        
        # Delete button
        Delete_but=Button(lbut_frame,text='Delete',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=16,borderwidth=5,command=delta)
        Delete_but.place(relx=0.5,rely=0.0)
        
        # Reset button
        Reset_but=Button(lbut_frame,text='Reset',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=16,borderwidth=5,command=reset)
        Reset_but.place(relx=0.75,rely=0.0)

        #add photo button
        Aps_but=Button(llbut_frame,text='Add Photo Sample',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=34,borderwidth=6,command=add_photo)
        Aps_but.place(relx=0.0,rely=0.0)
        
        #update photo button
        Ups_but=Button(llbut_frame,text='Update Photo Sample',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=34,borderwidth=6,command=update_photo)
        Ups_but.place(relx=0.5,rely=0.0)

        #right frame
        right_frame=LabelFrame(mainframe,text='Student Details',bd=3,fg='#9f1c33',font=('Tw Cen MT',15),relief=RAISED,borderwidth=3)
        right_frame.place(relx=0.462,rely=0.01,width=723,height=465)
        
        #search frame
        ru_frame=LabelFrame(right_frame,text="View Student Details & Search Stystem",borderwidth=2,font=('Tw Cen MT',13),fg='#9f1c33',relief=SUNKEN)
        ru_frame.place(relx=0.01,rely=0.0,width=700,height=80)

        search_label=Label(ru_frame,text='Search by',font=('Tw Cen MT',12))
        search_label.grid(row=0,column=0,padx=10, pady=10)

        search_cb=ttk.Combobox(ru_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_searchcb)
        search_cb['values']=('Select','StudentID no.','Roll no.','Mobile no.')
        search_cb.current(0)
        search_cb.grid(row=0,column=1,padx=10,pady=10)

        search_tb=Entry(ru_frame,font=('Tw Cen MT',12),width=14,textvariable=var_searchtb)
        search_tb.grid(row=0,column=2,padx=10,pady=10)

        search_but=Button( ru_frame,text='Search',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=8,borderwidth=3,command=search)
        search_but.grid(row=0,column=3,padx=10,pady=10)

        showall_but=Button( ru_frame,text='Show All',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=8,borderwidth=3,command=fetch_data)
        showall_but.grid(row=0,column=4,padx=5,pady=10)

        #table frame
        rl_frame=Frame(right_frame,borderwidth=2,relief=SUNKEN)
        rl_frame.place(relx=0.01,rely=0.2,width=700,height=340)

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

    def face_func(root=root):
        #bol('Click ,Yes ,if want to create new atendance sheet. else . Click , "No", if want to select existing Sheet')
        ask=messagebox.askyesno('Face Detector','Click "Yes" if want to create new atendance sheet.\n Click "No" if want to select existing Sheet',parent=root)
        if ask==True:
            try:
                name = askstring('Attendance Sheet', 'Enter Subject or Class: ')
                file_name=f'Attendance Sheets/{name}.csv'
                open(file_name,'w')
            except Exception as e:
                #bol('Please Try again and Select file.')
                messagebox.showwarning('Alert!!!','Please Try again and Select file.')
                home()
                return
            
        else:
            file_name=filedialog.askopenfilename(initialdir='Attendance Sheets',title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=root)

        if len(file_name)>0:

            
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
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
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
            lbph.read('lbph_data.xml')

            video_cap=cv2.VideoCapture(0)
            while True:
                    ret,img=video_cap.read()
                    img=recognize(img,lbph,face_classifier)
                    cv2.imshow('Welcome to Face Recognition',img)

                    if cv2.waitKey(1)==13:
                            break
            video_cap.release()
            cv2.destroyAllWindows() 
        else:
            #bol('Please Try again and Select file.')
            messagebox.showwarning('Alert!!!','Please Try again and Select file.')
            home()
            
    def atten_func(root=root):
        
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

        fln=filedialog.askopenfilename(initialdir='Attendance Sheets',title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=root)
        if len(fln)>0:

            def export_csv():
                try:
                    if len(mydata)<1:
                        #bol(' No Data found to Export')
                        messagebox.showerror('No Data',' No Data found to Export!',parent=root)
                        return False
                    flnex=filedialog.asksaveasfilename(initialdir='Attendance Sheets',title="Open CSV",filetypes=(('CSV File','*.csv'),("All File","*.*")),parent=root)
                    with open(flnex,mode='w',newline="") as myfile:
                        csvwrite=csv.writer(myfile,delimiter=',')
                        for i in mydata:
                            csvwrite.writerow(i)
                        #bol('Data Exported to ,'+os.path.basename(flnex)+' ,Successfully ')
                        messagebox.showinfo('Result','Data Exported to '+os.path.basename(flnex)+' Successfully ')
                except Exception as e:
                        #bol(f'Error,Due to {e}')
                        messagebox.showerror('Error',f'Due to {e}')

            def updatecsv():
                    for i in mydata:
                        if len(i)>0:
                            if i[0]==var_AstdID.get():
                                i[0],i[1],i[2],i[3],i[4],i[5],i[6]=var_AstdID.get(),var_Arollno.get(),var_AstdName.get(),var_Adept.get(),var_Atime.get(),var_Adate.get(),var_Astatus.get()

                    try:
                        with open(fln,mode='w',newline="") as myfile:
                            csvwrite=csv.writer(myfile,delimiter=',')
                            for i in mydata:
                                csvwrite.writerow(i)
                            #bol('File ,'+os.path.basename(fln)+' ,Updated Successfully ')
                            messagebox.showinfo('Result','File '+os.path.basename(fln)+' Updated Successfully ')
                            fetchData(mydata)

                    except Exception as e:
                        #bol(f'Error,Due to {e}')

                        messagebox.showerror('Error',f'Due to {e}')

        


            def reset_csv():
                var_AstdID.set(''),
                var_Arollno.set(''),
                var_AstdName.set(''),
                var_Adept.set(''),
                var_Atime.set(''),
                var_Adate.set(''),
                var_Astatus.set('')
            nav=Frame( root,bg='#636466',width=1100,height=35)
            nav.place(relx=0,rely=0)
            nav_text=Label(nav,text='> Attendance',font=('Tw Cen MT',14),bg='#636466',fg='white')
            nav_text.place(relx=0.01,rely=0.05)
            

            #main frame
            mainframe=Frame(root,bd=4,bg='#636466',relief=SUNKEN,borderwidth=3)
            mainframe.place(relx=0.0,rely=0.3,width=1365,height=485)

            #left frame
            left_frame=LabelFrame(mainframe,text='Student Attendance Details',bd=3,fg='#9f1c33',font=('Tw Cen MT',15),borderwidth=3,relief=RAISED)
            left_frame.place(relx=0.007,rely=0.01,width=610,height=465)

            #left upper frame 9321999651
            lu_frame=LabelFrame(left_frame,borderwidth=2,font=('Tw Cen MT',12),fg='#9f1c33',relief=SUNKEN)
            lu_frame.place(relx=0.01,rely=0.025 ,width=590,height=160)
            

            #AttendanceID
            sutID_lbl=Label(lu_frame,text="AttendanceID : ",font=('Tw Cen MT',12))
            sutID_lbl.grid(row=0,column=0,padx=2.5,pady=7.5,sticky=W)

            sutID_tb=Entry(lu_frame,font=('Tw Cen MT',12),width=16,textvariable=var_AstdID)
            sutID_tb.grid(row=0,column=1,padx=2.5,pady=7.5,sticky=W)

            #student name
            sutname_lbl=Label(lu_frame,text="Student Name : ",font=('Tw Cen MT',12))
            sutname_lbl.grid(row=0,column=2,padx=2.5,pady=7.5,sticky=E)

            sutname_tb=Entry(lu_frame,font=('Tw Cen MT',12),width=16,textvariable=var_AstdName)
            sutname_tb.grid(row=0,column=3,padx=2.5,pady=7.5,sticky=E)

            #department
            dep_lbl=Label(lu_frame,text="Department : ",font=('Tw Cen MT',12))
            dep_lbl.grid(row=1,column=0,padx=2.5,pady=7.5,sticky=W)


            dep_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_Adept)
            dep_cb['values']=('Select Department','Computer','IT','Civil','Electrical','Mechnical')
            dep_cb.current(0)
            dep_cb.grid(row=1,column=1,padx=2.5,pady=7.5,sticky=W)
            

            #roll nno.
            Rollno_lbl=Label(lu_frame,text="Roll no.: ",font=('Tw Cen MT',12))
            Rollno_lbl.grid(row=1,column=2,padx=2.5,pady=7.5,sticky=E)

            Rollno_tb=Entry(lu_frame,font=('Tw Cen MT',12),width=16,textvariable=var_Arollno)
            Rollno_tb.grid(row=1,column=3,padx=2.5,pady=7.5)

            #time
            time_lbl=Label(lu_frame,text="Time : ",font=('Tw Cen MT',12))
            time_lbl.grid(row=2,column=0,padx=2.5,pady=7.5,sticky=W)

            time_cb=Entry(lu_frame,font=('Tw Cen MT',12),width=16,textvariable=var_Atime)
            time_cb.grid(row=2,column=1,padx=2.5,pady=7.5,sticky=W)

            #date
            date_lbl=Label(lu_frame,text="Date : ",font=('Tw Cen MT',12))
            date_lbl.grid(row=2,column=2,padx=2.5,pady=7.5,sticky=E)

            date_tb=Entry(lu_frame,font=('Tw Cen MT',12),width=16,textvariable=var_Adate)
            date_tb.grid(row=2,column=3,padx=2.5,pady=7.5,sticky=E)

            #Attandance atatus
            a_status_lbl=Label(lu_frame,text="Attendance Status : ",font=('Tw Cen MT',12))
            a_status_lbl.grid(row=3,column=0,padx=2.5,pady=7.5,sticky=E)

            a_status_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',12),state='readonly',width=14,textvariable=var_Astatus)
            a_status_cb['values']=('Select','Present','Absent')
            a_status_cb.grid(row=3,column=1,padx=2.5,pady=7.5,sticky=E)
            a_status_cb.current(0)


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
            
            # exportcsv button
            exportcsv_but=Button(ll_frame,text='Export CSV',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=22,borderwidth=6,command=export_csv)
            exportcsv_but.grid(row=0,column=2,padx=0,pady=0)
            # update button
            Update_but=Button(ll_frame,text='Update',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=22,borderwidth=6,command=updatecsv)
            Update_but.grid(row=0,column=0,padx=0,pady=0)
            # Reset button
            Reset_but=Button(ll_frame,text='Reset',font=('Tw Cen MT',12),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=22,borderwidth=6,command=reset_csv)
            Reset_but.grid(row=0,column=1,padx=0,pady=0)

            #right frame
            right_frame=LabelFrame(mainframe,text='Attendance Sheet',bd=3,fg='#9f1c33',font=('Tw Cen MT',15),relief=RAISED,borderwidth=3)
            right_frame.place(relx=0.462,rely=0.01,width=723,height=465)

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
            # fetchData(mydata)
            # import_csv()
            mydata=[]
                
            with open(fln,'r') as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                fetchData(mydata)
            AttendanceReportTable.bind('<ButtonRelease>',cursor_Atten)
        else:
            #bol('Please Try again and Select file.')
            messagebox.showwarning('Alert!!!','Please Try again and Select file.')
            home()

    def train_func(root=root):
        data_dir=('data')
        if len(os.listdir(data_dir))>0:

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
            lbph.write('lbph_data.xml')
            cv2.destroyAllWindows()
            #bol('Trainning Datasets Completed')
            messagebox.showinfo('Result','Trainning Datasets Completed.')
        else:
            messagebox.showwarning('Alert!!!','Not Data Found for Training.')
            
            student_func()
            messagebox.showinfo('Generate Data','Please Register Student and Add Photo Samples')


        
    def photo_func(root=root):
        if platform.system()=='Linux':
            os.system(r'xdg-open  data')
        else:
            os.startfile('data')
            

    def exit(root=root):
        #bol('Are you sure to Exit FRAMS? ')
        exit=messagebox.askyesno('Face Recognition','Are you sure to Exit FRAMS? ',parent=root)
        if exit>0:
            root.destroy()
            auth.destroy()
        else:
            return

    def nav(root=root):
        #navigation
        # nav=Frame( root,bg='#636466',width=1430,height=2)
        # nav.place(relx=0,rely=0)
        nav=Frame( root,bg='#636466',width=1366,height=35)
        nav.place(relx=0,rely=0)
        def time():
            str=strftime('%H:%M:%S %p')
            time_lbl.config(text=str)
            time_lbl.after(1000,time)

        time_lbl=Label(nav,font=('Tw Cen MT',13),fg='White',bg='#636466',width=12,)
        time_lbl.place(relx=0.83,rely=0.15)
        time()
        exit_but=Button( nav,text='Exit',font=('Tw Cen MT',13),fg='white',bg='#636466',relief=RAISED,cursor='hand2',width=10,command=exit)
        exit_but.place(relx=0.91,rely=0.0)
        #logo
        
        #college name
        col_name=Label( root,text='D Y Patil Institute Of Engineering and Technology',font=('Tw Cen MT',30,'bold'),bg='white')
        col_name.place(relx=0.21,rely=0.08,relwidth=0.65,relheight=0.065)
        ambi_name=Label( root,text='Pune, Ambi',font=('Tw Cen MT',15,'bold'),bg='white')
        ambi_name.place(relx=0.833,rely=0.1,relwidth=0.1,relheight=0.03)
        #subtitle
        subtitle=Label( root,text='F . R . A . M . S',font=('Tw Cen MT',25,'bold'),bg='white')
        subtitle.place(relx=0.34,rely=0.143)
        subtitle=Label( root,text='Face Recognition Anttendance Management System',font=('Tw Cen MT',15,'bold'),bg='white')
        subtitle.place(relx=0.51,rely=0.16)
        # #red line
        redline=Frame( root,bg='#9f1c33',width=screen_width,height=40)
        redline.place(relx=0,rely=0.248)
        #home
        home(root)

        # home_but=Button( redline,text='Home',command=home,font=('Tw Cen MT',14),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=10,borderwidth=2,bd=3,highlightcolor='#636466',highlightthickness=1)
        # home_but.grid(row=0,column=0,padx=35)
        # # home_but.place(relx=)

        sd_but=Button( redline,text='Student Details',command=student_func,font=('Tw Cen MT',14),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=2,bd=3,highlightcolor="#636466",highlightthickness=1)
        # sd_but.grid(row=0,column=1,padx=55)
        sd_but.place(relx=0.05,rely=0)
        # #face Recognizer
        faced_but=Button( redline,text='Face Recognizer',font=('Tw Cen MT',14),fg='white',bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=2,command=face_func,bd=3,highlightcolor="#636466",highlightthickness=1)
        faced_but.place(relx=0.25,rely=0)
        # #attendance
        atten_but=Button( redline,text='Attendance',font=('Tw Cen MT',14),fg='white',bg='#9f1c33',bd=3,relief=RAISED,cursor='hand2',width=13,borderwidth=2,command=atten_func,highlightcolor="#636466",highlightthickness=1)
        atten_but.place(relx=0.45,rely=0)
        # #train
        train_but=Button( redline,text='Train Data',font=('Tw Cen MT',14),fg='white',bg='#9f1c33',bd=3,relief=RAISED,cursor='hand2',width=13,borderwidth=2,command=train_func,highlightcolor="#636466",highlightthickness=1)
        train_but.place(relx=0.65,rely=0)
        # #Photos
        photo_but=Button( redline,text='Photos',font=('Tw Cen MT',14),command=photo_func,fg='white',bd=3,bg='#9f1c33',relief=RAISED,cursor='hand2',width=13,borderwidth=2,highlightcolor="#636466",highlightthickness=1)
        photo_but.place(relx=0.85,rely=0)
        messagebox.showinfo('Successful','Loged In Successfully')

    def disable_close():
        pass

    nav(root)
    root.protocol('WM_DELETE_WINDOW',disable_close)
    root.mainloop()

def register_func():
    auth.geometry(f'300x350+{int(screen_width)}+{int(screen_height)}')
    var_user=StringVar()
    var_pass=StringVar()
    var_sq=StringVar()
    var_ans=StringVar()
    def register():
        if var_user.get()=='' or var_pass.get()=='' or var_sq.get()=='Select' or var_ans.get()=='':
            #bol('All Fields are Required')
            messagebox.showerror('Error','All Fields are Required!!!')
        else:
            try:
                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()
                db_cursor.execute(' INSERT INTO users VALUES (?,?,?,?)',(   var_user.get(), 
                    var_pass.get(),var_sq.get(),var_ans.get()
                ))  
                conn.commit()
                conn.close()
                #bol('User Registered Successfully')
                messagebox.showinfo('Registered','User Registered Successfully')
                login_func()
            except Exception as e:
                #bol(f'Username ,{var_user.get()} ,is already registered')
                messagebox.showerror('Alert',f'Username {var_user.get()} is already registered')
                login_func()
    index_frame=Canvas(auth,highlightthickness=0,bg='#636466')
    index_frame.place(relx=0.0,rely=0.0 ,width=300,height=20)
    index_text=Label(index_frame,text='Register',font=('Tw Cen MT',10),bg='#636466',fg='white')
    index_text.place(relx=0.0,rely=0.0)
    lu_frame=Canvas(auth,highlightthickness=0,bg='white')
    lu_frame.place(relx=0.01,rely=0.4 ,width=289,height=250)
    
    user_lbl=Label(lu_frame,text="Username : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    user_lbl.place(relx=0.16,rely=0.0)

    user_tb=Entry(lu_frame,font=('Tw Cen MT',10),width=18,textvariable=var_user,bg='white')
    user_tb.place(relx=0.42,rely=0.0)
    


    pass_lbl=Label(lu_frame,text="Password : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    pass_lbl.place(relx=0.16,rely=0.15)

    pass_tb=Entry(lu_frame,font=('Tw Cen MT',10),width=18,textvariable=var_pass,show='*')
    pass_tb.place(relx=0.42,rely=0.15)
    
    secque_lbl=Label(lu_frame,text="Security Question : ",font=('Tw Cen MT',12),fg="#9f1c33",bg='white')
    secque_lbl.place(relx=0.05,rely=0.3)

    secque_cb=ttk.Combobox(lu_frame,font=('Tw Cen MT',10),state='readonly',width=17,textvariable=var_sq)
    secque_cb['values']=('Select','Nickname?','First School?','Favourite Colour?','Birth Place??','Hobby?')
    secque_cb.current(0)
    secque_cb.place(relx=0.5,rely=0.3)

    ans_lbl=Label(lu_frame,text="Answer : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    ans_lbl.place(relx=0.16,rely=0.45)

    ans_tb=Entry(lu_frame,font=('Tw Cen MT',10),width=18,textvariable=var_ans,bg='white')
    ans_tb.place(relx=0.42,rely=0.45)

    
    register_but=Button(lu_frame,text='Register',font=('Tw Cen MT',11),fg='white',bg='#9E1C32',relief=RAISED,cursor='hand2',width=7,borderwidth=3,command=register)
    register_but.place(relx=0.4,rely=0.6)
    resortlogin_but=Button(lu_frame,text='Login',font=('Tw Cen MT',10),bg='white',fg='#9E1C32',borderwidth=0,cursor='hand2',command=login_func,highlightthickness=0)
    resortlogin_but.place(relx=0.7,rely=0.65)    
   
def forgot_func():
    auth.geometry(f'300x300+{int(screen_width)}+{int(screen_height)}')
    var_user=StringVar()
    var_pass=StringVar()
    var_sq=StringVar()
    var_ans=StringVar()
    def forpass():
        if var_user.get()=='' or var_sq.get()=='Select' or var_ans.get()=='':
            #bol('All Fields are Required')
            messagebox.showerror('Error','All Fields are Required!!!')
        else:
            try:
                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()
                db_cursor.execute(' SELECT * FROM users WHERE Username=? ',(   var_user.get(), 
                )) 
                test=db_cursor.fetchone()
                #print(test)
                if test[2]==var_sq.get() and test[3]==var_ans.get():
                    #bol(f'Your Password is ')
                    #[bol(i) for i in test[1]]
                    messagebox.showinfo('Authenticated',f'Your Password is {test[1]} .')
                    login_func()
                    
                else:
                    #bol('Incorrect Security Question , or,Answer , Please try again')
                    messagebox.showerror('Alert!!!','Incorrect Security Question/Answer, \n  Please try again')

                    
                conn.commit()
                conn.close()
                
            except Exception as e:
                #bol(f'Username ,{var_user.get()} ,is not registered')
                messagebox.showerror('Alert!!!',f'Username {var_user.get()} is not registered')
                register_func()
                # print(e)
    index_frame=Canvas(auth,highlightthickness=0,bg='#636466')
    index_frame.place(relx=0.0,rely=0.0 ,width=300,height=20)
    index_text=Label(index_frame,text='Forgot Password',font=('Tw Cen MT',10),bg='#636466',fg='white')
    index_text.place(relx=0.0,rely=0.0)
    l_frame=Canvas(auth,highlightthickness=0,bg='white')
    l_frame.place(relx=0.01,rely=0.4 ,width=289,height=250)
    
    user_lbl=Label(l_frame,text="Username : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    user_lbl.place(relx=0.16,rely=0.0)

    user_tb=Entry(l_frame,font=('Tw Cen MT',10),width=18,textvariable=var_user,bg='white')
    user_tb.place(relx=0.42,rely=0.0)
    
    
    secque_lbl=Label(l_frame,text="Security Question : ",font=('Tw Cen MT',12),fg="#9f1c33",bg='white')
    secque_lbl.place(relx=0.05,rely=0.15)

    secque_cb=ttk.Combobox(l_frame,font=('Tw Cen MT',10),state='readonly',width=17,textvariable=var_sq)
    secque_cb['values']=('Select','Nickname?','First School?','Favourite Colour?','Birth Place??','Hobby?')
    secque_cb.current(0)
    secque_cb.place(relx=0.5,rely=0.15)

    ans_lbl=Label(l_frame,text="Answer : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    ans_lbl.place(relx=0.16,rely=0.3)

    ans_tb=Entry(l_frame,font=('Tw Cen MT',10),width=18,textvariable=var_ans,bg='white')
    ans_tb.place(relx=0.42,rely=0.3)

    
    getpass_but=Button(l_frame,text='Authenticate',font=('Tw Cen MT',11),fg='white',bg='#9E1C32',relief=RAISED,cursor='hand2',width=8,borderwidth=3,command=forpass)
    getpass_but.place(relx=0.4,rely=0.5)
    resortlogin_but=Button(l_frame,text='Login',font=('Tw Cen MT',10),bg='white',fg='#9E1C32',borderwidth=0,cursor='hand2',command=login_func,highlightthickness=0)
    resortlogin_but.place(relx=0.71,rely=0.55)
    
    

def login_func():
    auth.geometry(f'300x300+{int(screen_width)}+{int(screen_height)}')
    var_user=StringVar()
    var_pass=StringVar()
    var_sq=StringVar()
    var_ans=StringVar()
    
    def login():
        if var_user.get()=='' or var_pass.get()=='':
            #bol('All Fields are Required!')
            messagebox.showerror('Error','All Fields are Required!!!')
        else:
            try:
                conn=sqlite3.connect('Student_DB.db')
                db_cursor=conn.cursor()
                db_cursor.execute(' SELECT Password FROM users WHERE Username=? ',(   var_user.get(), 
                )) 
                test=db_cursor.fetchone()
                if test[0]==var_pass.get():
                    
                    #bol('Loged In Successfully')
                    
                    auth.withdraw()
                    main()

                    
                else:
                    
                    #bol('Incorrect Password   , Please try again')
                    messagebox.showerror('Alert!!!','Incorrect Password, \n  Please try again')                    
                conn.commit()
                conn.close()  
            except Exception as e:
                #bol(f'Username ,{var_user.get()} ,is not registered')
                messagebox.showerror('Alert!!!',f'Username {var_user.get()} is not registered')                
    
    index_frame=Canvas(auth,highlightthickness=0,bg='#636466')
    index_frame.place(relx=0.0,rely=0.0 ,width=300,height=20)
    index_text=Label(index_frame,text='Login',font=('Tw Cen MT',10),bg='#636466',fg='white')
    index_text.place(relx=0.0,rely=0.0)
    ll_frame=Canvas(auth,highlightthickness=0,bg='white')
    ll_frame.place(relx=0.01,rely=0.4 ,width=289,height=220)
    
    user_lbl=Label(ll_frame,text="Username : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    user_lbl.place(relx=0.145,rely=0.05)

    user_tb=Entry(ll_frame,font=('Tw Cen MT',10),width=18,textvariable=var_user,bg='white')
    user_tb.place(relx=0.42,rely=0.05)
    
    pass_lbl=Label(ll_frame,text="Password : ",font=('Tw Cen MT',12),bg='white',fg='#9f1c33')
    pass_lbl.place(relx=0.16,rely=0.25)

    pass_tb=Entry(ll_frame,font=('Tw Cen MT',10),width=18,textvariable=var_pass,show='*')
    pass_tb.place(relx=0.42,rely=0.25)

    login_but=Button(ll_frame,text='Log In',font=('Tw Cen MT',11),fg='white',bg='#9E1C32',relief=RAISED,cursor='hand2',width=7,borderwidth=3,command=login)
    login_but.place(relx=0.16,rely=0.5)
    
    register_but=Button(ll_frame,text='Register',font=('Tw Cen MT',10),bg='white',fg='#9E1C32',borderwidth=0,cursor='hand2',command=register_func,highlightthickness=0)
    register_but.place(relx=0.55,rely=0.47)

    forgotPass_but=Button(ll_frame,text='Forgot Password',font=('Tw Cen MT',10),bg='white',fg='#9E1C32',borderwidth=0,cursor='hand2',command=forgot_func,highlightthickness=0)
    forgotPass_but.place(relx=0.55,rely=0.57)
    
if __name__=='__main__':
    auth=Tk()
    auth.iconbitmap(r'C:\Users\zaid\Desktop\FRAMS\fram_icon.ico')
    screen_width = auth.winfo_screenwidth()/2.5
    screen_height = auth.winfo_screenheight()/4
    auth.geometry(f'300x300+{int(screen_width)}+{int(screen_height)}')
    auth.title('Authentication')
    auth.configure(bg='white')
    auth.resizable(False,False)
    
    logo=ImageTk.PhotoImage(Image.open("tasveer/dyicon.jpeg").resize((70,70)))
    logo_lable=Label( auth,image=logo,border=0,borderwidth=0,cursor='hand2')
    logo_lable.place(relx=0.38,rely=0.07)
    logo_lable.bind('<Button-1>', lambda x: webbrowser.open_new('https://dypatiluniversitypune.edu.in/school-of-engineering-ambi.php'))
    login_lbl=Label(auth,text="Welcome to F.R.A.M.S.",font=('Tw Cen MT',18),bg='white',fg='#9f1c33')
    login_lbl.place(relx=0.12,rely=0.3)
    
    login_func()
    auth.mainloop()
