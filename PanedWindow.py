import tkinter
window = tkinter.Tk()
window.title("PanedWindow - Om Solanki")
window.geometry('500x500')

pw1 = tkinter.PanedWindow(window)
pw2 = tkinter.PanedWindow(window)

t = tkinter.Text(pw1,height=5,width=25)
lb = tkinter.Listbox(pw2,selectmode='single',height=4)
lb.insert('end','PP','DS','CN','DBMS','AM','CJ','IES','COST','SE','CGA')

s1 = tkinter.Scrollbar(pw1)
s1['command'] = t.yview
t['yscrollcommand'] = s1.set

s2 = tkinter.Scrollbar(pw2)
s2['command'] = lb.yview
lb['yscrollcommand'] = s2.set

pw1.grid(row=1,column=1)
pw1.add(t)
pw1.add(s1)

pw2.grid(row=1,column=2,sticky='nw')
pw2.add(lb)
pw2.add(s2)

window.mainloop()
