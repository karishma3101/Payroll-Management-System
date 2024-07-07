import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from PIL import Image,ImageTk


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['empid'])
    e2.insert(0, select['Empname'])
    e3.insert(0, select['Mobile'])
    e4.insert(0, select['Date'])
    e5.insert(0, select['inhand'])
    e6.insert(0, select['leavee'])
    e7.insert(0, select['money'])
    e8.insert(0, select['advance'])
    e9.insert(0, select['taxe'])
    e10.insert(0, select['pension'])
    e11.insert(0, select['total'])


def Add():
    empid = e1.get()
    empname = e2.get()
    mobile = e3.get()
    joiningdate = e4.get()
    inhand=e5.get()
    leavee=e6.get()
    money=e7.get()
    advance=e8.get()
    taxe=e9.get()
    pension=e10.get()
    total=e11.get()


    mysqldb = mysql.connector.connect(host="localhost", user="root", password="abhinavi", database="PMS")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  personal (empid,empname,mobile,joiningdate) VALUES (%s, %s, %s, %s)"
        val = (empid, empname, mobile, joiningdate)
        sql1 = "INSERT INTO  monthly (empid,inhand,leavee,money) VALUES (%s,%s, %s, %s)"
        val1 = (empid,inhand, leavee, money)
        sql2 = "INSERT INTO  deduction(advance,taxe,pension,total,empid) VALUES (%s, %s, %s, %s,%s)"
        val2 = (advance,taxe,pension,total,empid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        mycursor.execute(sql1, val1)
        mysqldb.commit()
        mycursor.execute(sql2, val2)
        mysqldb.commit()
        mysqldb.commit()

        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
def delete():
    empid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="abhinavi", database="PMS")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from personal where empid = %s"
        val = (empid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="abhinavi", database="PMS")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT empid,empname,mobile,joiningdate FROM personal")
    records = mycursor.fetchall()
    print(records)
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT inhand,leavee,money FROM monthly")
    record = mycursor.fetchall()
    print(record)
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT advance,taxe,pension,total FROM deduction")
    recor = mycursor.fetchall()
    print(recor)

    for i, (empid,empname,mobile,joiningdate) in enumerate(records, start=1):
        listBox.insert("", "end", values=(empid,empname,mobile,joiningdate))
        mysqldb.close()

root = Tk()
root.geometry("1200x1200")
image=Image.open("C:\\Users\\shashi\\Desktop\\payroll management\\payroll1.jpg")
bck_end=ImageTk.PhotoImage(image)
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global e9
global e10
global e11


tk.Label(root, text="Payroll Management System", fg="red",bg="black", font=("Broadway", 30)).place(x=300, y=5)
##personal data table
Label(root,text="Personal Data",fg="red",bg="black",font=("Arial black", 30)).place(x=10,y=70)
tk.Label(root, text="Employee ID",font="20",fg="white",bg="black").place(x=10, y=140)
Label(root, text="Employee Name",font="20",fg="white",bg="black").place(x=10, y=180)
Label(root, text="Mobile",font="20",fg="white",bg="black").place(x=10, y=220)
Label(root, text="Joining Date ",font="20",fg="white",bg="black").place(x=10, y=250)

e1 = Entry(root)
e1.place(x=170, y=140)

e2 = Entry(root)
e2.place(x=170, y=180)

e3 = Entry(root)
e3.place(x=170, y=220)

e4 = Entry(root)
e4.place(x=170, y=250)
##monthly entries table
Label(root,text="Monthly Entries",fg="red",bg="black",font=("arial black", 30)).place(x=400,y=70)
tk.Label(root, text="In hand salary",font="20",fg="white",bg="black").place(x=400, y=140)
Label(root, text="Leaves taken",font="20",fg="white",bg="black").place(x=400, y=180)
Label(root, text="Overtime Money",font="20",fg="white",bg="black").place(x=400, y=220)


e5 = Entry(root)
e5.place(x=600, y=140)

e6 = Entry(root)
e6.place(x=600, y=180)

e7 = Entry(root)
e7.place(x=600, y=220)


Button(root, text="Add", command=Add, height=3, width=13).place(x=400, y=300)

Button(root, text="Delete", command=delete, height=3, width=13).place(x=600, y=300)

##deduction from salary
Label(root,text="Deductions",fg="red",bg="black",font=("arial black", 30)).place(x=800,y=70)
tk.Label(root, text="Advance taken",font="20",fg="white",bg="black").place(x=800, y=140)
Label(root, text="Tax",font="20",fg="white",bg="black").place(x=800, y=170)
Label(root, text="PENSION",font="20",fg="white",bg="black").place(x=800, y=200)
Label(root, text="Total",font="20",fg="white",bg="black").place(x=800, y=230)

e8 = Entry(root)
e8.place(x=1000, y=140)

e9 = Entry(root)
e9.place(x=1000, y=170)

e10 = Entry(root)
e10.place(x=1000, y=200)

e11 = Entry(root)
e11.place(x=1000, y=230)

cols = ('Emp id', 'Empname', 'Mobile', 'joiningdate')
listBox = ttk.Treeview(root, columns=cols, show='headings')


for col in cols:

    listBox.heading(col, text=col)
    listBox.grid(row=0, column=0)
    listBox.place(x=100, y=500)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
