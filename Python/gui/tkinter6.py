from tkinter import *

wn = Tk()
wn.title('KeyDetect')

m = 0

def down(e):
    print('Down\n', e.char, '\n', e)

def up(e):
    print('Up\n', e.char, '\n', e)

wn.bind('<KeyPress>', down)
wn.bind('<KeyRelease>', up)

wn.mainloop()