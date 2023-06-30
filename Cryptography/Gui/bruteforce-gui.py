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
       self.height =530
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
        SPECIAL = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
        NORMAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        #*********************
        if(self.check_one.get() == 0):
            messagebox.showerror("Required","Special or Normal.")
        else:
            if(self.check_one.get() == 1):
                LETTERS = SPECIAL
            elif(self.check_one.get() == 2):
                LETTERS = NORMAL

            #Looping into the keys 
            for key in range(1,len(LETTERS)):
                
                translated = ""

                #Looping into the message
                for symbol in message:
                    #Checking  if the characters in the message is in the letters
                    if symbol in LETTERS:
                        num = LETTERS.find(symbol)
                        num = num - key
                        #Checking if num is greater than 0
                        if num < 0:
                            num = num + len(LETTERS)

                        #appending the character to the translated
                        translated = translated + LETTERS[num]

                    else:
                        #Adding the characters in the message to the translated
                        translated = translated + symbol
                #displaying the number of keys and the message decoded
                ciphertext = f"key: {key} : {translated} \n"
                """Outputing it into the Output text Box"""
                self.text_area.insert(END, ciphertext)
                self.text_area.see(END)
                self.update_idletasks()
                self.progress['value'] += 4
                time.sleep(1)
                self.txt.config(text=f"{int(self.progress['value'])}%")
                
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
        self.frameset_one = Frame(self, bg="yellow", width=130, height=30).place(x=180, y=190)
        #RadioButton
        self.text_hard = Radiobutton(self.frameset_one, text='Special',width=10,cursor="hand2",
                                        variable=self.check_one,value=1).place(x=130, y=194)
        self.text_easy = Radiobutton(self.frameset_one, text='Normal',width=10,cursor="hand2",
                                                variable=self.check_one,value=2).place(x=250, y=194)

        #Button 
        self.clicked= Button(self,text = "Brute-Force",bg="#ffffff",font=("",10,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command=self.security)
        self.clicked.place(x=190, y=225)
        #progress 
        self.progress = Progressbar(self, orient=HORIZONTAL, length=407, mode='determinate')
        self.progress.place(x=25, y=290)
        #Percentage
        self.txt = Label(self,text = '0%', bg = 'silver', fg = 'black')
        self.txt.place(x=433,y=288,width=50)

        #Label for the output
        Label(self,text = "CipherText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=260,width= 400)
        Label(self,text = "PlainText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=4,width= 400)
        #Output Box 
        self.text_area = scrolledtext.ScrolledText(self, wrap = WORD,width = 55,
                                               height = 10, font = ("Times New Roman", 12)
                                               ,highlightcolor="white",relief="sunken")
        self.text_area.place(x=25, y=310)
        # Placing cursor in the text area
        self.text_area.focus()
                
    

if __name__ == "__main__":
    root = BruteForce()
    root.mainloop()