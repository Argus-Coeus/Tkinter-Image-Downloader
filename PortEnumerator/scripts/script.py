#!/usr/bin/python3


#!/usr/bin/python3

from tkinter import messagebox
import ftplib
from threading import Thread
import queue
import sys
sys.path.append('/media/argus/New Volume/Scripts/PortEnumerator')
from portenumerator import Hashed

class FtpEnumerate():
    def __init__(self):
       super().__init__()
       self.ftp_brute_force()
       
    def ftp_brute_force(self):
        q = queue.Queue()
        n_threads = 30
        host = Hashed.get_ip(self)
        print(host)


FtpEnumerate()
