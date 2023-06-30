#!/usr/bin/python3
import hashlib
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from pathlib import Path

class Hashed(Tk):
    def __init__(self):
       super().__init__()
       self.height =250
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("HASHED PASSWORD ")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.gui()
    def hashedCracker(self):
        #Assigning entry to the variable
        if(self.passwordEntry.get() and self.passwordEntry2.get()):
            wlist = self.passwordEntry2.get()
            hash2crack = self.passwordEntry.get()
        else:
            messagebox.showinfo("Required","Fill the all the entry boxes.")

        #Read file
        p = Path(__file__).with_name(wlist)
        wlistlines = p.open("r").readlines()

        #loop
        """***********************************************************************************"""
        password_found = False

        if(self.var.get() == 1):
            for dictionary_value in wlistlines:
                hashed_value = (hashlib.md5(dictionary_value.encode())).hexdigest()
                if hashed_value == hash2crack:
                    password_found = True
                    recovered_password = dictionary_value

            if password_found == True:
                self.label.config(text= recovered_password ,fg="black")
            else:
                messagebox.showinfo("Password Match","Not Found")
       
        elif(self.var.get() == 2):
            for dictionary_value in wlistlines:
                hashed_value = (hashlib.sha256(dictionary_value.encode())).hexdigest()
                if hashed_value == hash2crack:
                    password_found = True
                    recovered_password = dictionary_value

            if password_found == True:
                self.label.config(text= recovered_password ,fg="black")
            else:
                messagebox.showinfo("Password Match","Not Found")
       
        elif(self.var.get() == 3):
            for dictionary_value in wlistlines:
                hashed_value = (hashlib.sha512(dictionary_value.encode())).hexdigest()
                if hashed_value == hash2crack:
                    password_found = True
                    recovered_password = dictionary_value

            if password_found == True:
                self.label.config(text= recovered_password ,fg="black")
            else:
                messagebox.showinfo("Password Match","Not Found")
       
        else:
            messagebox.showerror("Error","RadioButton Required")
    
       

    
    def gui(self): 
        self.var = IntVar()
        self.nameVar = StringVar()
        self.passwordEntry = Entry(self,width=30,bd=5,font=("", 12))
        self.passwordEntry.config(highlightcolor="white",relief="sunken")
        self.passwordEntry.place(x=40, y =35)
        ########################################################################
        self.passwordEntry2 = Entry(self,width=30,bd=5,font=("", 12))
        self.passwordEntry2.config(highlightcolor="white",relief="sunken")
        self.passwordEntry2.place(x=40, y =75)
        #########################################################################
        passwordButton = Button(self,text = "Done",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.hashedCracker)
        passwordButton.place(x=170, y=170)
        ############################################################################
        md5Button = Radiobutton(self,text="MD5", variable=self.var, value=1,
                  command="")
        md5Button.place(x=30, y=10)
        sha256Button = Radiobutton(self,text="SHA256", variable=self.var, value=2,
                  command="")
        sha256Button.place(x=150, y=10)
        sha543Button = Radiobutton(self,text="SHA532", variable=self.var, value=3,
                  command="")
        sha543Button.place(x=270, y=10)
        ############################################################################
        self.label = Label( self, text = "HASHED", relief=RAISED,height=2,width=11,bg="#ffffff" )
        self.label.place(x=380, y=30)
        self.label = Label( self, text = "WORDLIST", relief=RAISED,height=2,width=11,bg="#ffffff" )
        self.label.place(x=380, y=75)
        ###############################################################################
        self.label = Label( self, text = "", relief=RAISED,height=2,width=58,bg="#ffffff" )
        self.label.place(x=15, y=120)

            

if __name__ == "__main__":
    root = Hashed()
    root.mainloop()