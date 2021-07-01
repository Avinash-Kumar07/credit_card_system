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
import approve_cust_pg

class Approve:
    def __init__(self,root):
        self.root = root
        self.root.title("Bank")
        self.root.geometry("1024x576+1+1")
        self.root.config(bg="#31a6ff")

        #______Top Logo___________________________________________________________________
        #self.logo=ImageTk.PhotoImage(file="Images/logo.png")
        #self.bg=Label(self.root,image=self.logo,bd=0).place(x=0,y=0)

        #___Top row links_________________________________________________________________
        lgt_btn=Button(self.root,text="Logout",bd=0,cursor="hand2",command=self.disp_data).place(x=635,y=8)
        
        abtus_btn=Button(self.root,text="About Us",bd=0,cursor="hand2").place(x=712,y=8)
        
        cntus_btn=Button(self.root,text="Contact Us",bd=0,cursor="hand2").place(x=800,y=8)
        
        ourservices_btn=Button(self.root,text="Our Services",bd=0,cursor="hand2").place(x=900,y=8)

        #___________Account Particulars____________________________________________________________
        txt_acc_id = Label(self.root, text="Account ID:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=120)
        self.txt_acc_id = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff", fg="white")
        self.txt_acc_id.place(x=250, y=120)

        txt_acc_name = Label(self.root, text="Acc Name:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=170)
        self.txt_acc_name = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_acc_name.place(x=250, y=170)

        txt_dob = Label(self.root, text="D.O.B:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=220)
        self.txt_dob = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_dob.place(x=250, y=220)

        txt_ver_of_card = Label(self.root, text="Card Version:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=270)
        self.txt_ver_of_card = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_ver_of_card.place(x=250, y=270)

        txt_type_of_card = Label(self.root, text="Type of Card:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=550, y=120)
        self.txt_type_of_card = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_type_of_card.place(x=700, y=120)

        txt_income = Label(self.root, text="Income:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=550, y=170)
        self.txt_income = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_income.place(x=700, y=170)

        txt_car = Label(self.root, text="Car:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=550, y=220)
        self.txt_car = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_car.place(x=650, y=220)

        txt_realty = Label(self.root, text="Realty:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=750, y=220)
        self.txt_realty = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_realty.place(x=850, y=220)

        txt_credit_limit = Label(self.root, text="Credit Limit:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=550, y=270)
        self.txt_credit_limit = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_credit_limit.place(x=700, y=270)

        self.result = approve_cust_pg.acc
        #print(self.result)

        con = pymysql.connect(host="localhost", user="root",password="home4444", database="credit_card_system")
        cur = con.cursor()
        cur.execute("select INCOME,CAR,REALTY from customers where ACC_ID='%s'",self.result[0][0])
        self.result2 = cur.fetchall()
        con.commit()
        con.close()

    def disp_data(self):
        self.txt_acc_id.configure(text=self.result[0][0])
        self.txt_acc_name.configure(text=self.result[0][1])
        self.txt_dob.configure(text=self.result[0][2])
        self.txt_type_of_card.configure(text=self.result[0][3])
        self.txt_ver_of_card.configure(text=self.result[0][4])
        self.txt_credit_limit.configure(text=self.result[0][6])
        self.txt_income.configure(text=self.result2[0][0])
        self.txt_car.configure(text=self.result2[0][1])
        self.txt_realty.configure(text=self.result2[0][2])

def call_approve():
    root = Tk()
    global obj6
    obj6 = Approve(root)
    root.mainloop()
#call_approve()