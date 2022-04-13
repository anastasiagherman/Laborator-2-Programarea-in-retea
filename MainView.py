import tkinter as tk
from FirstPage import FirstPage
from InboxPage import InboxPage

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = FirstPage(self)
        p1.config(bg="light blue")
        p2 = InboxPage(self)
        p2.config(bg="light blue")

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="right", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Send E-Mail", command=p1.lift, bg = "cyan")
        b2 = tk.Button(buttonframe, text="View inbox", command=p2.lift, bg = "cyan")

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()