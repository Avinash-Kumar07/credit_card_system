from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import ttk, messagebox
from tkcalendar import *
import pymysql

class ApplyCC:
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
    	
        #_______Title______________________________________________________________________________
        title=Label(self.root,text="APPLICATION",font=("times new roman",20,"bold"),bg="#31a6ff").place(x=430,y=60)

        #______Data Columns__________________________________________________________________________
        acc_id=Label(self.root,text="Account ID",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=100)
        self.txt_acc_id=Entry(self.root,font=("Arial",15))
        self.txt_acc_id.place(x=550,y=100,width=250)

        acc_name=Label(self.root,text="Name of Account Holder",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=150)
        self.txt_acc_name=Entry(self.root,font=("Arial",15))
        self.txt_acc_name.place(x=550,y=150,width=250)

        card_type=Label(self.root,text="Type of Card",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=250)
        self.cmb_card_type=ttk.Combobox(self.root,font=("Arial",15),state="readonly",justify=CENTER)
        self.cmb_card_type['values']=("Select","Silver","Gold","Platinum","Diamond")
        self.cmb_card_type.place(x=550,y=250,width=250)
        self.cmb_card_type.current(0)

        credit_limit=Label(self.root,text="Credit Limit(in Rupees)",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=300)
        self.txt_credit_limit=Entry(self.root,font=("Arial",15))
        self.txt_credit_limit.place(x=550,y=300,width=250)

        nameon_card=Label(self.root,text="Name on Card",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=350)
        self.txt_nameon_card=Entry(self.root,font=("Arial",15))
        self.txt_nameon_card.place(x=550,y=350,width=250)

        card_ver=Label(self.root,text="Card Version",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=400)
        self.cmb_card_ver=ttk.Combobox(self.root,font=("Arial",15),state="readonly",justify=CENTER)
        self.cmb_card_ver['values']=("Select","Master","Maestro","Visa","RuPay")
        self.cmb_card_ver.place(x=550,y=400,width=250)
        self.cmb_card_ver.current(0)

        dob=Label(self.root,text="Date of Birth",font=("arial",15,"bold"),bg="#31a6ff",fg="Black").place(x=280,y=200)
        self.txt_dob=Label(self.root,text="2000-01-01",font=("Arial",15))
        self.txt_dob.place(x=550,y=200,width=120)
        dob_btn=Button(self.root,text="Select Date",command=self.calendar_func).place(x=700,y=200)

        self.apply_btn=ImageTk.PhotoImage(file="Images/applycc_bttn.png")
        apply_btn=Button(self.root,image=self.apply_btn,bd=0,cursor="hand2",command=self.register_data).place(x=430,y=450)

        self.apply_msg=Label(self.root,text="",font=("arial",15,"bold"),bg="#31a6ff",fg="Green")
        self.apply_msg.place(x=410,y=500)


    def show_date(self):
        self.txt_dob.configure(text=self.cal.get_date(),font=("Arial",15))
        global DOB
        DOB = self.cal.get_date()
        frame1.destroy()

#__________Calendar_______________________________________________________________________________________
    def calendar_func(self):
        #___Frame_______
        global frame1
        frame1=Frame(self.root)
        frame1.pack(pady=250)
        self.cal = DateEntry(frame1,selectmode="day")
        self.cal.pack()
        sel_btn=Button(frame1,text="Select",command=self.show_date).pack()
#============Calendar======================================================================================

#_____________Get Data in Database_________________________________________________________________________
    def register_data(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="home4444",database="credit_card_system")
            cur=con.cursor()
            cur.execute("insert into card_applications(ACC_ID,ACC_NAME,DOB,TYPE_OF_CARD,VER_OF_CARD,NAME_ON_CARD,CREDIT_LIMIT) values(%s,%s,%s,%s,%s,%s,%s)",
            (int(self.txt_acc_id.get()),self.txt_acc_name.get(), DOB,
            self.cmb_card_type.get(),self.cmb_card_ver.get(),
            self.txt_nameon_card.get(),int(self.txt_credit_limit.get())))
            con.commit()
            con.close()

            self.apply_msg.configure(text="Applied Succesfully")

        except Exception as es:
            messagebox.showerror("error",f"Invalid Inputs due to: {str(es)}",parent=self.root)
#============Get Data in DataBase===========================================================================
        
def call_apply():
    root = Tk()
    global obj3
    obj3 = ApplyCC(root)
    root.mainloop()