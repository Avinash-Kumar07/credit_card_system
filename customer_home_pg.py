from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import ttk, messagebox
from tkcalendar import *
import pymysql
import login_pg
import applyc_pg

class cust_home:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank")
        self.root.geometry("1024x576+1+1")
        self.root.config(bg="#31a6ff")

        #______Top Logo__________________________________________________________________
        self.logo = ImageTk.PhotoImage(file="Images/logo.png")
        bg = Label(self.root, image=self.logo, bd=0).place(x=0, y=0)

        #___Top row links_________________________________________________________________
        lgt_btn = Button(self.root, text="Logout", bd=0,cursor="hand2").place(x=635, y=8)

        abtus_btn = Button(self.root, text="About Us", bd=0,cursor="hand2").place(x=712, y=8)

        cntus_btn = Button(self.root, text="Contact Us",bd=0, cursor="hand2").place(x=800, y=8)

        ourservices_btn = Button(self.root, text="Our Services", bd=0, cursor="hand2").place(x=900, y=8)

        #_______Greet Message______________________________________________________________________
        self.greet_msg = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.greet_msg.place(x=430, y=60)

        #___________Account Particulars____________________________________________________________
        txt_acc_id = Label(self.root, text="Account ID:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=120)
        self.txt_acc_id = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff", fg="white")
        self.txt_acc_id.place(x=250, y=120)

        txt_email = Label(self.root, text="Email ID:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=170)
        self.txt_email = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_email.place(x=250, y=170)

        txt_phone = Label(self.root, text="Phone:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=100, y=220)
        self.txt_phone = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_phone.place(x=250, y=220)

        txt_dob = Label(self.root, text="D.O.B:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=550, y=120)
        self.txt_dob = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_dob.place(x=700, y=120)

        txt_ccstatus = Label(self.root, text="Card Status:", font=("times new roman", 18, "bold"), bg="#31a6ff").place(x=550, y=170)
        self.txt_ccstatus = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff", fg="green")
        self.txt_ccstatus.place(x=700, y=170)

        self.txt_cceligiblity = Label(self.root, text="", font=("times new roman", 18, "bold"), bg="#31a6ff")
        self.txt_cceligiblity.place(x=200, y=270)

        self.cal_score_btn = ImageTk.PhotoImage(file="Images/cal_score_bttn.png")
        cal_score_btn = Button(self.root, image=self.cal_score_btn, bd=0,cursor="hand2").place(x=480, y=370)

#__________________________Get data from database_______________________________________________________________
        con = pymysql.connect(host="localhost", user="root",password="home4444", database="credit_card_system")
        cur = con.cursor()
        cur.execute("select * from customers where ACC_ID='%s'",login_pg.lgn_id)
        self.result = cur.fetchall()
        con.commit()
        con.close()
#==========================Get data from databse================================================================

        if len(self.result) != 0:
            self.disp_data()

    def disp_data(self):
        self.greet_msg.configure(text="Hi, " + self.result[0][1] + " " + self.result[0][2])
        self.txt_acc_id.configure(text=self.result[0][0])
        self.txt_email.configure(text=self.result[0][3])
        self.txt_phone.configure(text=self.result[0][4])
        self.txt_dob.configure(text=self.result[0][5])
        self.txt_ccstatus.configure(text=self.result[0][9])
        self.check_eligibility()

    def check_eligibility(self):
        if (self.result[0][7]) > 150000 or ((self.result[0][7]) > 80000 and (self.result[0][10] == "Y" or (self.result[0][11]) == "Y")):
            self.txt_cceligiblity.configure(text="You are eligible for a credit card", bg="grey", fg="white")

            self.apply_btn = ImageTk.PhotoImage(file="Images/applycc_bttn.png")
            apply_btn = Button(self.root, image=self.apply_btn, bd=0,cursor="hand2",command=apply_call).place(x=480, y=320)
            
        else:
            self.txt_cceligiblity.configure(text="Sorry, you are not eligible for a credit card", bg="grey", fg="white")

def call_cust_home_pg():
    root = Tk()
    global obj2
    obj2 = cust_home(root)
    root.mainloop()

def apply_call():
    obj2.root.destroy()
    applyc_pg.call_apply()