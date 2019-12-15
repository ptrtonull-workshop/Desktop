from tkinter import *
from app.sql import *
from app.insert import*
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
        print()
    def delete_data():
        print()
    def search_data():
        find(db,database,table)
        
    Button(mainPage, text='I know.',command = destroy_win).grid(row=4,column=2)
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
