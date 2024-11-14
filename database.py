import pymysql
from tkinter import messagebox

def conn_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host="localhost",user="root",password="Anjumbano12@#$%1")
        mycursor=conn.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTs employee_data")
        mycursor.execute("USE employee_data")
        mycursor.execute("CREATE TABLE  IF NOT EXISTS data(Id int,Name varchar(50),Phone BIGINT,Role varchar(62),Gender varchar(50),salary DECIMAL(10,2))")
        messagebox.showinfo("successful", "your database is connected successfully")
    except Exception as e:
        messagebox.showerror("Error", f"something went wrong try agin later:{e}")
        return
    
def insert(id,name,phone,role,gender,salary):
#    print(id,name,phone,role,gender,salary)
    mycursor.execute("insert into data values(%s,%s,%s,%s,%s,%s)",(id,name,phone,role,gender,salary))
    conn.commit()
def id_exists(id):
    mycursor.execute("SELECT COUNT(*) FROM data where id=%s",id) 
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute("select * from data")
    result=mycursor.fetchall()
    return result
def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute("update data set name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s",(new_name,new_phone,new_role,new_gender,new_salary,id))
    # conn.commit()
def delete(id):
    mycursor.execute("delete from data where id=%s",id)    

def search(option,value):
    mycursor.execute(f"select * from data where {option}=%s",value)
    result=mycursor.fetchall()
    return result
def deleteall_records():
    mycursor.execute("Truncate table data")
    conn.commit()
conn_database()   