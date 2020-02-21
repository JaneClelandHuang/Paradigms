import tkinter as tk

app = tk.Tk()
app.geometry("200x100")

def callback(event):
    label["text"] = "You pressed Enter"

app.bind('<Return>', callback)

label = tk.Label(app, text="")
label.pack()

app.mainloop()