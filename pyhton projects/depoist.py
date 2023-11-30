from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql.cursors
import datetime
import math
import beforeuser
class depmoney:
    def __init__(self):
        self.root=Tk()
        self.root.title("DEPOIST")
        self.root.config(background="lightcyan")
        self.root.geometry("500x450+0+0")
        self.l1=Label(self.root)
        self.l1.pack()
        self.ii2=ImageTk.PhotoImage(Image.open("images\\download.jpg").resize((600,140),Image.ANTIALIAS))
        self.l1.config(image=self.ii2)
        self.l2=Label(self.root,text="ACCOUNT NUMBER:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
        self.l2.place(relx=.265,rely=.39,anchor="center")
        self.t3=Entry(self.root,width=35)
        self.t3.place(relx=.5,rely=.37)
        self.b2=Button(self.root,text=" SEARCH ",font=("Times New Roman",12,"bold"),command=self.balance)
        self.b2.place(relx=.5,rely=0.46,anchor="center")
        self.b3=Button(self.root,text=" BACK ",font=("Times New Roman",12,"bold"),command=self.back)
        self.b3.place(relx=.7,rely=0.46,anchor="center")
    def back(self):
        self.root.destroy()
        obj=beforeuser.buttons()
             
    def balance(self):
        if self.t3.get()=="":
            messagebox.showinfo("Info","please fill the account number")
        conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=conn.cursor()
        accno=self.t3.get()
        cursor.execute("select * from tbaccount where accno=%s",(accno,))
        #self.conn.commit()
        rows=cursor.rowcount
        self.t3.configure(state="disabled")

        if rows>0:
            
            messagebox.showinfo("Info","Record found!!")
            
            self.l1=Label(self.root,text="BALACE :-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
            self.l1.place(relx=0.3,rely=.56,anchor="center")
            self.t1=Entry(self.root,width=35)
            self.t1.place(relx=.5,rely=.53)
            self.l3=Label(self.root,text="AMOUNT TO ADD:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
            self.l3.place(relx=0.28,rely=0.78,anchor="center")
            self.t2=Entry(self.root,width=35)
            self.t2.place(relx=.500,rely=.755)
            self.b1=Button(self.root,text=" DEPOIST ",font=("Times New Roman",12,"bold"),command=self.finaldep)
            self.b1.place(relx=.5,rely=.90,anchor="center")
            cursor.execute("select * from tbaccount where accno=%s",(accno,))
            for row in cursor:
                row = row[9]
            self.t1.insert(0,row)
            self.t1.configure(state="disabled")
        else:
            messagebox.showinfo("Info","Record not found!!")
            self.t3.configure(state="normal")
            self.t3.delete(0,END)    
        cursor.execute("select * from tbaccount where accno=%s",(accno,))
               
    def finaldep(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=self.conn.cursor()
        amm=self.t2.get()
        self.t1.configure(state="normal")
        bal=int(self.t1.get())
        add=(int(bal)+int(amm))
        print(bal)
        print(amm)
        self.t1.delete(0,END)
        
        self.t1.insert(0,add)
        self.t1.configure(state="disabled")
        self.t3.configure(state="normal")
        accno=self.t3.get()
        self.t3.configure(state="disabled")
        cursor.execute("update tbaccount set balance=%s where accno=%s",(add,accno))
        messagebox.showinfo("Info","Record updated successfully!!")
        self.conn.commit()
        
        
        cursor.execute("select ifnull(max(transid),0) from tbtransaction")
        #self.conn.commit()
        row=cursor.fetchone()
        eno=row[0]
        eno=eno+1
        tr="deposit"
        date=datetime.date.today()
        today=datetime.datetime.now()
        time=datetime.datetime.time(today)
        #self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor.execute("insert into tbtransaction values(%s,%s,%s,%s,%s,%s,%s)",(eno,accno,accno,tr,amm,date,time))
        self.conn.commit()
        print("hello")
        self.conn.close()
                       
        self.root.destroy()
        obj=depmoney()
            
            
#obj=depmoney()
