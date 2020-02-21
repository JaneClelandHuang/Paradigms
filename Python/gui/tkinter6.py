from tkinter import Tk, Label, Button

class app(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
		
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        self.label = tk.Label(self.root, text="")
        self.label.pack()
        self.root.bind('<Return>', self.callback)
        self.root.mainloop()


    def callback(self, event):
        self.label["text"] = "You pressed {}".format(event.keysym)
    
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()