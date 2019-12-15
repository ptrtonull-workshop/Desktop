from tkinter import *
from app.sql import *
import app.main as main_page

def display_res(meta,res):
    display_res_win = Tk()

    def destroy_win():
        display_res_win.destroy()

    L = Listbox(display_res_win)
    L.pack()
    for i in range(len(res)):
        L.insert("end","attribute "+str(meta[i]))
        for j in res[i]:
            temp=""
            for m in j:
                temp+=str(m)+" "
            L.insert("end",temp)
    Button(display_res_win, text="I know.", command=destroy_win).pack()
    display_res_win.mainloop()

def find(db, database,table):
    find = Toplevel()
    find_data = StringVar()
    def commfirm():
        res = find_data.get()
        datas = select(db, database, table, res)
        meta = showMeta(db, database, table)
        display_res(meta, datas)
    def close():
        find.destroy()
    E = Entry(find, textvariable=find_data)
    E.grid(row=0,column=1)
    print(E.get())
    Button(find, text = "取消", command = close).grid(row=1,column=1)
    Button(find, text = "确定", command = commfirm).grid(row=1,column=0)
    find.mainloop()