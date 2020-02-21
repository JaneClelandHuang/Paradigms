from tkinter import *
print("Hello there")
main = Tk()

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

frame = Frame(main, width=100, height=100)
frame.bind('<Left>', leftKey)
frame.bind('<Right>', rightKey)
frame.focus_set()
frame.pack()
main.mainloop()