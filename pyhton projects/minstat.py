from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
import beforeuser
class mini:
    def __init__(self):
        self.root=Tk()
        self.root.title("MINI STATEMENT")
        self.root.geometry("650x500+0+0")
        self.l1=Label(self.root,text="MINI STATEMENT",font=("Times New Roman",36,"bold","underline"))
        self.l1.place(relx=0.5,rely=0.08,anchor="center")
        self.l2=Label(self.root,text="ENTER ACCOUNT",font=("Times New Roman",16,"bold","underline"))
        self.l2.place(relx=0.2,rely=0.2,anchor="center")
        self.t1=Entry(self.root,width=25,font=("Times New Roman",16))
        self.t1.place(relx=0.39,rely=0.175)
        self.b1=Button(self.root,text="  SEARCH  ",font=("Times New Roman",12),command=self.ser)
        self.b1.place(relx=0.39,rely=0.25)
    def ser(self):
        
        
        self.l3=Label(self.root,text="Trans id",font=("Times New Roman",16,"bold","underline"))
        self.l3.place(relx=0.05,rely=0.35)
        self.l4=Label(self.root,text="Transaction account",font=("Times New Roman",16,"bold","underline"))
        self.l4.place(relx=0.05,rely=0.44)
        self.l4=Label(self.root,text="Destination account",font=("Times New Roman",16,"bold","underline"))
        self.l4.place(relx=0.05,rely=0.53)
        self.l5=Label(self.root,text="Transaction type",font=("Times New Roman",16,"bold","underline"))
        self.l5.place(relx=0.05,rely=0.62)
        self.l6=Label(self.root,text="Transaction amount",font=("Times New Roman",16,"bold","underline"))
        self.l6.place(relx=0.05,rely=0.71)
        self.l7=Label(self.root,text="Transaction date",font=("Times New Roman",16,"bold","underline"))
        self.l7.place(relx=0.05,rely=0.80)
        self.l8=Label(self.root,text="Transaction time",font=("Times New Roman",16,"bold","underline"))
        self.l8.place(relx=0.05,rely=0.89)
        self.l9=Text(self.root,height=2,width=30)
        self.l9.place(relx=0.40,rely=0.35)
        self.t2=Text(self.root,height=2,width=30)
        self.t2.place(relx=0.40,rely=0.44)
        self.t3=Text(self.root,height=2,width=30)
        self.t3.place(relx=0.40,rely=0.53)
        self.t4=Text(self.root,height=2,width=30)
        self.t4.place(relx=0.40,rely=0.62)
        self.t5=Text(self.root,height=2,width=30)
        self.t5.place(relx=0.40,rely=0.71)
        self.t6=Text(self.root,height=2,width=30)
        self.t6.place(relx=0.40,rely=0.80)
        self.t7=Text(self.root,height=2,width=30)
        self.t7.place(relx=0.40,rely=0.89)
        self.list1=Listbox(self.root,selectmode=SINGLE,width=30,height=15)
        self.list1.place(relx=0.79,rely=0.35)
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=self.conn.cursor()
        acc=self.t1.get()
        self.t1.configure(state="disabled")
        cursor.execute("select * from tbtransaction")
        for row in cursor:
            print(row[0])
            self.list1.insert(0,str(row[0])+"\n")
        self.b1=Button(self.root,text="SEARCH",command=self.search)
        self.b1.place(relx=0.8,rely=0.8)
        self.b1=Button(self.root,text="  BACK  ",command=self.back)
        self.b1.place(relx=0.8,rely=0.8)

    def search(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=self.conn.cursor()
        #print(self.list1.curselection())

        cursor.execute("select * from tbtransaction where transid=%s",(self.list1.get(self.list1.curselection()),))
        rf=cursor.fetchone()
        print(rf)
        self.l9.insert(1.0,rf[0])
        self.t2.insert(1.0,rf[1])
        self.t3.insert(1.0,rf[2])
        self.t4.insert(1.0,rf[3])
        self.t5.insert(1.0,rf[4])
        self.t6.insert(1.0,rf[5])
        self.t7.insert(1.0,rf[6])
        self.l9.configure(state="disabled")
        self.t2.configure(state="disabled")
        self.t3.configure(state="disabled")
        self.t4.configure(state="disabled")
        self.t5.configure(state="disabled")
        self.t6.configure(state="disabled")
        self.t7.configure(state="disabled")
       
    def back(self):
        self.root.place()
        self.beforeuser.before
                      
#obj=mini()        
        
