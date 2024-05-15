import tkinter
import tkinter.messagebox
window = tkinter.Tk()
window.title("Menu-Om Solanki")

def new():
    w1 = tkinter.Tk()
def openfile():
    filename = tkinter.filedialog.askopenfilename()
    m = tkinter.messagebox.showinfo("132",filename)

def close(event=""):
    window.destroy()

def colorY():
    window["background"]="yellow"

def colorC():
    window.configure(background="cyan")

def colorW():
    window.configure(background="white")

def colorK():
    window.configure(background="black")

menu = tkinter.Menu(window)
menu_file = tkinter.Menu(menu,tearoff=0)

menu_file.add_command(label ="New",command=new)
menu_file.add_command(label ="Open",command=openfile)
menu_file.add_separator()
menu_file.add_command(label ="Exit",command=close,accelerator='Ctrl-X')
menu.add_cascade(label='File',menu=menu_file)

menu_color=tkinter.Menu(menu,tearoff=0)
menu_color.add_command(label='Yellow',command=colorY)
menu_color.add_command(label='Cyan',command=colorC)
menu_color.add_command(label='White',command=colorW)
menu_color.add_command(label='Black',command=colorK)
menu.add_cascade(label='Color',menu=menu_color)

popup = tkinter.Menu(window,tearoff=0)
popup.add_command(label='White',command=colorW)
popup.add_command(label='Black',command=colorK)

def disp_popup(event):
    popup.tk_popup(event.x_root,event.y_root)
    popup.grab_release()

window["menu"]=menu
window.bind("<Button-3>",disp_popup)
window.bind('<Control-x>',close)
window.mainloop()
    
    
