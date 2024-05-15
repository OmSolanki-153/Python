import tkinter
window = tkinter.Tk()
window.title("Message-Om Solanki")
window.geometry('500x500')

def msg1():
    m=tkinter.messagebox.showinfo("132","Om Solanki")
def msg2():
    m=tkinter.messagebox.showwarning("132","Om Solanki")
def msg3():
    m=tkinter.messagebox.showerror("132","Om Solanki")
def msg4():
    if(tkinter.messagebox.askyesno("132","Exit",default='no')):
        window.destroy()
def msg5():
    if(tkinter.messagebox.askokcancel("132","Exit")):
        window.destroy()
def msg6():
    if(tkinter.messagebox.askretrycancel("132","Exit")):
        window.destroy()

b1=tkinter.Button(window,text="Show Info",command=msg1)
b2=tkinter.Button(window,text="Show Warning",command=msg2)
b3=tkinter.Button(window,text="Show Error",command=msg3)
b4=tkinter.Button(window,text="Ask Yes/No",command=msg4)
b5=tkinter.Button(window,text="Ask Ok/Cancel",command=msg5)
b6=tkinter.Button(window,text="Ask Retry/Cancel",command=msg6)

b1.pack(expand=True)
b2.pack(expand=True)
b3.pack(expand=True)
b4.pack(expand=True)
b5.pack(expand=True)
b6.pack(expand=True)

Window.mainloop()
