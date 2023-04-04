from tkinter import *
from PIL import Image,ImageTk;
import mysql.connector
Mydb= mysql.connector.connect(host="localhost",user="root",password="19204@aBs",database='ai')
cur=Mydb.cursor()

root = Tk()
root.geometry("600x300")
root.minsize(400,200)
root.title("welcome!")
root.iconbitmap("safe_secure_privacy_padlock_lock_icon_230581.ico") 
root.config(bg='black')
def np():
    root.withdraw()
    u=usrname.get()
    p=passwd.get()
    query = "SELECT * FROM user WHERE dbusrname=%s"
    values = [u]
    cur.execute(query,values)
    res = cur.fetchone()
    if res is None:
        
        s="insert into user(dbusrname,dbpasswd) values(%s,%s);"
        l=[u,p]
        cur.execute(s,l)
        Mydb.commit()
        print("login successful")
    
        
        
        notep = Toplevel(root)
        notep.title("Welcome!")
        notep.geometry("500x300")
        notep.config(bg='black')
        npl1=Label(notep,text=f"hello {usrname.get()}")
        npl1.grid(row=5,column=5)
        
        
    else:
        print("user exists")
        root.destroy()
        
        


root.maxsize(600,400)

l1 =Label(text="Login to your account (password must have more than 3 characters)",background="black",fg="white",height=4,font=("MS Arial",10,"bold"))
l1.place(x=100,y=0)

l3=Label(root,text="Enter username",bg="black",fg="white",font=("MS Arial",10,"bold"))
l3.place(x=100,y=100)
l4=Label(root,text="Enter password",bg="black",fg="white",font=("MS Arial",10,"bold"))
l4.place(x=100,y=130)

usrname=StringVar()
passwd=StringVar()
dbpasswd=StringVar()
dbusrname=StringVar()
passwd.set('')
usr=Entry(root,textvariable=usrname)
usr.place(x=220,y=100)
passw=Entry(root,textvariable=passwd)
passw.place(x=220,y=130)
b = Button(root,text="LOGIN",command=np)
b.place(x=150,y=160)
root.mainloop()


