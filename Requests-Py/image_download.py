#!/usr/bin python3
#Reverse Cipher GUI


#Libraries 
from tkinter import *
from tkinter import messagebox
import os
import re
import requests

#Main Class
class Img(Tk):
    def __init__(self):
       super().__init__()
       self.height =190
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("Image Download App")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.configure(bg='Silver')
       self.gui()

   
    
    def display_selected(self, *args):
        choice = self.choose.get()
        return choice
    

    def operation(self):
        #**********************************************************


        #Assigning entry to the variable
        if(self.name_url.get()):
            res = requests.get(f'{self.name_url.get()}')
            if res.status_code // 100 == 2:
                saved = res.content

                if not re.match("^[a-z]*$", self.name_saved.get()):
                    messagebox.showerror("Alert","Only letters a-z allowed!")
                else:
                    if os.path.exists(f'saved/{self.name_saved.get()}.{self.display_selected()}'):
                        response = messagebox.askyesno("Question",f'This will overwrite the files {self.name_saved.get()}. (C)ontinue or (Q)uit?')
                        if response == 1 :
                            self.verify_file_save = self.name_saved.get()
                        elif response == 2:
                            messagebox.showinfo("Info","You are not ready yet.")
                            self.verify_file_save = ""
                    else:
                        outputFileObj = open(f'{self.name_saved.get()}.{self.display_selected()}','wb')
                        outputFileObj.write(saved)
                        outputFileObj.close()
            else:
                messagebox.showerror("Connection Error","Make sure, you are connected to the internet.")
        else:
            messagebox.showinfo("Required","Provide a URL.")

        if(self.name_url.get() == "" and self.name_url.get() == "" ):
            messagebox.showinfo("Required","Fill the all the entries.")
        


        

        #********************************************************
        

    """The GUI setup for the App"""
    def gui(self):  
        self.name_url = StringVar()
        self.name_saved = StringVar()
        self.choose = StringVar()
        # setting variable for Integers
        self.countries = ("png","jpg")
        self.choose.set(self.countries[0])
        # creating widget
        select_option = OptionMenu(self,self.choose,*self.countries,command=self.display_selected)
        select_option.place(x=395, y =75,width=70)
        self.urlEntry = Entry(self,width=38,bd=5,font=("", 12))
        self.urlEntry.config(highlightcolor="white",relief="sunken",textvariable=self.name_url)
        self.urlEntry.place(x=70, y =35)
        #************************************************************************
        self.passwordSaved = Entry(self,width=38,bd=5,font=("", 12))
        self.passwordSaved.config(highlightcolor="white",relief="sunken",textvariable=self.name_saved)
        self.passwordSaved.place(x=140, y =75,width=250)
        #########################################################################
        passwordButton = Button(self,text = "Done",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.operation)
        passwordButton.place(x=180, y=120)
        ############################################################################
        Label(self,text = "Image Download App",font = ("Times New Roman", 12), 
              background = 'white',foreground = "Black",justify = CENTER).place(x=50, y=4,width= 400)
    
        Label(self,text = "URL :",font = ("Times New Roman", 12), 
              background = 'white',foreground = "Black",justify = CENTER).place(x=20, y=41,width= 45)
        Label(self,text = "Save As :",font = ("Times New Roman", 12), 
              background = 'white',foreground = "Black",justify = CENTER).place(x=60, y=81,width= 70)
    

if __name__ == "__main__":
    root = Img()
    root.mainloop()
