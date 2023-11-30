from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql.cursors
import beforeuser
class editp:
    def __init__(self):
        self.root=Tk()
        self.root.title("UPDATE PROFILE")
        self.root.geometry("500x500+0+0")
        self.fr=LabelFrame(self.root,width=450,height=450,text="ACCOUNTs FILE")
        self.fr.place(relx=.5,rely=.5,anchor="center")
        self.l1=Label(self.fr,text="AMIN ID :- ",foreground="black",font=("Arial",13),anchor="w")
        self.l1.place(relx=.04,rely=.036)
        self.t1=Entry(self.fr,width=20,font=("Arial",11))
        self.t1.place(relx=.52,rely=0.036)
        self.b1=Button(self.fr,text="  SEARCH  ",font=("Arial",11) ,command=self.search)
        self.b1.place(relx=0.517,rely=0.1)
        self.b4=Button(self.fr,text="  BACK  ",font=("Arial",11),command=self.back1)
        self.b4.place(relx=0.73,rely=0.1)
    def back1(self):
        self.root.destroy()
        obj=beforeuser.buttons()
    def search(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        
        cursor=self.conn.cursor()
        
        accno=self.t1.get()
        cursor.execute("select * from tbadmin where admid=%s",(accno,))
        self.conn.commit()
        rows=cursor.rowcount
        self.t1.configure(state="disabled")
        if rows>0:
            
            messagebox.showinfo("Info","Record found!!")
            self.fr1=LabelFrame(self.fr,height=350,width=405,text="ACCOUNT DETAILS")
            self.fr1.config(relief=SUNKEN)
            self.fr1.place(relx=.06,rely=.16)
            self.l2=Label(self.fr1,text="SECURITY QUEs:-",font=("Times New Roman",13,"bold","underline"))
            self.l2.place(relx=.06,rely=.03)
            self.t2=Entry(self.fr1,width=18)
            self.t2.place(relx=0.7,rely=0.05)

            
            self.l3=Label(self.fr1,text="SECURITY ANSWER:-",font=("Times New Roman",13,"bold","underline"))
            self.l3.place(relx=.06,rely=.18)
            self.t3=Entry(self.fr1,width=18)
            self.t3.place(relx=0.7,rely=0.18)

        
            self.l4=Label(self.fr1,text="ADMIN'S NAME :-",font=("Times New Roman",13,"bold","underline"))
            self.l4.place(relx=.06,rely=.32)
            self.t4=Entry(self.fr1,width=18)
            self.t4.place(relx=0.7,rely=0.32)


            self.l5=Label(self.fr1,text="ADMIN'S ADDRESS:-",font=("Times New Roman",13,"bold","underline"))
            self.l5.place(relx=.06,rely=.47)
            self.t5=Entry(self.fr1,width=18)
            self.t5.place(relx=0.7,rely=0.47)

            self.l6=Label(self.fr1,text="ADMIN'S MAIL ID:-",font=("Times New Roman",13,"bold","underline"))
            self.l6.place(relx=.06,rely=.61)
            self.t6=Entry(self.fr1,width=18)
            self.t6.place(relx=0.7,rely=0.61)

            self.l7=Label(self.fr1,text="ADMIN'S MOBILE NUMBER:-",font=("Times New Roman",13,"bold","underline"))
            self.l7.place(relx=.06,rely=.75)
            self.t7=Entry(self.fr1,width=18)
            self.t7.place(relx=0.7,rely=0.75)

            self.b3=Button(self.fr1,text="UPDATE")
            self.b1.place(relx=0.75,rely=0.82)
            self.t1.configure(state="normal")
            accno=self.t1.get()
            self.t1.configure(state="disabled")
            
            cursor.execute("select * from tbadmin where admid=%s",(accno,))
            self.b3=Button(self.fr1,text="UPDATE",command=self.updata)
            self.b3.place(relx=0.7,rely=0.92)
            self.conn.commit()
            self.b3=Button(self.fr1,text="  BACK  ",command=self.back1)
            self.b3.place(relx=0.85,rely=0.92)
            
            
            for row in cursor:
                self.t2.insert(0,row[2])
                self.t2.configure(state="disabled")
                
                
                self.t3.insert(0,row[3])
                self.t3.configure(state="disabled")
                
                self.t4.insert(0,row[4])
                self.t4.configure(state="disabled")
                self.t5.insert(0,row[5])
    
                self.t6.insert(0,row[6])
                
                self.t7.insert(0,row[7])
                
                

                

            
        else:
            messagebox.showinfo("Info","Record not found!!")
            self.t1.configure(state="normal")
            self.t1.delete(0,END)

    def updata(self):
        self.t1.configure(state="normal")
        accno=self.t1.get()
        self.t1.configure(state="disabled")
        cursor1=self.conn.cursor()
        
        cemail=self.t5.get()
        cmob=self.t6.get()
        cfname=self.t7.get()
        
        cursor1.execute("update tbadmin set admaddress=%s,admemail=%s,admphno=%s where admid=%s",(cemail,cmob,cfname,accno))
        messagebox.showinfo("Info","Record updated successfully!!")
        self.conn.commit()
        self.root.destroy()
        obj=editp()
                    
#obj=editp()
