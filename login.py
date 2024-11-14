from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if userentry.get()=='' or passwordentry.get()=="":
       messagebox.showerror("Error", "Can't Login because You do not fill any place ") 
    elif userentry.get()=="Anjum Bano" and passwordentry.get()=="1122":
        messagebox.showinfo("Sucess","You logined successfully go ahead")
        root.destroy()
        import ems
        ems.open_ems()

    else:
        messagebox.showerror("Error","Wrong credentials")  




root=CTk()
root.geometry('860x605')
root.resizable(0,0)
root.title("Login Page")
image=CTkImage(Image.open('aa.jpg'),size=(860,605))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text="Employee Management System",text_color='dark blue',bg_color="#FAFAFA",font=("Arial",16,'bold'))
headinglabel.place(x=20,y=100)
userentry=CTkEntry(root,placeholder_text="Enter your Username",bg_color="#FFFFFF",text_color="#000000",width=180)
userentry.place(x=50,y=150)
passwordentry=CTkEntry(root,placeholder_text="Enter your Password",bg_color="#FFFFFF",text_color="#000000",width=180,show="*")
passwordentry.place(x=50,y=200)
loginButton=CTkButton(root,text="Login",cursor="hand2",command=login)
loginButton.place(x=50,y=260)

root.mainloop()