#!/usr/bin/python3.8

import tkinter as tk
from MainView import MainView

if __name__ == "__main__":
    root = tk.Tk(className=" Mail Agent")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x600")
    root.mainloop()