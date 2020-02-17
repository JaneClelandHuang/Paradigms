from tkinter import *
from tkinter import ttk
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
# Label that act as a "Title" something like an H1
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
 
lbl.grid(column=0, row=0)
 
# Tabs
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='First')
 
tab_control.add(tab2, text='Second')
 
lbl1 = Label(tab1, text= 'label1')
 
lbl1.grid(column=0, row=2)
 
lbl2 = Label(tab2, text= 'label2')
 
lbl2.grid(column=0, row=2)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()