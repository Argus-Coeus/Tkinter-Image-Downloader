#!/usr/bin python3
from pylibrary.transposition import Transposition
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
import re


#Main Class
class TranspositionFiles(Tk):
    def __init__(self):
       super().__init__()
       self.height = 350
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("Caesar Cipher")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.configure(background= "gray")
       self.gui()
 
    def change_text_er(self):
        if(self.check_one.get() == 1):
            self.clicked.config(text="Encrypt")
            self.mode = 'encrypt'
    
          
        
    def change_text_dr(self):
        if(self.check_one.get() == 2):
            self.clicked.config(text="Decrypt")
            self.mode = 'decrypt'

    def check_input_file(self):
        if not re.match("^[a-z]*$", self.input_file.get()):
            messagebox.showerror("Alert","Only letters a-z allowed!")
        else:
            if not os.path.exists(self.input_file.get()):
                messagebox.showerror("Alert",f'The file {self.input_file.get()} does not exit.')
            else:
                    fileObj = open(self.input_file.get())
                    self.content = fileObj.read()
                    fileObj.close()
        
    
            
    
    def check_input_save(self):
        if not re.match("^[a-z]*$", self.input_save.get()):
            messagebox.showerror("Alert","Only letters a-z allowed!")
        else:
            if os.path.exists(f'saved/{self.input_save.get()}'):
                response = messagebox.askyesno("Question",f'This will overwrite the files {self.input_save.get()}. (C)ontinue or (Q)uit?')
                if response == 1 :
                    self.verify_file_save = self.input_save.get()
                elif response == 2:
                    messagebox.showinfo("Info","You are not ready yet.")
                    self.verify_file_save = ""
            else:
                outputFileObj = open(f'saved/{self.input_save.get()}','w')
                outputFileObj.write(self.translated)
                outputFileObj.close()

    """The security function reverse the sentence or word put into the text box."""
    def security(self):
        # message =  self.entry.get(1.0, "end-1c")

        if(self.check_one.get() == 0):
            messagebox.showerror("Required","Encrypt or Decrypt.")
        """Operation"""
        """Checked First Operation"""
        #Key
        try:
            key = int(self.var.get())
        except:
            messagebox.showerror("Error","Key must a number.")

        self.check_input_file()

        if self.mode == 'encrypt':
            self.translated = Transposition.encryptMessage(key,self.content)
        elif self.mode == 'decrypt':
            self.translated  = Transposition.decryptMessage(key,self.content)


        self.check_input_save()

    def preview_func(self):
        if (self.input_save.get() == ""):
            messagebox.showerror("Error","Give a name to cipher text.")
        else:
            if os.stat(f'saved/{self.input_save.get()}').st_size == 0:
                messagebox.showerror("Alert","The File is empty.")
            else:
                #Text Entry Box
                self.text_area = scrolledtext.ScrolledText(self, wrap = WORD,width = 55,
                                                height = 7, font = ("Times New Roman", 12)
                                                ,highlightcolor="white",relief="sunken")
                self.text_area.place(x=25, y=25)
                Label(self,text = "CipherText Review",font = ("Times New Roman", 12), 
                    background = 'white',foreground = "black").place(x=50, y=2,width= 400)
                self.review()
                
    def review(self):
        self.text_area.insert(END, self.translated)
        self.text_area.see(END)
                


        
    """The GUI setup for the App"""
    def gui(self):  
        #Radiobutton textvariable
        self.check_one = IntVar()
        self.var = IntVar()
        self.input_file = StringVar()
        self.input_save = StringVar()
        """"""
        self.frameset_one = Frame(self, bg="yellow", width=130, height=30).place(x=180, y=190)
        self.frameset_two = Frame(self, bg="red", width=130, height=30).place(x=50, y=190)
        self.frameset_three = Frame(self, bg="green", width=130, height=30).place(x=300, y=190)
        #RadioButton
        self.text_hard = Radiobutton(self.frameset_one, text='Encrypt',width=10,cursor="hand2",
                                        variable=self.check_one,value=1,command=self.change_text_er).place(x=100, y=194)
        self.text_easy = Radiobutton(self.frameset_one, text='Decrypt',width=10,cursor="hand2",
                                                variable=self.check_one,value=2,command=self.change_text_dr).place(x=280, y=194)

        self.select_key = Entry(self.frameset_one,width= 5,highlightthickness=0,background = 'white',foreground = "black",
                                font = ("Times New Roman", 12),bd=0,justify="center",textvariable=self.var).place(x=225, y=194)
        #Button 
        self.clicked= Button(self,text = "",bg="#ffffff",font=("",10,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.security)
        self.clicked.place(x=190, y=270)
        #Preview
        self.preview = Button(self,text = "Preview",bg="#ffffff",font=("",10,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=20,relief="raised",command=self.preview_func)
        self.preview.place(x=150, y=305)

        #Files Entries 
        #Label
        Label(self,text = "File",font = ("courier", 12), 
              background = 'white',foreground = "black").place(x=45, y=236,width= 50)
        Label(self,text = "Saved As",font = ("courier", 12), 
              background = 'white',foreground = "black").place(x=240, y=236,width= 85)

        #File to be encrypted
        self.file_entry = ttk.Entry(self, textvariable = self.input_file ,justify = CENTER,font = ('courier', 12, 'bold'))
        self.file_entry.focus_force()
        self.file_entry.place(x=100, y=235,height=25,width=130)
        #Save File 
        self.file_save = ttk.Entry(self, textvariable = self.input_save ,justify = CENTER,font = ('courier', 12, 'bold'))
        self.file_save.focus_force()
        self.file_save.place(x=330, y=235,height=25,width=130)
        #progress 
        self.progress = Progressbar(self, orient=HORIZONTAL, length=407, mode='determinate')
        self.progress.place(x=25, y=168)
        #Percentage
        self.txt = Label(self,text = '0%', bg = 'silver', fg = 'black')
        self.txt.place(x=433,y=168,width=50)


if __name__ == "__main__":
    root = TranspositionFiles()
    root.mainloop()