#!/usr/bin python3
#Brute Force for the ceasar cipher
#Libraries 
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time

#Main Class
class BruteForce(Tk):
    def __init__(self):
       super().__init__()
       self.height =500
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("Caesar Cipher")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.configure(bg='Silver')
       self.gui()
 
    """The security function reverse the sentence or word put into the text box."""
    def security(self):
        message =  self.entry.get(1.0, "end-1c")
       

        """Operation"""
        """Checked First Operation"""

                #         #appending the character to the translated
                #         translated = translated + LETTERS[num]

                #     else:
                #         #Adding the characters in the message to the translated
                #         translated = translated + symbol
                # #displaying the number of keys and the message decoded
                # ciphertext = f"key: {key} : {translated} \n"
                # """Outputing it into the Output text Box"""
                # self.text_area.insert(END, ciphertext)
                # self.text_area.see(END)
                # self.update_idletasks()
                # self.progress['value'] += 4
                # time.sleep(1)
                # self.txt.config(text=f"{int(self.progress['value'])}%")
                
        if self.txt['text'] == "100%":
            self.txt.config(text="Done")
            self.progress['value'] = 0

    """The GUI setup for the App"""
    def gui(self):  
        #Radiobutton textvariable
        self.check_one = IntVar()
        #Text Entry Box
        self.entry = Text( self,height=2,width=35,bg="#ffffff")
        self.entry.config(highlightcolor="white",relief="sunken")
        self.entry.place(x=25, y =30,height=150,width=450)
        """"""
        #Button 
        self.clicked= Button(self,text = "Brute-Force",bg="#ffffff",font=("",10,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.security)
        self.clicked.place(x=190, y=185)
        #progress 
        self.progress = Progressbar(self, orient=HORIZONTAL, length=407, mode='determinate')
        self.progress.place(x=25, y=250)
        #Percentage
        self.txt = Label(self,text = '0%', bg = 'yellow', fg = 'black')
        self.txt.place(x=433,y=248,width=50)

        #Label for the output
        Label(self,text = "CipherText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=220,width= 400)
        Label(self,text = "PlainText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=4,width= 400)
        #Output Box 
        self.text_area = scrolledtext.ScrolledText(self, wrap = WORD,width = 55,
                                               height = 10, font = ("Times New Roman", 12)
                                               ,highlightcolor="white",relief="sunken")
        self.text_area.place(x=25, y=280)
        # Placing cursor in the text area
        self.text_area.focus()
                
    

if __name__ == "__main__":
    root = BruteForce()
    root.mainloop()