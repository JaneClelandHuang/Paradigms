import tkinter as tk

class Window1:
    def __init__(self, master):
        pass
        # Create labels, entries,buttons
    def button_click(self):
        pass
        # If button is clicked, run this method and open window 2


class Window2:
    def __init__(self, master):
        #create buttons,entries,etc

    def button_method(self):
        #run this when button click to close window
        self.master.destroy()

def main(): #run mianloop 
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
