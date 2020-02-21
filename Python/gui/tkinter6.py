from tkinter import *
 
root = Tk()
 
def key(event):
    kp = repr(event)
    print ("pressed", kp)
    if (kp == 'x'):
        print ("pressed x", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)
 
frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
 
root.mainloop()