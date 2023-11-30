from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql.cursors
import math
import datetime
import beforeuser
class withmoney:
    def __init__(self):
        self.root=Tk()
        self.root.title("WITHDRAW")
        self.root.config(background="lightcyan")
        self.root.geometry("500x450+0+0")
        self.l1=Label(self.root)
        self.l1.pack()
        self.i2=ImageTk.PhotoImage(Image.open("images\\download2.png").resize((600,140),Image.ANTIALIAS))
        self.l1.config(image=self.i2)
        self.l2=Label(self.root,text="ACCOUNT NUMBER:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
        self.l2.place(relx=.265,rely=.39,anchor="center")
        self.t1=Entry(self.root,width=35)
        self.t1.place(relx=.5,rely=.37)
        self.b2=Button(self.root,text=" SEARCH ",font=("Times New Roman",12,"bold"),command=self.withds)
        self.b2.place(relx=.5,rely=0.46,anchor="center")
        self.b3=Button(self.root,text=" BACK ",font=("Times New Roman",12,"bold"),command=self.back)
        self.b3.place(relx=.7,rely=0.46,anchor="center")
    def back(self):
        self.root.destroy()
        obj=beforeuser.buttons()
    def withds(self):
         
        if self.t1.get()=="":
            messagebox.showinfo("Info","please fill the account number")
        else:    
            self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
            cursor=self.conn.cursor()
            accno=self.t1.get()
            cursor.execute("select * from tbaccount where accno=%s",(accno,))
            self.conn.commit()
            rows=cursor.rowcount
            self.t1.configure(state="disabled")
            if rows>0:
                messagebox.showinfo("Info","Record found!!")
                self.l3=Label(self.root,text="BALACE :-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
                self.l3.place(relx=0.3,rely=.53,anchor="center")
                self.t2=Entry(self.root,width=35)
                self.t2.place(relx=.5,rely=.51)
                self.l4=Label(self.root,text="WITHDRAW AMOUNT:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
                self.l4.place(relx=0.25,rely=0.75,anchor="center")
                self.t3=Entry(self.root,width=35)
                self.t3.place(relx=.500,rely=.73)
                self.b3=Button(self.root,text=" WITHDRAW ",font=("Times New Roman",12,"bold"),command=self.withdraw)
                self.b3.place(relx=.5,rely=.85,anchor="center")
                self.t1.configure(state="normal")
                accno=self.t1.get()
                self.t1.configure(state="disabled")
                cursor.execute("select * from tbaccount where accno=%s",(accno,))
                for row in cursor:
                    row = row[9]
                self.t2.insert(0,row)
                self.t2.configure(state="disabled")

                self.conn.commit()
            else:
                messagebox.showinfo("Info","Record not found!!")
                self.t1.configure(state="normal")
                self.t1.delete(0,END)
    def withdraw(self):
        self.t2.configure(state="normal")
        bal=self.t2.get()
        amt=self.t3.get()
        if int(amt)>int(bal):
            messagebox.showinfo("Info","INSUFFICIENT AMOUNT!!")
        else:
            new=int(bal)-int(amt)
            self.t1.configure(state="normal")
            accno=self.t1.get()
            self.t1.configure(state="disabled")
            self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
            cursor=self.conn.cursor()
            cursor.execute("update tbaccount set balance=%s where accno=%s",(new,accno))
            self.conn.commit()
            self.t2.configure(state="normal")
            cursor.execute("select * from tbaccount where accno=%s",(accno,))
            self.conn.commit()
            for r in cursor:
                r=r[9]
            self.t2.delete(0,END)    
            self.t2.insert(0,r)
            self.t2.configure(state="disabled")
            messagebox.showinfo("Info","WITHDRAWN SUCCESSFULLY!!")
            cursor.execute("select ifnull(max(transid),0) from tbtransaction")
        
            row=cursor.fetchone()
            eno=row[0]
            eno=eno+1
            tr="WITHDRAW"
            date=datetime.date.today()
            today=datetime.datetime.now()
            time=datetime.datetime.time(today)
        
            cursor.execute("insert into tbtransaction values(%s,%s,%s,%s,%s,%s,%s)",(eno,accno,accno,tr,amt,date,time))
            self.conn.commit()
        
            self.root.destroy()
            obj=withmoney()
            
#obj= withmoney()       
