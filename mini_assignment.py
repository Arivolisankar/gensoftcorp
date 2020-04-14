from tkinter import *
import sqlite3
from sys import exit

def connection():
    try:
        conn=sqlite3.connect("projects.db")
    except:
        print("cannot connect to the database")
    return conn    


def verifier():
    a=b=c=d=e=f=0
    if not project_name.get():
        t1.insert(END,"<>Project name is required<>\n")
        a=1
    if not client_name.get():
        t1.insert(END,"<>Client Name is required<>\n")
        b=1
    if not company_name.get():
        t1.insert(END,"<>Company name is required<>\n")
        c=1
    if not c_address.get():
        t1.insert(END,"<>Address is requrired<>\n")
        d=1
    if not c_phone.get():
        t1.insert(END,"<>Contact is required<>\n")
        e=1
    if not due_date.get():
        t1.insert(END,"<>Due date is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS PROJECTS(PROJECT TEXT,CLIENT TEXT,BRANCH TEXT,COMPANY TEXT,PHONE TEXT,DUEDATE TEXT)")
                cur.execute("insert into PROJECTS values(?,?,?,?,?,?)",(project_name.get(),client_name.get(),company_name.get(),c_address.get(),c_phone.get(),due_date.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from PROJECTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM PROJECTS WHERE CLIENT=?",(roll_no.get()))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE PROJECT\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE PROJECTS SET PROJECT=?,CLIENT=?,COMPANY=?,ADDRESS=?,PHONE=?,DUEDATE=? where CLIENT=?",(project_name.get(),client_name.get(),company_name.get(),c_address.get(),c_phone.get(),due_date.get(),client_name.get()))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")


def clse():
    sys.exit() 


if __name__=="__main__":
    root=Tk()
    root.title("Project Management System")
     
    project_name=StringVar()
    client_name=StringVar()
    company_name=StringVar()
    c_address=StringVar()
    c_phone=StringVar()
    due_date=StringVar()
    
    label1=Label(root,text="Project name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Client Name:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Company:")
    label3.place(x=0,y=60)

    label4=Label(root,text="Company address:")
    label4.place(x=0,y=90)

    label5=Label(root,text="Contact Number:")
    label5.place(x=0,y=120)

    label6=Label(root,text="Due Date:")
    label6.place(x=0,y=150)

    e1=Entry(root,textvariable=project_name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=client_name)
    e2.place(x=100,y=30)

    e3=Entry(root,textvariable=company_name)
    e3.place(x=100,y=60)

    e4=Entry(root,textvariable=c_address)
    e4.place(x=100,y=90)
    
    e5=Entry(root,textvariable=c_phone)
    e5.place(x=100,y=120)

    e6=Entry(root,textvariable=due_date)
    e6.place(x=100,y=150)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)
   


    b1=Button(root,text="ADD PROJECT",command=add_student,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL PROJECTS",command=view_student,width=40)
    b2.grid(row=12,column=0)

    b3=Button(root,text="DELETE PROJECT",command=delete_student,width=40)
    b3.grid(row=13,column=0)

    b4=Button(root,text="UPDATE PROJECT INFO",command=update_student,width=40)
    b4.grid(row=14,column=0)

    b5=Button(root,text="CLOSE",command=clse,width=40)
    b5.grid(row=15,column=0)


    root.mainloop()
