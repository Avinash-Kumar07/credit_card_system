from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import ttk

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
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
        txt_username=Entry(frame1,font=("Arial",15)).place(x=170,y=110,width=300)

        passwrd=Label(frame1,text="Password",font=("arial",12,),bg="#31a6ff",fg="#696969").place(x=170,y=160)
        txt_passwrd=Entry(frame1,show="*",font=("Arial",15)).place(x=170,y=190,width=300)

        forgot_passwrd=Label(frame1,text="Forgot Password?",font=("arial",12,'underline'),bg="#31a6ff",fg="Blue").place(x=170,y=230)

        #___Login Button______
        self.lgn_btn=ImageTk.PhotoImage(file="Images/login_bttn.png")
        lgn_btn=Button(frame1,image=self.lgn_btn,bd=0,cursor="hand2",command=applycc).place(x=270,y=260)

class ApplyCC:
     def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1024x576+1+1")
        self.root.config(bg="#ffffff")
       
        #___BG Image____
        self.bg=ImageTk.PhotoImage(file="Images/login_bg.png")
        bg=Label(self.root,text="Hello World").place(relheight=1,relwidth=1)

# def loginfun:
#     ("seletc")
def applycc():
    obj.root.destroy()
    root=Tk()
    obj1=ApplyCC(root)

root=Tk()
obj=Login(root)
root.mainloop()