#!/usr/bin python3
#Reverse Cipher GUI


#Libraries 
from tkinter import *
from tkinter import scrolledtext

#Main Class
class Cipher(Tk):
    def __init__(self):
       super().__init__()
       self.height =450
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("Reverse Cipher")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.gui()

    """The security function reverse the sentence or word put into the text box."""
    def security(self):
        message =  self.entry.get(1.0, "end-1c")
        translated = ""

        """Checking for symbol"""


        #Operation
        i = len(message) - 1
        while i >= 0: 
            translated = translated + message[i]
            i = i -1
        
        """Outputing it into the Output text Box"""
        self.text_area.insert(END, translated)
        self.text_area.see(END)


 



    """The GUI setup for the App"""
    def gui(self):  
        #Text Entry Box
        self.entry = Text( self,height=2,width=35,bg="#ffffff")
        self.entry.config(highlightcolor="white",relief="sunken")
        self.entry.place(x=25, y =30,height=150,width=450)
        #Button 
        self.clicked= Button(self,text = "Reverse",bg="#ffffff",font=("",10,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.security)
        self.clicked.place(x=190, y=185)
        #Label for the output
        Label(self,text = "PlainText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=4,width= 400)
        Label(self,text = "CipherText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=225,width= 400)
        #Output Box 
        self.text_area = scrolledtext.ScrolledText(self, wrap = WORD,width = 55,
                                               height = 7, font = ("Times New Roman", 12)
                                               ,highlightcolor="white",relief="sunken")
        self.text_area.place(x=25, y=255)
        # Placing cursor in the text area
        self.text_area.focus()
                
        

if __name__ == "__main__":
    root = Cipher()
    root.mainloop()