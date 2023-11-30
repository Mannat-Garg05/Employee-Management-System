from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image,ImageTk
#import  beforeuser 
import pymysql.cursors
class view:
    def __init__(self):                     ###############this is a comment
        
        self.root=Tk()
        self.root.title("SEARCH")
        self.root.config(background="lightcyan")
        self.root.geometry("750x600+0+0")
        self.ll=Label(self.root)
        self.ll.pack()
        self.ii2=ImageTk.PhotoImage(Image.open("images\\images.jpg").resize((500,120),Image.ANTIALIAS))
        self.ll.config(image=self.ii2)
        self.l1=Label(self.root,text=" USER NAME:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l1.place(relx=0.2,rely=0.24,anchor="center")
        self.t1=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t1.place(relx=0.515,rely=0.24,anchor="center")

        self.l2=Label(self.root,text=" USER ADDRESS:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l2.place(relx=0.18,rely=0.33,anchor="center")
        self.t2=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t2.place(relx=0.515,rely=0.33,anchor="center")

        self.l3=Label(self.root,text=" USER GENDER:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l3.place(relx=0.18,rely=0.42,anchor="center")
        self.t3=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t3.place(relx=0.515,rely=0.42,anchor="center")

        self.l4=Label(self.root,text=" USER E-MAIL:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l4.place(relx=0.18,rely=0.51,anchor="center")
        self.t4=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t4.place(relx=0.515,rely=0.51,anchor="center")

        self.l5=Label(self.root,text=" USER MOBILE:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l5.place(relx=0.18,rely=0.6,anchor="center")
        self.t5=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t5.place(relx=0.515,rely=0.6,anchor="center")

        self.l6=Label(self.root,text=" FATHER NAME:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l6.place(relx=0.18,rely=0.69,anchor="center")
        self.t6=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t6.place(relx=0.515,rely=0.69,anchor="center")

        self.l7=Label(self.root,text="MOTHERS NAME:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l7.place(relx=0.18,rely=0.78,anchor="center")
        self.t7=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t7.place(relx=0.515,rely=0.78,anchor="center")

        self.l8=Label(self.root,text="OPENING DATE:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l8.place(relx=0.18,rely=0.855,anchor="center")
        self.t8=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t8.place(relx=0.515,rely=0.855,anchor="center")

        self.l9=Label(self.root,text="BALANCE:-",font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.l9.place(relx=0.18,rely=0.93,anchor="center")
        self.t9=Entry(self.root,width=25,font=("Times New Roman",14,"bold","underline"),background="lightcyan")
        self.t9.place(relx=0.515,rely=0.93,anchor="center")

        self.list1=Listbox(self.root,selectmode=SINGLE,width=30,height=20)
        self.list1.place(relx=0.74,rely=0.22)

        self.b1=Button(self.root,text="SEARCH",command=self.search)
        self.b1.place(relx=0.8,rely=0.8)
        self.b1=Button(self.root,text="  BACK  ",command=self.back)
        self.b1.place(relx=0.8,rely=0.8)

        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=self.conn.cursor()

        cursor.execute("select * from tbaccount")
        self.conn.commit()
        for row in cursor:
            print(row[0])
            self.list1.insert(0,str(row[0])+"\n")
    def search(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        cursor=self.conn.cursor()
        #print(self.list1.curselection())

        cursor.execute("select * from tbaccount where accno=%s",(self.list1.get(self.list1.curselection()),))
        rf=cursor.fetchone()
        print(rf)
        self.t1.insert(0,rf[1])
        self.t2.insert(0,rf[2])
        self.t3.insert(0,rf[3])
        self.t4.insert(0,rf[4])
        self.t5.insert(0,rf[5])
        self.t6.insert(0,rf[6])
        self.t7.insert(0,rf[7])
        self.t8.insert(0,rf[8])
        self.t9.insert(0,rf[9])
            
        
    def back(self):
        self.root.place()
        self.beforeuser.before
      
        
