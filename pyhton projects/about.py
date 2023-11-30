from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import beforeuser
class us:
    def __init__(self):                     ###############this is a comment
        
        self.root=Tk()
        self.root.title("SEARCH")
        self.root.config(background="lightcyan")
        self.root.geometry("750x600+0+0")
        self.ll=Label(self.root)
        self.ll.pack()
        self.ii2=ImageTk.PhotoImage(Image.open("images\\team back.jpg").resize((500,80),Image.ANTIALIAS))
        self.ll.config(image=self.ii2)
        self.l2=Label(self.root,text="ABOUT US",font=("Times New Roman",65,"bold"),background="lightcyan")
        self.l2.place(relx=0.5,rely=0.23,anchor="center")
        self.b1=Button(self.root,text="  BACK  ",command=self.back)
        self.b1.place(relx=0.5,rely=0.5,anchor="center")
    def back(self):
        self.root.destroy()
        onj=beforeuser.buttons()
#obj=us()
