from tkinter import*
from tkinter.ttk import*
class demo:
    def __init__(self):
        self.root=Tk()
        self.root.resizable(False,False)
        self.root.state("zoomed")
#################################3################Name###################################
        self.l1=Label(self.root,text="ENTER YOUR CITY :- ",foreground="black",font=("Arial",13),anchor="w")
        self.l1.place(x=3,y=3)
        self.t1=Entry(self.root,width=30,font=("Arial",13))
        self.t1.place(x=212,y=3)
        self.b1=Button(self.root,text="Insert",command=self.insert1)
        self.b1.place(x=212,y=30)
        self.list1=Listbox(self.root,selectmode=MULTIPLE,width=40,height=20)
        self.list1.place(x=9,y=60)
        self.b2=Button(self.root,text=">",width=5,command=self.trans1)
        self.b2.place(x=263,y=150)
        self.b3=Button(self.root,text="<",width=5,command=self.trans2)
        self.b3.place(x=263,y=270)
        self.list2=Listbox(self.root,selectmode=MULTIPLE,width=40,height=20)
        self.list2.place(x=310,y=60)
        self.b4=Button(self.root,text="DELETE",width=8,command=self.delete1)
        self.b4.place(x=110,y=400)
        self.b5=Button(self.root,text="DELETE",width=8,command=self.delete2)
        self.b5.place(x=393,y=400)
    def insert1(self):
        self.list1.configure(state="normal")
        self.list1.insert(0,self.t1.get()+"\n")
        self.t1.delete(0,END)
        
    def delete1(self):
        
        self.list1.delete(self.list1.index(self.list1.curselection()))
    def delete2(self):
        
        self.list1.delete(self.list1.index(self.list1.curselection()))
    def trans1(self):
        self.list2.insert(END,self.list1.get(self.list1.curselection()))
        self.list1.delete(self.list1.index(self.list1.curselection()))
        
    def trans2(self):
        self.list1.insert(END,self.list2.get(self.list2.curselection()))
        self.list2.delete(self.list2.index(self.list2.curselection()))
        
obj=demo()
