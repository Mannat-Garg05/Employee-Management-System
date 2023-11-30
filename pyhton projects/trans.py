from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql.cursors
import datetime
class closeacc:
    def __init__(self):
        self.root=Tk()
        self.root.title("update account")
        self.root.geometry("450x500+0+0")
        self.fr=LabelFrame(self.root,width=400,height=450,text="ACCOUNT DETAILS")
        self.fr.place(relx=.5,rely=.5,anchor="center")
        self.l1=Label(self.fr,text="ACCOUNT NUMBER :- ",foreground="black",font=("Arial",11),anchor="w")
        self.l1.place(relx=.04,rely=.036)
        self.t1=Entry(self.fr,width=20,font=("Arial",11))
        self.t1.place(relx=.52,rely=0.036)

        self.b1=Button(self.fr,text="  SEARCH  ",font=("Arial",11),command=self.search)
        self.b1.place(relx=0.517,rely=0.1)
    def search(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        
        cursor=self.conn.cursor()
        cursor1=self.conn.cursor()
        adminid=self.t1.get()
        cursor.execute("select * from tbadmin where admid=%s",(adminid,))
        self.conn.commit()
        rows=cursor.rowcount
        if rows>0:
            
            messagebox.showinfo("Info","Record found!!")

obj=closeacc()
