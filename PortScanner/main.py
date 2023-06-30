#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import socket
import sys
import threading
from queue import Queue
import time


class Hashed(Tk):
    def __init__(self):
       super().__init__()
       self.height = 350
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("PORT NAME FINDER ")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.storage = []
       self.store = []
       self.gui()
       self.runner()


    def runner(self):
        socket.setdefaulttimeout(0.25)
        self.lock = threading.Lock()

        
    def finder(self,port):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            con = sock.connect((self.portEntry.get(),port))
            with self.lock:
                print(port,"is open")
            con.close()
        except:
            pass

    def execute(self):
        while True:
            worker = self.queue.get()
            self.finder(worker)
            self.queue.task_done()
    def runner_script(self):
        #####################################################
        self.label_scan = Label( self, text = "Scanning...",relief=RAISED,height=1,width=40,bg="#ffffff" )
        self.label_scan.place(x=100, y=120)
        self.queue = Queue()
        self.start_time = time.time()

        for x in range(100):
            thread = threading.Thread(target = self.execute)
            thread.daemon = True
            thread.start()

        for worker in range(1,1024):
            self.queue.put(worker)
        
        self.queue.join()

        print('Time taken:',time.time()- self.start_time)



           




    def gui(self): 
        self.label = Label( self, text = "IP Address",relief=RAISED,height=1,width=40,bg="#ffffff" )
        self.label.place(x=100, y=9)
        """Entry for the port"""
        self.portEntry = Entry(self,width=30,bd=5,font=("", 12))
        self.portEntry.config(highlightcolor="white",relief="sunken")
        self.portEntry.place(x=105, y =30)
         ############################################################################
        """Button for the port to Submit"""
        port_button = Button(self,text = "Submit",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=7,relief="raised",command=self.runner_script)
        port_button.place(x=210, y=70)
        """Declaring the treeview for the App """
        columns = ('PORT', 'OPEN')
        self.tree = ttk.Treeview(self, columns=columns, show='headings',height = 6,selectmode=BROWSE)
        # define headings
        self.tree.heading('PORT', text='PORT')
        self.tree.heading('OPEN', text='OPEN')
        self.tree.place(x=50, y=140)
        #add a scrollbar
        self.scrollbar = ttk.Scrollbar(self,orient=VERTICAL,command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=452,y=140,height=142)
        
      
            

if __name__ == "__main__":
    root = Hashed()
    root.mainloop()