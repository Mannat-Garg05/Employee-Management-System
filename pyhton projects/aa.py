from tkinter import*
from tkinter.ttk import*
from tkinter import filedialog
class demo:
    def __init__(self):
        self.root=Tk()
        
        self.root.state("normal")

        self.t1=Text(self.root)
        self.t1.grid(row=0,column=0,sticky="nsew")
        self.root.resizable(False,False)

        #self.root.option_add(*tearoff,False)

        #this is make the menu bar
        self.mb=Menu(self.root)

        #this is to add menu into the menu bar
        self.root.config(menu=self.mb)
        self.f1=Menu(self.mb)
        self.e1=Menu(self.mb)
        self.ff1=Menu(self.mb)
        self.r1=Menu(self.mb)
        self.o1=Menu(self.mb)
        self.h1=Menu(self.mb)
        self.w1=Menu(self.mb)

        #this gives name to the menu added to the menu bar
        self.mb.add_cascade(menu=self.f1,label="File")
        self.mb.add_cascade(menu=self.e1,label="edit")
        self.mb.add_cascade(menu=self.ff1,label="Format")
        self.mb.add_cascade(menu=self.r1,label="run")
        self.mb.add_cascade(menu=self.o1,label="option")
        self.mb.add_cascade(menu=self.w1,label="window")
        self.mb.add_cascade(menu=self.h1,label="help")

        #this is to add command inside the menu
        self.f1.add_command(label="new",command=lambda: self.new(10))
        self.f1.add_command(label="open",command=self.open)
        
        self.s1=Menu(self.f1)
        self.f1.add_cascade(menu=self.s1,label="save")
        self.s1.add_command(label="save as",command=self.save)
        self.s1.add_command(label="save all")
        
        self.f1.entryconfig("new",accelerator="Ctrl+N")
        self.root.bind_all("<Control-n>",self.new)
        self.sc=Scrollbar(self.root,orient=VERTICAL,command=self.t1.yview)
        self.sc.grid(row=0,column=1,sticky="ns")
        self.t1.config(yscrollcommand=self.sc.set)
        self.sc=Scrollbar(self.root,orient=HORIZONTAL,command=self.t1.xview)
        self.sc.grid(row=1,column=0,sticky="ew")
        self.t1.config(xscrollcommand=self.sc.set)
        
    def new(self,a):
        print("new")
    def open(self):
        f=filedialog.askopenfile(initialdir="c:\\",title="Select file",filetypes=("all files","*.*"))
        print(f)
        pass
    def save(self):
        f=filedialog.askopenfile(initialdir="c:\\",title="Select file",filetypes=(("all files","*.*")))
        print(f)
        
        
        
obj=demo()
