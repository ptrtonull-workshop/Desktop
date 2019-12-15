from tkinter import *
from app.sql import *
from app.insert import*
from app.set import*
from app.search import *
def page(db, database, table):
    mainPage = Tk()
    Label(mainPage,text="table "+table+" in "+database).grid(row=0)
    L = Listbox(mainPage)
    L.grid(row=1)
    def destroy_win():
        mainPage.destroy()
    def insert_data():
        destroy_win()
        add(db,database,table)
    def updata_data():
        no = L.curselection()
        set_f(db,database,table,no[0]-1)
    def delete_data():
        no = L.curselection()
        delete(db,database,table,no[0]-1)
        data = display(db,database,table)
        L.delete(0,END)
        L.insert('end',meta)
        for j in data:
            L.insert("end",j)
    def search_data():
        find(db,database,table)
    def refresh():
        data = display(db,database,table)
        L.delete(0,END)
        L.insert('end',meta)
        for j in data:
            L.insert("end",j)
    Button(mainPage, text='I know.',command = destroy_win).grid(row=4,column=2)
    Button(mainPage, text='刷新',command = refresh).grid(row=4,column=1)
    Button(mainPage, text='插入',command = insert_data).grid(row=2,column=0)
    Button(mainPage, text='修改',command = updata_data).grid(row=2,column=1)
    Button(mainPage, text='删除',command = delete_data).grid(row=3,column=0)
    Button(mainPage, text='查找',command = search_data).grid(row=3,column=1)
    meta = showMeta(db,database,table)
    data = display(db,database,table)
    L.insert('end',meta)
    for j in data:
        L.insert("end",j)
    mainPage.mainloop()
