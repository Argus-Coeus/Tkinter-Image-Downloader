#!/usr/bin/python3
import hashlib
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

class Hashed(Tk):
    def __init__(self):
       super().__init__()
       self.height =170
       self.width = 305
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("HASHED PASSWORD ")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.gui()
    def hashedPassword(self):
        if(not self.passwordEntry.get() ):
            messagebox.showinfo("Required","Fill the entry box.")
        else:
            if(self.var.get() == 1):
                result = hashlib.md5(self.passwordEntry.get().encode())
                entry = result.hexdigest()
                self.label.insert(END,entry)
                self.label.config(fg="black",width=35)
            elif(self.var.get() == 2):
                result = hashlib.sha256(self.passwordEntry.get().encode())
                entry = result.hexdigest()
                self.label.insert(END,entry)
                self.label.config(fg="black",width=35)
            elif(self.var.get() == 3):
                result = hashlib.sha512(self.passwordEntry.get().encode())
                entry = result.hexdigest()
                self.label.insert(END,entry)
                self.label.config(fg="black",width=35)
            else:
                messagebox.showerror("Error","RadioButton Required")
    def gui(self): 
        self.var = IntVar()
        self.nameVar = StringVar()
        self.stringLabel = StringVar()
        self.passwordEntry = Entry(self,width=20,bd=5,font=("", 12))
        self.passwordEntry.config(highlightcolor="white",relief="sunken")
        self.passwordEntry.place(x=40, y =35)
        #########################################################################
        passwordButton = Button(self,text = "Done",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.hashedPassword)
        passwordButton.place(x=80, y=120)
        ############################################################################
        md5Button = Radiobutton(self,text="MD5", variable=self.var, value=1,
                  command="")
        md5Button.place(x=30, y=10)
        sha256Button = Radiobutton(self,text="SHA256", variable=self.var, value=2,
                  command="")
        sha256Button.place(x=90, y=10)
        sha543Button = Radiobutton(self,text="SHA532", variable=self.var, value=3,
                  command="")
        sha543Button.place(x=170, y=10)
        ############################################################################
        
        self.label = Text( self,height=2,width=35,bg="#ffffff")
        self.label.place(x=10, y=70)

            

if __name__ == "__main__":
    root = Hashed()
    root.mainloop()