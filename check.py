from tkinter import *
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width = 3000 ,height = 1600)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\Syed Hussain\\Desktop\\New folder (2)\\Figure_1.png"))

canvas.create_image(0,0,anchor = NW, image = image)
canvas.pack()
 
def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "Admin" and password == "123"):
 
        messagebox.showinfo("","Login Success")
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")
 
 
root = Tk()
root.title("Login")
root.geometry("300x200")
global e1
global e2
 
Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")
 
 
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=10, y=100)
 
root.mainloop()