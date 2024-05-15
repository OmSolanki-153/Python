import tkinter
import tkinter.messagebox
window = tkinter. Tk()
window.title("Listbox - Om Solanki")
def list1():
    if lb1.curselection()==():
        m = tkinter.messagebox.showinfo("List 1-132","No element selected")
    else:
        value = lb1.get('active')
        m = tkinter.messagebox.showinfo("List 1-132", value)

def list2():
    lb2.see(0)
def list3():
    s = lb3.size()
    m = tkinter.messagebox.showinfo("List 3-132", "Total Elements = " + str(s))
def list4():
    if lb4.curselection()==():
        m = tkinter.messagebox.showinfo("List 4-132", "No element selected")
    else:
        v = ''
        for i in lb4.curselection():
            v= v + "\n" + lb4.get(i)
        m = tkinter.messagebox.showinfo("List 4-132", v)
lb1 = tkinter.Listbox(window)
lb2 = tkinter.Listbox(window,activestyle='dotbox', bg='#eefcab', selectbackground='#aa12cf',selectmode ='single', height=3)
lb3 = tkinter.Listbox(window, selectmode='multiple')
lb4 = tkinter.Listbox(window, selectmode='extended')
lb1.insert('end', 'IP', 'DE', 'OS', 'DM', 'CS')
lb2.insert('end', 'OOPs', 'MA','WP', 'NSM', 'GC')
lb3.insert('end', 'PP', 'DS', 'CN', 'DBMS', 'AM')
lb4.insert('end', 'CJ', 'IES', 'COST', 'SE', 'CGA')
b1 = tkinter.Button(window, text="List 1", command=list1)
b2 = tkinter.Button(window, text="List 2", command=list2)
b3 = tkinter.Button(window, text="List 3", command=list3)
b4 = tkinter.Button(window, text="List 4", command=list4)
lb1.grid(row=1, column=1, padx=10, pady=10)
lb2.grid(row=1, column=2, padx=10, pady=10)
lb3.grid(row=1, column=3, padx=10, pady=10)
lb4.grid(row=1, column=4, padx=10, pady=10)
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)
b3.grid(row=2, column=3)
b4.grid(row=2, column=4)
window.mainloop()
