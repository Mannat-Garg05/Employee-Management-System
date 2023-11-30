from tkinter import *
from tkinter import messagebox
import beforeuser
import pymysql.cursors
class edit:
    def __init__(self):
        self.root=Tk()
        self.root.title("EDIT PASSWORD")
        self.root.geometry("550x550+10+10")
        self.fr=LabelFrame(self.root,height=500,width=500,text="ID")
        self.fr.config(relief=SUNKEN)
        self.fr.place(relx=.04,rely=.05)
        self.l1=Label(self.fr,text="Admin Id:-",font=("Times New Roman",14,"bold","underline"))
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
            
            messagebox.showinfo("Info","Welcome admin")

    
            self.fr1=LabelFrame(self.fr,height=400,width=430,text="SECURITY")
            self.fr1.config(relief=SUNKEN)
            self.fr1.place(relx=.06,rely=.16)
            self.t1.config(state="disabled")
            self.l2=Label(self.fr1,text="Security ques is :-",font=("Times New Roman",12,"bold","underline"))
            self.l2.place(relx=.08,rely=.01)
            
            self.l4=Label(self.fr1)

            cursor.execute("select admsecques from tbadmin where admid=%s",(adminid,))
            self.l4.place(relx=.47,rely=.01)
            for r in cursor:
                for i in r:
                    pass    
            self.l4.config(text=i)    

            
            self.l4=Label(self.fr1,text="Security answer :-",font=("Times New Roman",12,"bold","underline"))
            self.l4.place(relx=.08,rely=.13)
            self.t2=Entry(self.fr1,width=20)
            self.t2.place(relx=.48,rely=.13)
            self.b1=Button(self.fr1,text="submit",command=self.new)
            self.b1.place(relx=0.72,rely=0.21)
        else:
            messagebox.showinfo("Info","Wrong input")
            self.t3.delete(0,END)
            self.conn.close()    

    def new(self):
        
        if self.t2.get()=="":
            messagebox.showinfo("Info","Enter the ans correctly")
        else:
            self.t2.config(state="disabled")
            self.fr2=LabelFrame(self.fr1,height=250,width=350,text="NEw PASSWORD")
            self.fr2.config(relief=SUNKEN)
            self.fr2.place(relx=.06,rely=.32)
            self.l5=Label(self.fr2,text="Enter new password:-",font=("Times New Roman",12,"bold","underline"))
            self.l5.place(relx=.07,rely=.07)
            self.t3=Entry(self.fr2,width=20,show="*")
            self.t3.place(relx=.53,rely=.08)
            self.l6=Label(self.fr2,text="Confirm the password:-",font=("Times New Roman",12,"bold","underline"))
            self.l6.place(relx=.07,rely=.27)
            self.t4=Entry(self.fr2,width=20,show="*")
            self.t4.place(relx=.533,rely=.28)
            self.b1=Button(self.fr2,text="Submit",command=self.pass1)
            self.b1.place(relx=0.85,rely=0.41)
    def pass1(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        
        cursor=self.conn.cursor()
        self.t1.config(state="normal")
        adminid=self.t1.get()
        self.t1.config(state="disabled")
        
        if self.t3.get()!=self.t4.get() or self.t3.get()=="" or self.t4.get()=="" :
            messagebox.showinfo("Info","Enter the password correctly")
        if self.t3.get()==self.t4.get():
            newpass=self.t3.get()
            self.t3.config(state="disabled")
            self.t4.config(state="disabled")
            cursor.execute("update tbadmin set admpwd=%s where admid=%s",(newpass,adminid))
            messagebox.showinfo("Info","Password updated")
            self.conn.commit()
            self.conn.close()
            self.root.destroy()
            obj=beforeuser.buttons()        
            
#obj=edit()        
