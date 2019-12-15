from tkinter import *
from app.sql import *
from app.insert import*
def page(db, database, table):
    mainPage = Tk()
    Label(mainPage,text=table+"in"+database).pack()
    L = Listbox(mainPage)
    L.pack()
    def destroy_win():
        mainPage.destroy()
    def insert_data():
        destroy_win()
        add(db,database,table)
    Button(mainPage, text='I know.',command = destroy_win).pack()
    Button(mainPage, text='插入',command = insert_data).pack()
    meta = showMeta(db,database,table)
    data = display(db,database,table)
    L.insert('end',meta)
    for j in data:
        L.insert("end",j)
    mainPage.mainloop()
