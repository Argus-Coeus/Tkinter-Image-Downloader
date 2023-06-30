#!/usr/bin/python3

#!/usr/bin/python3
import socket
import subprocess
import sys
from datetime import datetime
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from pathlib import Path
from tkinter import ttk

class Hashed(Tk):
    def __init__(self):
       super().__init__()
       self.height =650
       self.width = 500
       self.x =(self.winfo_screenwidth()//2) - (self.width//2)
       self.y =(self.winfo_screenheight()//2) - (self.height//2)
       self.title("PORT ENUMERATOR")
       self.geometry('{}x{}+{}+{}'.format(self.width,self.height,self.x,self.y))
       self.resizable(False,False)
       self.protocol_port = {21:"FTP",22:"SSH",25:"SMTP",43:"WHOIS",53:"DNS",80:"HTTP",88:"KERBEROS",110:"POP3",691:"MS_EXCHANGE",
       873:"RSYNC",1025:"RPC",3306:"MYSQL",111:"RFC",8080:"HTTP",143:"IMAP",139:"NetBIOS",161:"SNMP",162:"SNMP"}
       self.storage = []
       #Apppending to the port optionmenu for further enumeration
       self.store = []
       self.gui()

    def select_itemPort(self,*arg):
        print(self.port_var.get())
        self.clicked_port  = int(self.port_var.get())
        
        """This loop seaches for the port name for the selected port. This open the script combobox 
        so to select the script to use."""
        for key,value in self.protocol_port.items():
            if self.clicked_port == key:
                self.store_ip = value
                """SCRIPT NAME"""
                self.script_name = Label( self, text = self.store_ip, relief=RAISED,height=1,width=30,bg="#ffffff" )
                self.script_name.place(x=130, y=247)
                print(self.store_ip)
                break
    def open_script(self):
        pass

    def select_itemIp(self,*arg):
        print(self.ip_var.get())
        self.clicked_ip = self.ip_var.get()


    def portScanner(self):
       
        try:
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                #return an error indicator
                result = s.connect_ex((self.ipEntry.get(),port))
                if result == 0:
                    self.storage.append((f'{port}',f'{"Open"}'))
                    self.store.append(port)
                    print(f"Port {port} is open")
                    print(self.store)
                s.close()

        except KeyboardInterrupt:
            messagebox.showerror("Error","Exiting Program")
        except socket.gaierror:
            messagebox.showerror("Error","Hostname could not be resolved!!!")
        except socket.error:
            messagebox.showerror("Error","Server not responding!!!")
            sys.exit()
            
        for store in self.storage:
            self.tree.insert('',END,values=store)
        # initial menu text for the port
        self.port_var = StringVar()
        option_menu1 = ttk.Combobox(self,values=self.store,textvariable=self.port_var,state='readonly')
        option_menu1.place(x=320, y=270,width=140)
        # initial menu text for the ip_address
        self.ip_var = StringVar()
        option_ip = ttk.Combobox(self,values=self.ipEntry.get(),textvariable=self.ip_var,state='readonly')
        option_ip.place(x=320, y=324,width=140)

        # Set the tracing for the given variable
        self.port_var.trace('w', self.select_itemPort)
        self.ip_var.trace('w', self.select_itemIp)

      
        # option_script = ttk.Combobox(self,values=)
        # option_script.place(x=320, y=292,width=140)
        

    def get_ip(self):
        ip_import = self.ipEntry.get()
        return ip_import
    
    def gui(self): 
        self.var = IntVar()
        self.nameVar = StringVar()
        # selected in OptionMenu
        self.value_inside = StringVar()
    
        self.ipEntry = Entry(self,width=30,bd=5,font=("", 12))
        self.ipEntry.config(highlightcolor="white",relief="sunken")
        self.ipEntry.place(x=40, y =35)
        ############################################################################
        self.label = Label( self, text = "IP ADDRESS",relief=RAISED,height=1,width=40,bg="#ffffff" )
        self.label.place(x=40, y=9)
        ###############################################################################
        """Button"""
        ip_button = Button(self,text = "Submit",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=7,relief="raised",command=self.portScanner)
        ip_button.place(x=365, y=35)
        ###############################################################################

        columns = ('PORT', 'OPEN')
        self.tree = ttk.Treeview(self, columns=columns, show='headings',height = 6,selectmode=BROWSE)
        # define headings
        self.tree.heading('PORT', text='PORT')
        self.tree.heading('OPEN', text='OPEN')
        self.tree.place(x=50, y=80)
        #add a scrollbar
        self.scrollbar = ttk.Scrollbar(self,orient=VERTICAL,command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=450,y=80,height=141)
        ############################################################################
        red = Radiobutton(self,text="RED", variable=self.var, value=1,
                  command="")
        red.place(x=50, y=270)
        yellow = Radiobutton(self,text="YELLOW", variable=self.var, value=2,
                  command="")
        yellow.place(x=60, y=290)
        green = Radiobutton(self,text="GREEN", variable=self.var, value=3,
                  command="")
        green.place(x=70, y=310)
        ############################################################################
        self.label2 = Label( self, text = "LANUCH PERSES", relief=RAISED,height=1,width=50,bg="#ffffff" )
        self.label2.place(x=50, y=225)
        ############################################################################

        self.label_port = Label( self, text = "PORT", relief=RAISED,height=1,width=15,bg="#ffffff" )
        self.label_port.place(x=190, y=270)
        self.label_script = Label( self, text = "SCRIPT", relief=RAISED,height=1,width=15,bg="#ffffff" )
        self.label_script.place(x=190, y=295)
        self.label_port = Label( self, text = "IP ADDRESS", relief=RAISED,height=1,width=15,bg="#ffffff" )
        self.label_port.place(x=190, y=324)


        ############################################################################
        # option menu1
        self.clicked = StringVar()
        
        # # option menu2
        # option_menu2 = OptionMenu(
        #     self,
        #     self.languages[0],
        #     *self.languages,
        #     command="")
        # option_menu2.place(x=320, y=292,width=140)
        # # option menu2
        
        ############################################################################
        """Button"""
        button = Button(self,text = "Done",bg="#ffffff",font=("",13,"bold"),bd=0,cursor="hand2",
        activebackground="#ffffff",width=10,relief="raised",command="")
        button.place(x=170, y=350)

        ############################################################################
        """DISPLAY"""
        display = ('ATHENA')
        output = ttk.Treeview(self, columns=display, show='headings',height = 9)
        # define headings
        output.heading('ATHENA', text='ATHENA')
        output.place(x=30, y=420,width=450)

        ############################################################################
        """PROGRESSBAR"""
        # progressbar
        pb = ttk.Progressbar(
            self,
            orient='horizontal',
            mode='indeterminate',
            length=280
        )
        # place the progressbar
        pb.place(x=30, y=400,width=450)

if __name__ == "__main__":
    root = Hashed()
    root.mainloop()