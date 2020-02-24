from tkinter import * 
root = Tk()


class keyPresser():  
    def handle_down_key(self,event):
        self.canvas.focus_set()    
        print('Down arrow key pressed')

    def __init__(self):   
        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.bind("<Down>", self.fred)
        self.canvas.focus()
        self.canvas.pack()
 
mm = keyPresser()
root.mainloop()

