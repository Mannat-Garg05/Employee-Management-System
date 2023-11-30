from tkinter import *
from PIL import Image,ImageTk
from loading import loading


class wel:
    def __init__(self):
        self.root=Tk()
        self.root.state("zoomed")
        self.root.title("welcome")    
        self.l1=Label(self.root)
        self.l1.pack()
        
        self.b1=Button(self.root,text="CLICK TO ENTER",width=132,height=2,relief=RAISED,command=self.show)
        self.b1.pack()
        self.b1.config(background="lightcyan",foreground="coral",font=("Times New Roman",12,"bold","underline"))
        
    def show(self):
        self.root.destroy()
        obj1=loading()
obj=wel()        
