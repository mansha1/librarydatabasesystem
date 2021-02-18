from tkinter import *
import sqlite3 
win = Tk()
win.title("libraray service")
win.geometry("1000x1000")


#==========creating variable
member = StringVar()
reference = StringVar()
title = StringVar()
firstname = StringVar()
surname = StringVar()
address1 = StringVar()
address2 = StringVar()
postcode= StringVar()
mobile = StringVar()
bookid = StringVar()
booktitle = StringVar()
author = StringVar()
dateborrowed = StringVar()
datedue = StringVar()
daysonloan = StringVar()
latereturn = StringVar()
dateoverdue = StringVar()
sellingprice = StringVar()

# data base creation
def clear():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)
    e17.delete(0, END)
    e18.delete(0, END)

def add():
    member1 = member.get()
    reference1 = reference.get()
    title1 = title.get()
    firstname1 = firstname.get()
    surname1 = surname.get()
    address11 = address1.get()
    address22 = address2.get()
    postcode1 = postcode.get()
    mobile1 = mobile.get()
    bookid1 = bookid.get()
    booktitle1 = booktitle.get()
    author1 = author.get()
    dateborrowed1 = dateborrowed.get()
    datedue1 = datedue.get()
    daysonloan1 = daysonloan.get()
    latereturn1 = latereturn.get()
    dateoverdue1 = dateoverdue.get()
    sellingprice1 = sellingprice.get()
    print(member1,reference1 ,title1)
    con = sqlite3.connect("lib1.db")
    with con:
        cursor = con.cursor()
        cursor.execute("create table if not exists Register_data(member Text,reference Text,title Text,firstname Text,surname Text,address1 Text,address2 Text,postcode Text,mobile Text,bookid Text,booktitle Text,author Text,dateborrowed Text,datedue Text,daysonloan Text,latereturn Text,dateoverdue Text,sellingprice Text)")
        cursor.execute("insert into Register_data(member,reference ,title,firstname,surname,address1,address2,postcode,mobile,bookid,booktitle,author,dateborrowed,datedue,daysonloan,latereturn,dateoverdue,sellingprice)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(member1,reference1 ,title1,firstname1,surname1,address11,address22,postcode1,mobile1,bookid1,booktitle1,author1,dateborrowed1,datedue1,daysonloan1,latereturn1,dateoverdue1,sellingprice1))
        con.commit()




# creating a label
l1 = Label(win,text = "Library Management System",width = 50,bg="skyblue",
           font = ("bold",28))
l1.place(x=10,y=5)

l2 = Label(win,text = "library membership info::",width = 50,bg = "skyblue",font = 25)
l2.place(x = 10,y=60)

l3 = Label(win,text = "member type:",width = 20,font = 25,bg = "skyblue")
l4 = Label(win,text = "Refernce number:",width = 20,font = 25,bg = "skyblue")
l5 = Label(win,text = "Title:",width = 20,font = 25,bg = "skyblue")
l6 = Label(win,text = "Firstname:",width = 20,font = 25,bg = "skyblue")
l7 = Label(win,text = "surname:",width = 20,font = 25,bg = "skyblue")
l8 = Label(win,text = "Address1:",width = 20,font = 25,bg = "skyblue")
l9 = Label(win,text = "address 2:",width = 20,font = 25,bg = "skyblue")
l10 = Label(win,text = "post code:",width = 20,font = 25,bg = "skyblue")
l11 = Label(win,text = "mobile number:",width = 20,font = 25,bg = "skyblue")
l12= Label(win,text = "Book id:",width = 20,font = 25,bg = "skyblue")
l13 = Label(win,text = "Book title:",width = 20,font = 25,bg = "skyblue")
l14 = Label(win,text = "Author:",width = 20,font = 25,bg = "skyblue")
l15 = Label(win,text = "Date borrowed:",width = 20,font = 25,bg = "skyblue")
l16 = Label(win,text = "Date due:",width = 20,font = 25,bg = "skyblue")
l17 = Label(win,text = "Days on loan:",width = 20,font = 25,bg = "skyblue")
l18 = Label(win,text = "Late return fine:",width = 20,font = 25,bg = "skyblue")
l19= Label(win,text = "Date over Due:",width = 20,font = 25,bg = "skyblue")
l20= Label(win,text = "selling price:",width = 20,font = 25,bg = "skyblue")

# place all labels
l3.place(x = 20,y=100)
l4.place(x = 20,y = 140)
l5.place(x=20,y=180)
l6.place(x=20,y=220)
l7.place(x=20,y=260)
l8.place(x=20,y=300)
l9.place(x=20,y=340)
l10.place(x=20,y=380)
l11.place(x=20,y=420)
l12.place(x=360,y=100)
l13.place(x=360,y=140)
l14.place(x=360,y=180)
l15.place(x=360,y=220)
l16.place(x=360,y=260)
l17.place(x=360,y=300)
l18.place(x=360,y=340)
l19.place(x=360,y=380)
l20.place(x=360,y=420)

# entry box
e1 = Entry(win,textvar = member,width = 20,bg="grey")
e2 = Entry(win,textvar = reference,width = 20,bg="grey")
e3 = Entry(win,textvar = title,width =20,bg="grey")
e4 = Entry(win,textvar = firstname,width = 20,bg="grey")
e5 = Entry(win,textvar= surname,width=20,bg="grey")
e6 = Entry(win,textvar = address1,width = 20,bg="grey")
e7 = Entry(win,textvar = address2,width = 20,bg="grey")
e8 = Entry(win,textvar = postcode,width = 20,bg="grey")
e9 = Entry(win,textvar = mobile,width = 20,bg="grey")
e10 = Entry(win,textvar = bookid,width = 20,bg="grey")
e11 = Entry(win,textvar = booktitle,width = 20,bg="grey")
e12 = Entry(win,textvar = author,width = 20,bg="grey")
e13 = Entry(win,textvar = dateborrowed,width = 20,bg="grey")
e14 = Entry(win,textvar = datedue,width = 20,bg="grey")
e15 = Entry(win,textvar = daysonloan,width = 20,bg="grey")
e16 = Entry(win,textvar = latereturn,width = 20,bg="grey")
e17 = Entry(win,textvar = dateoverdue,width = 20,bg="grey")
e18 = Entry(win,textvar = sellingprice,width = 20,bg="grey")

# placing entry box
e1.place(x=220,y=100)
e2.place(x = 220,y = 140)
e3.place(x=220 , y=180)
e4.place(x=220,y=220)
e5.place(x= 220,y=260)
e6.place(x=220,y=300)
e7.place(x=220,y=340)
e8.place(x=220,y=380)
e9.place(x=220,y=420)
e10.place(x = 560,y=100)
e11.place(x=560,y=140)
e12.place(x=560,y=180)
e13.place(x=560,y=220)
e14.place(x=560,y=260)
e15.place(x=560,y=300)
e16.place(x=560,y=340)
e17.place(x=560,y=380)
e18.place(x=560,y=420)

#create button
b1 = Button(win,text = "Add Data",width = 10,command = add,bg = "skyblue",font = ("bold",15))
"""
b2 = Button(win,text = "Display Data",width = 20,command = display)
"""
b3  = Button(win,text = "Clear Data",width = 10,command = clear,bg = "skyblue",font = ("bold",15))
"""
b4 = Button(win,text = "Delete Data",width = 20,command = delete)
b5 = Button(win,text = "Update Data",width = 20,command = update)
b6 = Button(win,text = "Exit",width = 20,command = Exit)
"""

#place button
b1.place(x = 20,y = 600)
b3.place(x=150,y=600)





win.mainloop()

