from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql.cursors
import datetime
import math
import beforeuser
class transmoney:
    def __init__(self):
        self.root=Tk()
        self.root.title("TRANSFER")
        self.root.config(background="lightcyan")
        self.root.geometry("500x450+0+0")
        self.l1=Label(self.root)
        self.l1.pack()
        self.i2=ImageTk.PhotoImage(Image.open("images\\transfer.png").resize((600,140),Image.ANTIALIAS))
        self.l1.config(image=self.i2)
        self.l2=Label(self.root,text="ACCOUNT NUMBER:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
        self.l2.place(relx=.265,rely=.39,anchor="center")
        self.t1=Entry(self.root,width=35)
        self.t1.place(relx=.5,rely=.37)
        self.b2=Button(self.root,text=" SEARCH ",font=("Times New Roman",12,"bold"),command=self.trans)
        self.b2.place(relx=.5,rely=0.46,anchor="center")
        self.b3=Button(self.root,text=" BACK ",font=("Times New Roman",12,"bold"),command=self.back)
        self.b3.place(relx=.7,rely=0.46,anchor="center")
    def back(self):
        self.root.destroy()
        obj=beforeuser.buttons()
    def trans(self):
         
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
                self.l4=Label(self.root,text="TRANSFER ACCOUNT:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
                self.l4.place(relx=0.25,rely=0.65,anchor="center")
                self.t3=Entry(self.root,width=35)
                self.t3.place(relx=.500,rely=.63)
                self.l5=Label(self.root,text="AMOUNT TO TRANSFER:-",font=("Times New Roman",16,"bold","underline"),background="lightcyan")
                self.l5.place(relx=0.26,rely=0.78,anchor="center")
                self.t4=Entry(self.root,width=35)
                self.t4.place(relx=.500,rely=.755)
                self.b3=Button(self.root,text=" TRANSFER ",font=("Times New Roman",12,"bold"),command=self.finaltrans)
                self.b3.place(relx=.5,rely=.90,anchor="center")
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
    def finaltrans(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=self.conn.cursor()
        trans=self.t4.get()
        self.t2.configure(state="normal")
        bal=self.t2.get()
        self.t2.configure(state="disabled")
         
        accno=self.t3.get()
        
        
        self.t3.configure(state="disabled")
        

        cursor.execute("select * from tbaccount where accno=%s",(accno,))
        self.conn.commit()
        rows=cursor.rowcount
        if rows==0:
            messagebox.showinfo("Info","ACCOUNT NOT FOUND!!")
            self.t3.configure(state="normal")
            self.t3.delete(0,END)
        else:    
                            
            if trans <= bal:
                self.t2.configure(state="normal")
                amt=int(bal)-int(trans)
                self.t2.delete(0,END)
                self.t2.insert(0,amt)
                self.t1.configure(state="normal")
                accno=self.t1.get()
                self.t1.configure(state="disabled")
                cursor.execute("update tbaccount set balance=%s where accno=%s",(amt,accno))
                self.conn.commit()
                self.t3.configure(state="normal")
                taccno=self.t3.get()
                cursor.execute("select * from tbaccount where accno=%s",(taccno,))
                self.conn.commit()
                for bb in cursor:
                    
                
                    tamt=int(self.t4.get())+int(bb[9])
                cursor.execute("update tbaccount set balance=%s where accno=%s",(tamt,taccno))
                self.conn.commit()
                
                messagebox.showinfo("Info","TRANSFER SUCCESSFULL!!")
                cursor.execute("select ifnull(max(transid),0) from tbtransaction")
        
                row=cursor.fetchone()
                eno=row[0]
                eno=eno+1
                tr="TRANSFER"
                date=datetime.date.today()
                today=datetime.datetime.now()
                time=datetime.datetime.time(today)
        
                cursor.execute("insert into tbtransaction values(%s,%s,%s,%s,%s,%s,%s)",(eno,accno,taccno,tr,tamt,date,time))
                self.conn.commit()
        
                self.root.destroy()
                obj=transmoney()
                
            else:
                messagebox.showinfo("Info","INSUFFICIENT BALANCE!!")
                self.t4.delete(0,END)
                
                
                
                
    
#obj=transmoney()        
