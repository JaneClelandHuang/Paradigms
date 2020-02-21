from tkinter import *

wn = Tk()
wn.title('KeyDetect')

m = 0

def down(e):
    if m == 0:
        print('Down\n', e.char, '\n', e)
        global m
        m = 1

def up(e):
    if m == 1:
        print('Up\n', e.char, '\n', e)
        global m
        m = 0

wn.bind('<KeyPress>', down)
wn.bind('<KeyRelease>', up)

wn.mainloop()