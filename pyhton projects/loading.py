from tkinter import *

import time
from tkinter.ttk import Progressbar
from login import login 
import threading
class loading:        
    def __init__(self):
        self.root=Tk()
        self.root.geometry("520x400+0+0")
        self.l1=Label(self.root,text="LOADING...",font=("Times New Roman",30,"bold"))
        self.l1.place(relx=0.47,rely=.10,anchor="center")
        self.l2=Label(self.root,text="It may take a while :-)",font=("Times New Roman",16,"bold"))
        self.l2.place(relx=0.455,rely=.2,anchor="center")
        self.v1=IntVar()
        self.p1=Progressbar(self.root,orient=HORIZONTAL,length=380,mode="determinate",maximum=100,variable=self.v1)
        self.p1.step(5)
        self.p1.place(relx=.240,rely=.40)
        tup=(101,)
        self.t1=threading.Thread(target=self.move,args=tup,name="first")
        self.t1.start()
        self.root.after(500,self.check)
        self.root.mainloop()
    def move(self,a):
        for i in range(a):
            self.v1.set(i)
            self.l3=Label(self.root,text=str(self.v1.get())+"%",font=("Times New Roman",30,"bold"))
            self.l3.place(relx=.9,rely=.09,anchor="center")
            time.sleep(.01)
    def check(self):
        if self.v1.get()!=100:
            self.root.after(500,self.check)
        else:
            self.p1.stop()
            self.root.destroy()
            onj=login()





