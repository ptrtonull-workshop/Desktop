from tkinter import *
from app.sql import *
import app.main as main_page
def add(db, database,table):
    add=Tk()
    data = StringVar()
    def commfirm():
        res = data.get()
        datas=[]
        res +=","
        temp=''
        for i in res:
            if i==',':
                datas.append(temp)
                temp=''
            else:
                temp+=i
        insert(db,database,table,datas)
    def check():
        main_page.page(db,database,table)
    def close():
        add.destroy()
    E = Entry(add,textvariable=data).grid(row=0,column=1)
    Button(add, text = "取消",command = close).grid(row=1,column=1)
    Button(add,text = "确定",command = commfirm).grid(row=1,column=0)
    Button(add,text = "查看",command = check).grid(row=1,column =2)
    add.mainloop()