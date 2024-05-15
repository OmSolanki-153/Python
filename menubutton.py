import tkinter
window = tkinter.Tk()
window.title("Menubutton-Om Solanki")

def new():
    w1=tkinter.Tk()
def close():
    window.destroy()
mb = tkinter.Menubutton(window, text="File_132", activeforeground='red',relief='raised', direction='right')
menu_file = tkinter.Menu(mb,tearoff=1,title="Om")
mb["menu"] = menu_file
menu_file.add_command(label='New', command=new)
menu_file.add_command(label='exit', command=exit)
mb.grid()

window.mainloop()
