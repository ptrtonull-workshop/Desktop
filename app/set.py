from tkinter import *
from app.sql import *
import app.main as main_page
def set_f(db, database,table,position):
    set_win = Toplevel()  # 有关Entry控件的函数做子函数时，如果用Tk()，会接收不到值
    # 具体的看这篇文章的评论区：https://blog.csdn.net/liyuan3970/article/details/82874653
    data_set_f = StringVar()
    def commfirm():
        res = data_set_f.get()
        datas=[]
        res +=":"
        temp=''
        for i in res:
            if i==':':
                datas.append(temp)
                temp=''
            else:
                temp+=i
        meta_data=datas[0]
        value = datas[1]
        update(db,database,table,position,meta_data,value)
        data = display(db,database,table)
        close()
    def check():
        main_page.page(db,database,table)
    def close():
        set_win.destroy()
    E = Entry(set_win,textvariable=data_set_f).grid(row=0,column=1)
    Button(set_win, text = "取消",command = close).grid(row=1,column=1)
    Button(set_win, text = "确定",command = commfirm).grid(row=1,column=0)
    Button(set_win, text = "查看",command = check).grid(row=1,column =2)
    set_win.mainloop()