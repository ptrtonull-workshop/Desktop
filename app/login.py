from tkinter import *
from app.sql import *
from app.main import*


def listTables(db, database):
    data  = show_Tables(db,database)
    showTables =Tk()
    def destroy_tables_win():
        showTables.destroy()
    Label(showTables, text="The tables in database:").pack()
    L = Listbox(showTables)
    L.pack()
    def choice():
        res = L.curselection()
        table = data[res[0]]
        page(db,database,table)
        destroy_tables_win()
    Button(showTables, text="I know.", command=destroy_tables_win).pack()
    Button(showTables,text='选中',command = choice).pack()
    for i in data:
        L.insert("end", i)
    showTables.mainloop()



def listDatabases(db,data):
    showDatabases = Tk()

    def destroy_database_win():
        showDatabases.destroy()

    Label(showDatabases, text="The Databases in mysql:").pack()
    L = Listbox(showDatabases)
    L.pack()
    def choice():
        res = L.curselection()
        database = data[res[0]]
        listTables(db,database)
        destroy_database_win()
    Button(showDatabases, text="I know.", command=destroy_database_win).pack()
    Button(showDatabases,text='选中',command = choice).pack()
    for i in data:
        L.insert("end", i)
    showDatabases.mainloop()


def loginFail():
    loginfail = Tk()

    def destroy_win():
        loginfail.destroy()

    Label(loginfail, text="login failed, inf incorrect!").pack()
    Button(loginfail, text="I know.", command=destroy_win).pack()
    loginfail.mainloop()


def login():
    loginin = Tk()
    loginin.title("loginIn")
    host = StringVar()
    username = StringVar()
    password = StringVar()

    def loginF():
        global account
        account["host"] = host.get()
        account["username"] = username.get()
        account["password"] = password.get()
        account["host"] = account["host"]
        account["username"] = account["username"]
        account["password"] = account["password"]
        db = create(account)
        if db == False:
            loginFail()
        else:
            listDatabases(db,show(db))

    def quitF():
        loginin.destroy()

    Label(loginin, text="host").grid(row=0, column=0)
    Entry(loginin, bd=2, textvariable=host).grid(row=0, column=1)
    Label(loginin, text="username").grid(row=1, column=0)
    Entry(loginin, bd=2, textvariable=username).grid(row=1, column=1)
    Label(loginin, text="password").grid(row=2, column=0)
    Entry(loginin, bd=2, textvariable=password).grid(row=2, column=1)
    Button(loginin, text="login", command=loginF).grid(row=3, column=0)
    Button(loginin, text="quit", command=quitF).grid(row=3, column=1)
    loginin.mainloop()