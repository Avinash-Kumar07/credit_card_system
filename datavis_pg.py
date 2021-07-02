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
import login_pg

class Datavis:
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

        #______________DATA DISP___________________________________________________________________
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        df = pd.read_sql_query(q1,con)
        con.commit()
        con.close()
        
        no_of_approved=Label(self.root,text="No of Approved Customers:",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=500,y=100)
        no_approved=Label(self.root,text=str(df.countofc[0]),font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=800,y=100)

        no_of_pending=Label(self.root,text="No of Pending applications:",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=500,y=150)
        no_pending=Label(self.root,text=str(df.countofc[1]),font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=800,y=150)

        no_of_declined=Label(self.root,text="No of Declined Customers:",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=500,y=200)
        no_declined=Label(self.root,text=str(df.countofc[2]),font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=800,y=200)

        no_of_notapplied=Label(self.root,text="No of not Applied Customers:",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=500,y=250)
        no_notapplied=Label(self.root,text=str(df.countofc[3]),font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=800,y=250)

        #___________Buttons_________________________________________________________________
        ccstatus_btn=Button(self.root,text="Customers Status",bd=2,cursor="hand2",command=self.disp_ccstatus).place(x=100,y=100)

        age_vs_income_btn=Button(self.root,text="Age vs Income",bd=2,cursor="hand2",command=self.disp_age_vs_income).place(x=100,y=150)

        age_vs_avgincome_bttn= Button(self.root,text="Age vs Average Income",bd=2,cursor="hand2",command=self.disp_age_vs_avgincome).place(x=100,y=200)

        income_type_bttn= Button(self.root,text="Income Type",bd=2,cursor="hand2",command=self.disp_income_type).place(x=100,y=250)

        approve_pg_bttn= Button(self.root,text="Approve Customers",bd=2,cursor="hand2",command=call_approve_cust_pg).place(x=500,y=500)

        #____________SEARCH_________________________________________________________________________
        search=Label(self.root,text="Search Customers",font=("arial",15),bg="#31a6ff",fg="Black").place(x=100,y=300)
        search_bttn= Button(self.root,text="Search",bd=2,cursor="hand2",command=self.search_cust).place(x=760,y=300)
        self.txt_search=Entry(self.root,font=("Arial",15))
        self.txt_search.place(x=280,y=300,width=200)
        self.cmb_search=ttk.Combobox(self.root,font=("Arial",15),state="readonly",justify=CENTER)
        self.cmb_search['values']=("Select","FIRST_NAME","LAST_NAME","ACC_ID","EMAIL","CC_STATUS")
        self.cmb_search.place(x=500,y=300,width=250)
        self.cmb_search.current(0)
    
        #____________tree view________________________________________________________________
        self.tree_cust=ttk.Treeview(self.root,show="headings",height="5")
        self.tree_cust.place(y=340)
        self.tree_cust['columns'] = ("ACC_ID","ACC_NAME","DOB","EMAIL","INCOME","CC_STATUS","PHONE")
        self.tree_cust.column("ACC_ID",anchor=E,width=120)
        self.tree_cust.column("ACC_NAME",anchor=W,width=180)
        self.tree_cust.column("DOB",anchor=E,width=100)
        self.tree_cust.column("EMAIL",anchor=W,width=230)
        self.tree_cust.column("INCOME",anchor=E,width=110)
        self.tree_cust.column("CC_STATUS",anchor=W,width=150)
        self.tree_cust.column("PHONE",anchor=E,width=130)

        self.tree_cust.heading("ACC_ID",text="ACC_ID")
        self.tree_cust.heading("ACC_NAME",text="ACC_NAME")
        self.tree_cust.heading("DOB",text="DOB")
        self.tree_cust.heading("EMAIL",text="EMAIL")
        self.tree_cust.heading("INCOME",text="INCOME")
        self.tree_cust.heading("CC_STATUS",text="CC_STATUS")
        self.tree_cust.heading("PHONE",text="PHONE")

    def clear_search(self):
            for i in self.tree_cust.get_children():
                self.tree_cust.delete(i)

    def search_cust(self):
        for i in self.tree_cust.get_children():
            self.tree_cust.delete(i)
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        cur=con.cursor()
        quer= "select ACC_ID,concat(FIRST_NAME,' ',LAST_NAME) as NAME,DOB,EMAIL,INCOME,CC_STATUS,PHONE from customers where " + self.cmb_search.get()+ " like '%" +self.txt_search.get() + "'"
        cur.execute(quer)
        self.rows = cur.fetchall()
        total = cur.rowcount
        con.commit()
        con.close()

        for i in self.rows:
            self.tree_cust.insert('','end',values=i)
        
    def disp_ccstatus(self):
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        df = pd.read_sql_query(q1,con)
        con.commit()
        con.close()
        labels = df.CC_STATUS
        colors=['#f56f5b','cyan','#f5ed5b','#4be373']
        plt.pie(df.countofc,labels=labels,colors=colors,autopct='%.1f %%')
        plt.show()
    
    def disp_age_vs_income(self):
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        df = pd.read_sql_query(q2,con)
        con.commit()
        con.close()
        plt.style.use('seaborn')
        plt.scatter(df.age,df.INCOME)
        plt.title('Age vs Income')
        plt.xlabel('AGE')
        plt.ylabel('INCOME')
        plt.show()

    def disp_age_vs_avgincome(self):
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        df = pd.read_sql_query(q3,con)
        con.commit()
        con.close()
        plt.style.use('seaborn')
        plt.bar(df.age,df.INCOME)
        plt.title('Age vs  Average Income')
        plt.xlabel('AGE')
        plt.ylabel('AVERAGE INCOME')
        plt.show()

    def disp_income_type(self):
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        df = pd.read_sql_query(q4,con)
        con.commit()
        con.close()
        labels = df.INCOME_TYPE
        colors=['#f56f5b','cyan','#f5ed5b','#4be373']
        plt.pie(df.countofc,labels=labels,autopct='%.1f %%')
        plt.show()


def call_datavis():
    root = Tk()
    global obj4
    obj4 = Datavis(root)
    root.mainloop()

def call_approve_cust_pg():
    obj4.root.destroy()
    approve_cust_pg.call_approve_cust()