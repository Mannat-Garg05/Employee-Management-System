from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import pymysql.cursors
class demo:
    def __init__(self):                       ###############this is a comment
        
        self.root=Tk()
        self.con=pymysql.connect(host="localhost",user="root",password="root",db="demo")
        self.root.resizable(False,False)
        self.cursor=self.con.cursor()
        
        self.root.state("zoomed")
###############################3################Name###################################
        self.l1=Label(self.root,text="ENTER YOUR NAME :- ",foreground="black",font=("Arial",13),anchor="w")
        self.l1.place(x=3,y=3)
        self.t1=Entry(self.root,width=30,font=("Arial",13))
        self.t1.place(x=212,y=3)
##########################################################################################################################
        self.l2=Label(self.root,text="ENTER THE USER ID:- ",foreground="black",font=("Arial",13),anchor="w")
        self.l2.place(x=3,y=35)
        self.t2=Entry(self.root,width=30,font=("Arial",13))
        self.t2.place(x=212,y=35)
        ###############################################################################################
        self.l3=Label(self.root,text="ENTER PASSWORD :- ",foreground="black",font=("Arial",13),anchor="w")
        self.l3.place(x=3,y=68)
        self.t3=Entry(self.root,width=30,show="*",font=("Arial",13))
        self.t3.place(x=212,y=68)
        #############################################################################################
        self.l4=Label(self.root,text="CONFIRM PASSWORD :- ",foreground="black",font=("Arial",13),anchor="w")
        self.l4.place(x=3,y=100)
        self.t4=Entry(self.root,width=30,show="*",font=("Arial",13))
        self.t4.place(x=212,y=100)
        ################################################################################################
        self.l5=Label(self.root,text="ENTER THE ADDRESS:- ",foreground="black",font=("Arial",13),anchor="w")
        self.l5.place(x=3,y=132 )
        self.t5=Text(self.root,width=30,height=5,font=("Arial",13))
        self.t5.place(x=212,y=132)
        ################################################################################################
        self.l6=Label(self.root,text="ENTER YOUR GENDER:- ",foreground="black",font=("Arial",13),anchor="w")
        self.l6.place(x=3,y=234)
        self.s1=StringVar()
        self.s1.set("Male")
        self.r1=Radiobutton(self.root,text="Male",variable=self.s1,value="Male",font=("Arial",13))
        self.r1.place(x=212,y=234)
        self.r2=Radiobutton(self.root,text="Female",variable=self.s1,value="Female",font=("Arial",13))
        self.r2.place(x=292,y=234)
        #########################################################################################################
        self.l7=Label(self.root,text="ENTER YOUR D.O.B.:- ",foreground="black",font=("Arial",13),anchor="w")
        self.l7.place(x=3,y=268)
        self.s2=StringVar()
        self.s2.set("Jan")
        self.c1=Combobox(self.root,textvariable=self.s2,font=("Arial",11),width=4)
        self.c1.place(x=212,y=268)
        ls=["jan","feb","mar","apr","may","june","july","aug","sept","oct","nov","dec"]
        self.c1.config(values=ls)

        self.s3=StringVar() 
        self.c2=Spinbox(self.root,from_=1,to=31,textvariable=self.s3,font=("Arial",11),width=6,)
        self.c2.place(x=273,y=268)
        
        self.s4=StringVar() 
        self.c3=Spinbox(self.root,from_=1947,to=2022,textvariable=self.s4,font=("Arial",11),width=6)
        self.c3.place(x=345,y=268)
        #############################################################################################################
        self.l8=Label(self.root,text="ENTER THE HOBBIES:-",foreground="black",font=("Arial",13),anchor="w")
        self.l8.place(x=3,y=300)
        self.s5=StringVar()
        self.s5.set("no")
        self.c4=Checkbutton(self.root,text="Read",font=("Arial",13))
        self.c4.config(variable=self.s5,onvalue="read",offvalue="no") 
        self.c4.place(x=207,y=300)

        
        self.s6=StringVar()
        self.s6.set("no")
        self.c5=Checkbutton(self.root,text="Swim",font=("Arial",13))
        self.c5.config(variable=self.s6,onvalue="swim",offvalue="no")
        self.c5.place(x=340,y=300)
        self.s7=StringVar()
        self.s7.set("no")
        self.c6=Checkbutton(self.root,text="Run",font=("Arial",13))
        self.c6.config(variable=self.s7,onvalue="run",offvalue="no")
        self.c6.place(x=279,y=300)
        ##################################################################################################################
        self.b1=Button(self.root,text="Save")
        self.b1.place(x=207,y=330)
        self.b2=Button(self.root,text="View")
        self.b2.place(x=245,y=330)
        self.b3=Button(self.root,text="update")
        self.b3.place(x=284,y=330)
        self.b4=Button(self.root,text="delete")
        self.b4.place(x=335,y=330)
        
        ###################################################################################################################
        self.t6=Listbox(self.root,selectmode=SINGLE,width=40,height=20)
        self.t6.place(x=538,y=3)
        self.t6.bind("<Double-Button-1>",self.fetchsingle)
    def fetchsingle(self,evt):
        index=self.t6.curselection()
        eno=self.l1.get()
        print(eno)
        
      
obj=demo()        

