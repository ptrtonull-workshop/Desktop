import tkinter as tk


# Main_window
def main_window():
    main_window = tk.Tk()
    main_window.iconbitmap('C:/Users/97607/Documents/GitHub/Python/Desktop/app/bitbug_favicon.ico')
    main_window.title('片源下载软件')

    main_window.geometry('800x600')

    # main title
    title = tk.Label(main_window,text='欢迎使用片源下载！',font=('楷体',20),width=30,height=2).place(x=200,y=10,anchor='nw')

    #menubar
    menubar = tk.Menu(main_window)
    
    moviemenu = tk.Menu(menubar,tearoff=0)  #movie informaition:including searching,(and ....what?)
    userinfo  = tk.Menu(menubar,tearoff=0)  #user infomation:including history,downloading files 

    menubar.add_cascade(label='电影',menu=moviemenu)
    menubar.add_cascade(label='用户',menu=moviemenu)

    moviemenu.add_command(label='查询电影',command=find_movie)
    
    userinfo.add_command(labe='历史记录',command=history)


    #Today recommand
    recom_title = tk.Label(main_window,text='今日推荐',font=('宋体',13),width=10,height=2).place(x=50,y=60,anchor='nw')

    #height:760







    
    main_window.config(menu=menubar)

    main_window.mainloop()









# The window of find_moive
#function:use to create a window which have the function of finding movies
def find_movie():
    find_window = tk.Tk()
    find_window.title('查询')

    find_window.geometry('500x400')

    find_window.mainloop()

# The window of history
#function: find the movie which has been searched
def history():
    history_window = tk.Tk()
    history_window.title('历史记录')

    history_window.geometry('500x400')

    history_window.mainloop()


def splash():
    root = tk.Tk()
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8,
                                   width*0.1, height*0.1))
    # 保存成gif格式。（但是没法显示动图，待解决。）
    image_file = "C:/Users/97607/Documents/gitHub/Python/Desktop/app/__pycache__/movie.png"
    #assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=height*0.8, 
                            width=width*0.8, bg="white")
    canvas.create_image(width*0.8/2, height*0.8/2, image=image)
    canvas.pack()
    # 设置splash显示的时间，单位是毫秒（milliseconds）
    root.after(4000, root.destroy)
    root.mainloop()



if __name__ == "__main__":
    splash()
    main_window()





