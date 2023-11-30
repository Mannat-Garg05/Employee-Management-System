from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql.cursors
import datetime
import  beforeuser 
class userpage:
    def __init__(self):
        self.root=Tk()
        self.root.title("new user")
        self.root.geometry("450x500+0+0")
        self.fr=LabelFrame(self.root,width=400,height=450,text="ACC. HOLDER'S FILE")
        self.fr.place(relx=.5,rely=.5,anchor="center")

        self.l1=Label(self.fr,text="ACCOUNT NUMBER :- ",foreground="black",font=("Arial",11),anchor="w")
        self.l1.place(relx=.04,rely=.036)
        self.t1=Entry(self.fr,width=20,font=("Arial",11))
        self.t1.place(relx=.52,rely=0.036)

        self.admidgen()
        


        self.l2=Label(self.fr,text="CUSTOMER NAME:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l2.place(relx=.04,rely=.13)
        self.t2=Entry(self.fr,width=20,font=("Arial",11))
        self.t2.place(relx=.52,rely=.13)


        self.l3=Label(self.fr,text="CUSTOMER ADDRESS:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l3.place(relx=.04,rely=0.22)
        self.t3=Entry(self.fr,width=20,font=("Arial",11))
        self.t3.place(relx=0.52,rely=0.22)

        self.l4=Label(self.fr,text="CUSTOMER GENDER:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l4.place(relx=0.04,rely=.31)
        self.s1=StringVar()
        self.s1.set("Male")
        self.r1=Radiobutton(self.fr,text="Male",variable=self.s1,value="Male",font=("Arial",11))
        self.r1.place(relx=0.52,rely=0.3)
        self.r2=Radiobutton(self.fr,text="Female",variable=self.s1,value="Female",font=("Arial",11))
        self.r2.place(relx=0.75,rely=0.3)


        self.l5=Label(self.fr,text="CUSTOMER EMAIL:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l5.place(relx=0.04,rely=0.39 )
        self.t5=Entry(self.fr,width=18,font=("Arial",13))
        self.t5.place(relx=0.52,rely=0.39)

        self.l6=Label(self.fr,text="CUSTOMER MOBILE :- ",foreground="black",font=("Arial",11),anchor="w")
        self.l6.place(relx=0.04,rely=0.48)
        self.t6=Entry(self.fr,width=20,font=("Arial",11))
        self.t6.place(relx=0.52,rely=0.48)
        
        self.l7=Label(self.fr,text="FATHER'S NAME:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l7.place(relx=0.04,rely=0.57)
        self.t7=Entry(self.fr,width=20,font=("Arial",11))
        self.t7.place(relx=0.52,rely=0.57)

        self.l8=Label(self.fr,text="MOTHER'S NAME:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l8.place(relx=0.04,rely=0.66)
        self.t8=Entry(self.fr,width=20,font=("Arial",11))
        self.t8.place(relx=0.52,rely=0.66)


        self.l9=Label(self.fr,text="ACCOUNT OPENING:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l9.place(relx=0.04,rely=0.75)
        date=datetime.date.today()
        self.l12=Entry(self.fr,width=20)
        self.l12.place(relx=0.52,rely=0.75)
        self.l12.configure(state="normal")
        self.l12.insert(0,date)
        self.l12.configure(state="disabled")
        
        


        self.l11=Label(self.fr,text="ACCOUNT BALANCE:- ",foreground="black",font=("Arial",11),anchor="w")
        self.l11.place(relx=0.04,rely=0.82)
        self.t11=Entry(self.fr,width=20,font=("Arial",11))
        self.t11.place(relx=0.52,rely=0.82)
        self.t11.insert(0,"0")
        self.t11.configure(state="disabled")

        self.b1=Button(self.fr,text="Save",command=self.valid)
        self.b1.place(relx=0.52,rely=0.91)
        self.b2=Button(self.fr,text="BACK",command=self.back)
        self.b2.place(relx=0.12,rely=0.91)
    def admidgen(self):
        self.con=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        self.cursor=self.con.cursor()
        self.cursor.execute("select ifnull(max(accno),0) from tbaccount")
        self.con.commit()
        row=self.cursor.fetchone()
        eno=row[0]
        eno=eno+1
        self.t1.configure(state="normal")
        self.t1.delete(0,END)
        self.t1.insert(0,eno)
        self.t1.configure(state="disabled")

    def back(self):
        self.root.destroy()
        obj=beforeuser.buttons()
    def valid(self):
         if self.t1.get()=="" or self.t2.get()=="" or self.t3.get()=="" or self.t5.get()=="" or self.t6.get()=="" or self.t7.get()=="" or self.t8.get()=="" or self.t11.get()=="":
            
            messagebox.showinfo("Info","please fill all the details")
            self.t1.delete(0,END)
            self.t2.delete(0,END)
            self.t3.delete(0,END)
            self.t5.delete(0,END)
            self.t6.delete(0,END)
            self.t7.delete(0,END)
            self.t8.delete(0,END)
            self.t11.delete(0,END)       

         else:
            
            self.cursor=self.con.cursor()
        
            accno=str(self.t1.get())
            cname=str(self.t2.get())
            cadd=str(self.t3.get())
            cgen=str(self.s1.get())
            cemail=str(self.t5.get())
            cmob=str(self.t6.get())    
            cfname=str(self.t7.get())
            cmname=str(self.t8.get())
            odate=str(self.l12.get())
            
            balance="0"
            self.cursor.execute("insert into tbaccount values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(accno,cname,cadd,cgen,cemail,cmob,cfname,cmname,odate,balance))
            
            self.con.commit()
            self.con.close()
            messagebox.showinfo("Info","INFO. UPDATED SUCCESSFULLY")
            self.t1.delete(0,END)
            self.t2.delete(0,END)
            self.t3.delete(0,END)
            self.t5.delete(0,END)
            self.t6.delete(0,END)
            self.t7.delete(0,END)
            self.t8.delete(0,END)
            self.t11.delete(0,END)
            self.root.destroy()
            obbj=userpage()
         print("hello")

#obj=userpage()
