from tkinter import * 
root = Tk()
def keyup(e):
    #print('up', e.char)
	print("You pressed up")
def keydown(e):
    print ('down', e.char)

frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()