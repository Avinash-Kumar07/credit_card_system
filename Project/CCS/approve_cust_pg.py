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
import approve_pg

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
        home_btn=Button(self.root,text="HOME",bd=0,cursor="hand2").place(x=558,y=8)
        
        lgt_btn=Button(self.root,text="Logout",bd=0,cursor="hand2").place(x=635,y=8)
        
        abtus_btn=Button(self.root,text="About Us",bd=0,cursor="hand2").place(x=712,y=8)
        
        cntus_btn=Button(self.root,text="Contact Us",bd=0,cursor="hand2").place(x=800,y=8)
        
        ourservices_btn=Button(self.root,text="Our Services",bd=0,cursor="hand2").place(x=900,y=8)

        #______________________Other widgets______________________________________________________________
        refesh_btn=Button(self.root,text="Refresh",bd=2,cursor="hand2",command=self.refresh_tree).place(x=900,y=110)

        select_cust_bttn=Button(self.root,text="Select Customer",bd=2,cursor="hand2",command=self.select_cust).place(x=750,y=110)

        #____________tree view________________________________________________________________
        self.tree_cust=ttk.Treeview(self.root,show="headings",height="5")
        self.tree_cust.pack(pady=150)
        self.tree_cust['columns'] = ("ACC_ID","ACC_NAME","DOB","TYPE_OF_CARD","VER_OF_CARD","NAME_ON_CARD","CREDIT_LIMIT")
        self.tree_cust.column("ACC_ID",anchor=W,width=120)
        self.tree_cust.column("ACC_NAME",anchor=W,width=180)
        self.tree_cust.column("DOB",anchor=W,width=100)
        self.tree_cust.column("TYPE_OF_CARD",anchor=W,width=140)
        self.tree_cust.column("VER_OF_CARD",anchor=W,width=140)
        self.tree_cust.column("NAME_ON_CARD",anchor=W,width=150)
        self.tree_cust.column("CREDIT_LIMIT",anchor=W,width=130)

        self.tree_cust.heading("ACC_ID",text="ACC_ID")
        self.tree_cust.heading("ACC_NAME",text="ACC_NAME")
        self.tree_cust.heading("DOB",text="DOB")
        self.tree_cust.heading("TYPE_OF_CARD",text="TYPE_OF_CARD")
        self.tree_cust.heading("VER_OF_CARD",text="VER_OF_CARD")
        self.tree_cust.heading("NAME_ON_CARD",text="NAME_ON_CARD")
        self.tree_cust.heading("CREDIT_LIMIT",text="CREDIT_LIMIT")

        self.refresh_tree()

    def refresh_tree(self):
        con = pymysql.connect(host="localhost", user="root",password="home4444", database="credit_card_system")
        cur = con.cursor()
        cur.execute(q8)
        self.rows = cur.fetchall()
        total = cur.rowcount
        con.commit()
        con.close()

        for i in self.rows:
            self.tree_cust.insert('','end',values=i)

    def select_cust(self):
        items = self.tree_cust.selection()
        cust_data = []
        for i in items:
            cust_data.append(self.tree_cust.item(i)['values'])
        global acc
        acc = cust_data
        obj5.root.destroy()
        approve_pg.call_approve()


def call_approve_cust():
    root = Tk()
    global obj5
    obj5 = Approve_cust(root)
    root.mainloop()