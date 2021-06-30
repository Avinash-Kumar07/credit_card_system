from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import ttk, messagebox
from mysql.connector import connection
from tkcalendar import *
import pymysql
import os
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from icecream import ic
from sql_queries import *

class Approve_cust:
    def __init__(self,root):
        self.root = root
        self.root.title("Bank")
        self.root.geometry("1024x576+1+1")
        self.root.config(bg="#31a6ff")

        #______Top Logo___________________________________________________________________
        self.logo=ImageTk.PhotoImage(file="Images/logo.png")
        bg=Label(self.root,image=self.logo,bd=0).place(x=0,y=0)

        #___Top row links_________________________________________________________________
        lgt_btn=Button(self.root,text="Logout",bd=0,cursor="hand2").place(x=635,y=8)
        
        abtus_btn=Button(self.root,text="About Us",bd=0,cursor="hand2").place(x=712,y=8)
        
        cntus_btn=Button(self.root,text="Contact Us",bd=0,cursor="hand2").place(x=800,y=8)
        
        ourservices_btn=Button(self.root,text="Our Services",bd=0,cursor="hand2").place(x=900,y=8)

def call_approve_cust():
    root = Tk()
    global obj5
    obj5 = Approve_cust(root)
    root.mainloop()

call_approve_cust()