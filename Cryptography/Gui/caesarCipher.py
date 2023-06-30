#!/usr/bin python3
#Reverse Cipher GUI


#Libraries 
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

#Main Class
class Cipher(Tk):
    def __init__(self):
       super().__init__()
       self.height =550
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("Caesar Cipher")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.configure(bg='Silver')
       self.gui()

    def change_text_er(self):
        if(self.check_one.get() == 1):
            self.clicked.config(text="Encrypt")
            self.mode = 'encrypt'
    def change_text_dr(self):
        if(self.check_one.get() == 2):
            self.clicked.config(text="Decrypt")
            self.mode = 'decrypt'
    
        


    """The security function reverse the sentence or word put into the text box."""
    def security(self):
        message =  self.entry.get(1.0, "end-1c")
        translated = ""

        """Operation"""
        """Checked First Operation"""
        SPECIAL = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
        NORMAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if(self.check_one.get() == 0):
            messagebox.showerror("Required","Encrypt or Decrypt.")

        if(self.check_two.get() == 0):
            messagebox.showerror("Required","Special or Normal.")
        
        if(self.var.get() == 0):
            messagebox.showerror("Note","Key should not be zero.")

    

        if(self.check_two.get() == 1):
            LETTERS = SPECIAL
        elif(self.check_two.get() == 2):
            LETTERS = NORMAL

        #Key
        try:
            key = int(self.var.get())
        except:
            messagebox.showerror("Error","Key must a number.")

        message = message.upper()

        """Main Operation of the Cryptography"""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                if self.mode == "encrypt":
                    num = num + key
                elif self.mode == "decrypt":
                    num = num - key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)
                                    
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol



        """Outputing it into the Output text Box"""
        self.text_area.insert(END, translated)
        self.text_area.see(END)

    """The GUI setup for the App"""
    def gui(self):  
        self.check_one = IntVar()
        self.check_two = IntVar()
        self.var = IntVar()
    

        #Text Entry Box
        self.entry = Text( self,height=2,width=35,bg="#ffffff")
        self.entry.config(highlightcolor="white",relief="sunken")
        self.entry.place(x=25, y =30,height=150,width=450)
        """"""
        #frame 
        self.frameset_one = Frame(self, bg="green", width=120, height=60).place(x=120, y=190)
        self.select_encrypt = Radiobutton(self.frameset_one, text='Encrypt',width=10,cursor="hand2",
                                        variable=self.check_one,value=1,command=self.change_text_er).place(x=60, y=191)
        #checkbox 2
        self.select_decrypt = Radiobutton(self.frameset_one, text='Decrypt',width=10,cursor="hand2",
                                        variable=self.check_one,value=2,command=self.change_text_dr).place(x=60, y=220)

        """"""
        self.frameset_two = Frame(self, bg="red", width=120, height=60).place(x=240, y=190)
        self.text_hard = Radiobutton(self.frameset_two, text='Special',width=10,cursor="hand2",
                                        variable=self.check_two,value=1).place(x=320, y=191)
        
        """"""
        self.frameset_three = Frame(self, bg="yellow", width=120, height=60).place(x=180, y=190)
        Label(self,text = "Key",font = ("Times New Roman", 12),
              background = 'yellow',foreground = "black").place(x=205, y=200,width= 70)
        self.select_key = Entry(self.frameset_three,width= 5,highlightthickness=0,background = 'white',foreground = "black",
                                font = ("Times New Roman", 12),bd=0,justify="center",textvariable=self.var).place(x=220, y=225)
        #checkbox 2
        self.text_easy = Radiobutton(self.frameset_two, text='Normal',width=10,cursor="hand2",
                                        variable=self.check_two,value=2).place(x=320, y=220)


        #Button 
        self.clicked= Button(self,text = "",bg="#ffffff",font=("",10,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.security)
        self.clicked.place(x=190, y=260)
        #Label for the output
        Label(self,text = "CipherText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=295,width= 400)
        Label(self,text = "PlainText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=4,width= 400)
        #Output Box 
        self.text_area = scrolledtext.ScrolledText(self, wrap = WORD,width = 55,
                                               height = 10, font = ("Times New Roman", 12)
                                               ,highlightcolor="white",relief="sunken")
        self.text_area.place(x=25, y=325)
        # Placing cursor in the text area
        self.text_area.focus()
                
    

if __name__ == "__main__":
    root = Cipher()
    root.mainloop()