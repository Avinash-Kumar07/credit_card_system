from tkinter import *
from tkcalendar import *
from applyc import *
import time

def dateval(self):
    print(self.cal.get_date())
    frame1.destroy()

def calendar_func(self):

    #___Frame_______
    global frame1
    frame1=Frame(self.root)
    frame1.pack(pady=250)
    self.cal = DateEntry(frame1,selectmode="day",year=2000,month=1,day=1)
    self.cal.pack()
    sel_btn=Button(frame1,text="Select",command=self.dateval).pack()

