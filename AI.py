from tkinter import *
from PIL import Image,ImageTk;
root = Tk()
root.geometry("500x300")
root.minsize(400,200)
root.title("login")
root.iconbitmap("pyFiles/safe_secure_privacy_padlock_lock_icon_230581.ico") 
def hack():
    
    if (passwd=='0000'):
        print(0000,"here's the password")
        return
    for i in range(1000,9999+1):
        print(i)
        if(i==passwd.get()):
            print(i,"HERE'S THE PASSWORD ^_^")
            break
root.maxsize(600,400)
root.config(bg="black")
l1 =Label(text="Login to your account using 4 digit PIN",background="black",fg="white",height=4,font=("MS Arial",10,"bold"))
l1.place(x=100,y=0)
i1= Image.open("pyFiles/ai.jpg")
p1=ImageTk.PhotoImage(i1)
l2=Label(root,image=p1)
l2.place(x=0,y=50)
l3=Label(l2,text="Enter username",bg="black",fg="white",font=("MS Arial",10,"bold"))
l3.place(x=100,y=100)
l4=Label(l2,text="Enter password",bg="black",fg="white",font=("MS Arial",10,"bold"))
l4.place(x=100,y=130)

usrname=StringVar()
passwd=IntVar()
passwd.set('')
usr=Entry(l2,textvariable=usrname)
usr.place(x=220,y=100)
passw=Entry(l2,textvariable=passwd)
passw.place(x=220,y=130)
b = Button(l2,text="LOGIN",command=hack)
b.place(x=150,y=160)
root.mainloop()

