import mysql.connector

import pyautogui    #1920w 1080h
from tkinter import *
from PIL import Image,ImageTk;
import time;
# w,h=pyautogui.size() #to get the size of your screen
# print(w,h)

Mydb= mysql.connector.connect(host="localhost",user="root",password="*****",database='ai')
cur=Mydb.cursor()


root=Tk()



root.geometry("600x300")
root.geometry("+500+50")
root.minsize(400,200)
root.title("let's hack")
root.iconbitmap("safe_secure_privacy_padlock_lock_icon_230581.ico") 
root.maxsize(500,300)

def hack():
    
    cur.execute(f"select dbpasswd from user where dbusrname='{usr.get()}'")
    res=cur.fetchall()
    a=res[0]
    b=''.join(a)
    f=open("dict.txt")
    
    for i in f:
        i=i.rstrip()  #to remain the new line and spaces 
        print(i)
        time.sleep(0.1)
        
        if(i==b):
            print()
            print(i+" "+f"is password for {usr}")
            return
    c=int(b)
    for i in range(100,99999999+1):
        print(i)
        
        if(i==c):
            print()
            print(i,f"HERE'S THE PASSWORD ^_^ for {usr.get()} ")
            break
usr=StringVar()
i1= Image.open("ai.jpg")
p1=ImageTk.PhotoImage(i1)
l2=Label(root,image=p1)
l2.place(x=0,y=0)
l=Label(l2,text="Enter username",background="black",fg="white",height=2,font=("MS Arial",10,"bold"))
l.place(x=50,y=10)
ent=Entry(l2,textvariable=usr)
ent.place(x=210,y=20)



b=Button(text="start",width=5,command=hack)
b.place(x=200,y=70)


root.mainloop()
