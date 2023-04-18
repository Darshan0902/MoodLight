import tkinter as tk

class Mood:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(self.frame, text="Ini adalah halaman Mood")
        self.label.pack()
    
    def get_frame(self):
        return self.frame
