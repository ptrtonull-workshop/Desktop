from app.app import *
db = create(account)
def yes():
    find(db,'test','sc')

sss = Tk()
Button(sss, text='修改',command = yes).grid(row=2,column=1)
sss.mainloop()