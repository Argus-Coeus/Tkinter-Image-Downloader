#!/usr/bin/python3
import hashlib
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from tkinter import ttk
import socket
import sys
class Hashed(Tk):
    def __init__(self):
       super().__init__()
       self.height = 300
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("PORT NAME FINDER ")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.newlist = []
       self.gui()
    def finder(self):

        """
        This is the main operation method for the determining the port names for the App
        """

        storage = {"21":"","22":"","23":"","25":"","53":""
                        ,"69":"","80":"","67":"","68":"","110":"","119":"","123":"","135":""
                        ,"139":"","161":"","162":"","389":"","443":"","143":"","3389":"","179":"","194":""
                        ,"3389":"","2":"","38":"","39":"","42":"","3022":"","445":"","1026":"","1701":"","1732":""
                        ,"135":""}
        self.port_protocol = "tcp"
        try:
            serviceName = socket.getservbyport(int(self.portEntry.get()),self.port_protocol)
            storage[self.portEntry.get()] = serviceName
            self.newlist.append((self.portEntry.get(),serviceName))
            branding = (self.portEntry.get(),storage[self.portEntry.get()])
            self.tree.insert('',END,values=branding)
           

        except KeyboardInterrupt:
            messagebox.showerror("Error","Exiting Program")
        except socket.gaierror:
            messagebox.showerror("Error","Port could not be resolved!!!")
        except ValueError:
            messagebox.showerror("Input Error","Enter a valid port number.")
        except OverflowError:
            messagebox.showerror("Overflow Error","Port must be 0-65535")
        except socket.error:
            messagebox.showerror("Error","Server not responding!!!")
           
            

            
    def gui(self): 
        """Label for the port"""
        self.label = Label( self, text = "PORT",relief=RAISED,height=1,width=40,bg="#ffffff" )
        self.label.place(x=100, y=9)
        """Entry for the port"""
        self.portEntry = Entry(self,width=30,bd=5,font=("", 12))
        self.portEntry.config(highlightcolor="white",relief="sunken")
        self.portEntry.place(x=105, y =35)
        """Button for the port to Submit"""
        port_button = Button(self,text = "Submit",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=7,relief="raised",command=self.finder)
        port_button.place(x=210, y=75)
        """Declaring the treeview for the App """
        columns = ('PORT', 'NAME')
        self.tree = ttk.Treeview(self, columns=columns, show='headings',height = 6,selectmode=BROWSE)
        # define headings
        self.tree.heading('PORT', text='PORT')
        self.tree.heading('NAME', text='NAME')
        self.tree.place(x=50, y=130)
        #add a scrollbar
        self.scrollbar = ttk.Scrollbar(self,orient=VERTICAL,command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=452,y=130,height=141)
            

if __name__ == "__main__":
    root = Hashed()
    root.mainloop()