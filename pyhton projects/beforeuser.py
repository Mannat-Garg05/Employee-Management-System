from tkinter import *
from tkinter.ttk import Combobox

from tkinter import messagebox
from PIL import Image,ImageTk
import userentry
import depoist
import close
import update
import transfer
import withdraw
import search
import editpass
import secset
import PROFILE
import about
class buttons:
    def __init__(self):
        self.root=Tk()
        self.root.title("HOME")
        self.root.geometry("450x400+0+0")
        self.l1=Label(self.root)
        self.l1.pack()

        self.iii2=ImageTk.PhotoImage(Image.open("images\\banking.jpg").resize((1200,440),Image.ANTIALIAS))


        self.l1.config(image=self.iii2)


        self.mb=Menu(self.root)
        self.root.config(menu=self.mb)
        self.f1=Menu(self.mb)
        self.e1=Menu(self.mb)
        self.ff1=Menu(self.mb)
        self.h1=Menu(self.mb)

        self.mb.add_cascade(menu=self.f1,label="ACCOUNT")
        self.mb.add_cascade(menu=self.e1,label="TRANSACTIONS")
        self.mb.add_cascade(menu=self.ff1,label="ADMIN")
        self.mb.add_cascade(menu=self.h1,label="HELP")
        self.f1.add_command(label="NEW ACCOUUNT",command=self.new)
        self.f1.add_command(label="DELETE ACCOUNT",command=self.deldata)
        self.f1.add_command(label="UPDATE ACCOUUNT",command=self.update)
        self.f1.add_command(label="VIEW ALL ACCOUNTS",command=self.search)
        self.f1.add_command(label="SEARCH",command=self.search)

        self.e1.add_command(label="WITHDRAW",command=self.withd)
        self.e1.add_command(label="DEPOSIT",command=self.dep)
        self.e1.add_command(label="TRANSFER",command=self.transfer1)
        self.e1.add_command(label="MINI STATEMENT",command=self.min)

        self.ff1.add_command(label="EDIT PROFILE",command=self.pro)
        self.ff1.add_command(label="EDIT PASSWORD",command=self.editp)
        self.ff1.add_command(label="EDIT SECURITY SETTINGS",command=self.set)
        self.ff1.add_command(label="LOGOUT",command=self.logout)

        self.h1.add_command(label="ABOUT US",command=self.ab)
    def min(self):
        self.root.destroy()
        obj=minstat.mini()
    def new(self):
        self.root.destroy()
        obj=userentry.userpage()
    def ab(self):
        self.root.destroy()
        obj=about.us()
    def update(self):
        self.root.destroy()
        obj=update.up()
    def deldata(self):
        self.root.destroy()
        obj=close.closeacc()

    def logout(self):
        self.root.destroy()
        obj=login.login()

    def dep(self):
        self.root.destroy()
        obj=depoist.depmoney()
    def transfer1(self):
        self.root.destroy()
        obj=transfer.transmoney()
    def withd(self):
        self.root.destroy()
        obj=withdraw.withmoney()
    def search(self):
        self.root.destroy()
        obj=search.view()
    def editp(self):
        self.root.destroy()
        obj=editpass.edit()
    def set(self):
        self.root.destroy()
        obj=secset.security()
    def pro(self):
        self.root.destroy()
        obj=PROFILE.editp()


#OBJ=buttons()
