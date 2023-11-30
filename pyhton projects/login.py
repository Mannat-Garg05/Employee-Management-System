from tkinter import *
from tkinter import messagebox
import beforeuser
import forgot

import pymysql.cursors
class login:
    def __init__(self):
        self.root=Tk()
        self.root.title("admin login")
        self.root.geometry("490x400+10+10")
        self.l2=Label(self.root,text="Login..",font=("Times New Roman",30,"bold"))
        self.l2.place(relx=.5,rely=.05,anchor="center")
        self.l1=Label(self.root,text="Admin Id:-",font=("Times New Roman",16,"bold","underline"))
        self.l1.place(relx=0.32,rely=.2,anchor="center")
        self.t1=Entry(self.root,width=35)
        self.t1.place(relx=.5,rely=.183)
        self.l3=Label(self.root,text="Password:-",font=("Times New Roman",16,"bold","underline"))
        self.l3.place(relx=0.32,rely=0.4,anchor="center")
        self.t2=Entry(self.root,width=35,show="*")
        self.t2.place(relx=.500,rely=.38)
        self.b1=Button(self.root,text="Forgot password",font=("Times New Roman",10,"bold"),command=self.forgotbut)
        self.b1.place(relx=.32,rely=.50)
        self.b2=Button(self.root,text="Login",font=("Times New Roman",8,"bold"),width=10,command=self.loginbut)
        self.b2.place(relx=.555,rely=.50)
    def loginbut(self):
        if self.t1.get()=="" or self.t2.get()=="":
            messagebox.showinfo("Info","please fill the id and password")
            self.t1.delete(0,END)
            self.t2.delete(0,END)
        else:
            conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
            cursor=conn.cursor()
            adminid=self.t1.get()
            pwd=self.t2.get()
            cursor.execute("select * from tbadmin where admid=%s and admpwd=%s",(adminid,pwd))
            conn.commit
            rows=cursor.rowcount
            if rows>0:
                messagebox.showinfo("Info","Welcome admin")
                self.root.destroy()
                obj=beforeuser.buttons()
            else:
                messagebox.showinfo("Info","Wrong input")
                self.t1.delete(0,END)
                self.t2.delete(0,END)
                
                
            
    def forgotbut(self):
        self.root.destroy()
        onj=forgot.forgot2()
obj=login()        
