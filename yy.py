import pymysql
from tkinter import messagebox
def conn_database():
    try:
        conn=pymysql.connect(host="localhost",user="root",password="Anjumbano12@#$%1")
        mycursor=conn.cursor()
        
    except Exception as e:
        messagebox.showerror("Error", f"something went wrong try agin later")
        return
    mycursor.execute("CREATE DATABASE IF NOT EXISTS ta")
    mycursor.execute("USE ta")
    mycursor.execute("CREATE TABLE  IF NOT EXISTS at(Id int,Name varchar(50),Phone BIGINT,Role varchar(62),Gender varchar(50),Salary Decimal(10,2))")
    messagebox.showinfo("successful", "your database is connected successfully")
    
def insert(id,name,phone,role,gender,salary):
   print(id,name,phone,role,gender,salary)

conn_database()       