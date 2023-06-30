#!/usr/bin python3
#Brute Force for the ceasar cipher
#Libraries 
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import math

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


        if(self.check_one.get() == 0):
            messagebox.showerror("Required","Encrypt or Decrypt.")
       

        """Operation"""
        """Checked First Operation"""

        #Key
        try:
            key = int(self.var.get())
        except:
            messagebox.showerror("Error","Key must a number.")
        
        if(self.mode == "encrypt"):
            #ciphertext
            cipherText =  self.encryptMessage(key,message)
            #print ciphertext
            self.text_area.insert(END, cipherText)
            self.text_area.see(END)
        elif(self.mode == "decrypt"):
            plainText =  self.decryptMessage(key,message)
            self.text_area.insert(END, plainText)
            self.text_area.see(END)



    #The decryption function
    def decryptMessage(self,key,message):
        #finding the ceiliing number of the message divided by the key 
        numOfColumns  = math.ceil(len(message)/key)
        # Storing the key inside the number of col
        numOfRows  = key
        #Finding the number of shadow boxes in the plaintext
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
        #Arrange in the plaintext
        plaintext = [''] * numOfColumns
        #Col and Row
        col = 0 
        row = 0
        #Looping in the message
        for symbol in message:
            plaintext[col] += symbol
            col += 1

            #Arranging the ciphertext to it's normal plaintext
            if (col == numOfColumns) or (col == numOfColumns - 1 and
                                        row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)
        
    
    def encryptMessage(self,key,message):
        ciphertext = [''] * key
        #Looping the columns
        for col in range(key):
            pointer = col
            #Looping to check the if the size of the message is less than the pointer
            while pointer < len(message):
                #stores it into the ciphertext by indexing
                ciphertext[col] += message[pointer]
                #Incresing the pointer in each iteration
                pointer += key
        #Return the ciphertext
        return ''.join(ciphertext)
       

    """The GUI setup for the App"""
    def gui(self):  
        #Radiobutton textvariable
        self.check_one = IntVar()
        self.var = IntVar()
        #Text Entry Box
        self.entry = Text( self,height=2,width=35,bg="#ffffff")
        self.entry.config(highlightcolor="white",relief="sunken")
        self.entry.place(x=25, y =30,height=150,width=450)
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
        self.clicked.place(x=190, y=225)
        

        #Label for the output
        Label(self,text = "CipherText",font = ("Times New Roman", 12), 
              background = 'white',foreground = "black").place(x=50, y=255,width= 400)
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