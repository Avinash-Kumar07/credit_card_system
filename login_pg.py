from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import ttk
from tkcalendar import *
from applyc_pg import *
import customer_home_pg

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Bank")
        self.root.geometry("1024x576+1+1")
        self.root.config(bg="#ffffff")
       
        #___BG Image____
        self.bg=ImageTk.PhotoImage(file="Images/login_bg.png")
        bg=Label(self.root,image=self.bg).place(relheight=1,relwidth=1)

        #___Top row links____
        
        abtus_btn=Button(self.root,text="About Us",bd=0,cursor="hand2").place(x=712,y=8)
        
        cntus_btn=Button(self.root,text="Contact Us",bd=0,cursor="hand2").place(x=800,y=8)
        
        ourservices_btn=Button(self.root,text="Our Services",bd=0,cursor="hand2").place(x=900,y=8)

        #___Frame_______
        frame1=Frame(self.root)
        frame1.place(x=212,y=38,width=600,height=500)
        frame1bg=Label(frame1,image=self.bg).place(x=-212,y=-38)

        title=Label(frame1,text="Login Here",font=("times new roman",20,"bold"),bg="#31a6ff").place(x=250,y=10)

        username=Label(frame1,text="User Name(Emp ID for Employees",font=("arial",12,),bg="#31a6ff",fg="#696969").place(x=170,y=80)
        self.txt_username=Entry(frame1,font=("Arial",15))
        self.txt_username.place(x=170,y=110,width=300)

        passwrd=Label(frame1,text="Password",font=("arial",12,),bg="#31a6ff",fg="#696969").place(x=170,y=160)
        self.txt_passwrd=Entry(frame1,show="*",font=("Arial",15))
        self.txt_passwrd.place(x=170,y=190,width=300)

        forgot_passwrd=Label(frame1,text="Forgot Password?",font=("arial",12,'underline'),bg="#31a6ff",fg="Blue").place(x=170,y=230)

        #___Login Button______
        self.lgn_btn=ImageTk.PhotoImage(file="Images/login_bttn.png")
        lgn_btn=Button(frame1,image=self.lgn_btn,bd=0,cursor="hand2",command=self.register_data).place(x=270,y=260)

        self.lgn_msg=Label(frame1,text="",font=("arial",15,"bold"),bg="#31a6ff",fg="Red")
        self.lgn_msg.place(x=270,y=320)
        
    def register_data(self):
        lgn_id_entered = int(self.txt_username.get())
        con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
        cur=con.cursor()
        cur.execute("select * from customers where ACC_ID='%s'",lgn_id_entered)
        result = cur.fetchall()
        if len(result) != 0:
            global lgn_id
            lgn_id = lgn_id_entered
            self.lgn_msg.configure(text="Login Successfull")
            cust_call()
        else:
            self.lgn_msg.configure(text="Invalid User")
        con.commit()
        con.close()

def call_login_pg():
    root=Tk()
    global obj1
    obj1=Login(root)
    root.mainloop()

def cust_call():
    obj1.root.destroy()
    customer_home_pg.call_cust_home_pg()