from tkinter import *
from tkinter import messagebox
import pymysql.cursors
import beforeuser
class security:
    def __init__(self):
        self.root=Tk()
        self.root.title("forgot password")
        self.root.geometry("550x550+10+10")
        self.fr=LabelFrame(self.root,height=500,width=500,text="ID")
        self.fr.config(relief=SUNKEN)
        self.fr.place(relx=.04,rely=.05)
        self.l1=Label(self.fr,text="ADMIN ID:-",font=("Times New Roman",14,"bold","underline"))
        self.l1.place(relx=0.2,rely=.05,anchor="center")
        self.t1=Entry(self.fr,width=30)
        self.t1.place(relx=.4,rely=.03)
        self.b1=Button(self.fr,text="submit",command=self.sec)
        self.b1.place(relx=0.745,rely=0.092)
    def sec(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        
        cursor=self.conn.cursor()
        cursor1=self.conn.cursor()
        adminid=self.t1.get()
        cursor.execute("select * from tbadmin where admid=%s",(adminid,))
        self.conn.commit()
        rows=cursor.rowcount
        if rows>0:
            
           # messagebox.showinfo("Info","Welcome admin")
            self.fr1=LabelFrame(self.fr,height=400,width=430,text="SECURITY")
            self.fr1.config(relief=SUNKEN)
            self.fr1.place(relx=.06,rely=.16)
            self.t1.config(state="disabled")
            self.l2=Label(self.fr1,text="ENTER PASSWORD :-",font=("Times New Roman",12,"bold","underline"))
            self.l2.place(relx=.08,rely=.01)
            
            self.t2=Entry(self.fr1,width=25,show="*")
            self.t2.place(relx=0.5,rely=0.013)
            self.b2=Button(self.fr1,text="SUBMIT",command=self.loginbut)
            self.b2.place(relx=0.65,rely=0.09)
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
                messagebox.showinfo("Info","Password matched")
                
                self.t2.config(state="disabled")
                self.fr2=LabelFrame(self.fr1,height=250,width=350,text="NEw PASSWORD")
                self.fr2.config(relief=SUNKEN)
                self.fr2.place(relx=.06,rely=.32)
                self.l5=Label(self.fr2,text="Enter new Question:-",font=("Times New Roman",12,"bold","underline"))
                self.l5.place(relx=.07,rely=.07)
                self.t3=Entry(self.fr2,width=20)
                self.t3.place(relx=.53,rely=.08)
                self.l6=Label(self.fr2,text="Enter the password:-",font=("Times New Roman",12,"bold","underline"))
                self.l6.place(relx=.07,rely=.27)
                self.t4=Entry(self.fr2,width=20)
                self.t4.place(relx=.533,rely=.28)
                self.b1=Button(self.fr2,text="Submit",command=self.pass1)
                self.b1.place(relx=0.85,rely=0.41)
            
            else:
                messagebox.showinfo("Info","Wrong input")
                self.t1.delete(0,END)
                self.t2.delete(0,END)

    def pass1(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        newques=self.t3.get()
        newpass=self.t4.get()
        self.t1.configure(state="normal")
        adminid=str(self.t1.get())
        self.t1.configure(state="disabled")
        cursor=self.conn.cursor()
        cursor.execute("update tbadmin set admsecques=%s, admsecans=%s where admid=%s",(newques,newpass,adminid))
        self.conn.commit()
        messagebox.showinfo("Info","Updation succefully")
        self.root.destroy()
        obj=before.buttons()
                
                       

    


        

