import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound
#window creation
window=tk.Tk()
window.title("timer<3")
window.geometry('600x600')
head=Label(window,text="COUNTDOWN-TIMER",font=('Calibri-15'))
head.pack(pady=20)
#display time
now=datetime.now()
current_time=now.strftime("%H:%M:%S")
Label(window,text="current_time").pack()

check=tk.BooleanVar()#check is of boolean type
hour=tk.IntVar()
minus=tk.IntVar()
secon=tk.IntVar()


#creating function
def countdown():
    h=hour.get()
    m=minus.get()
    s=secon.get()#get the value
    t= h * 3600 + m * 60 + s
    while t:
        mins,secs=divmod(t,60)
        display=('{:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)
        t-=1
        Label(window,text=display).pack()

    if (check.get()==True):#if the value of check is true     
            winsound.Beep(440, 1000)#beep sound 

    Label(window,text="Time-Up",font=('bold', 20)).place(x=250,y=440)
    #display notification
    toast = ToastNotifier()#create toast variable
    toast.show_toast("Notification","Timer is Off",duration = 20,icon_path = NONE,threaded = True,)#show toast


#taking input
Label(window,text="Enter time in HH:MM:SS",font=('bold')).pack()
Entry(window,textvariable = hour,width=30).pack()
Entry(window,textvariable = minus,width=30).pack()
Entry(window,textvariable = secon,width=30).pack()

Checkbutton(text='Check for Music',onvalue=True,variable=check).pack()#creating checkbox
Button(window,text="Set Countdown",command=countdown,bg='red').pack()#create buttons  
window.update()#update the window

window.mainloop()#main command