# File : SleepTrackerPage.py 
# Berisi kelas boundary SleepTrackerPage, yang bertanggung jawab untuk
# Mengatur hubungan antara kelas controller SleepTrackerController dengan pengguna luar 

import os
from tkinter import Spinbox
from customtkinter import *
from PIL import Image
from tkcalendar import Calendar 
# from Sleep.SleepTrackerController import SleepTrackerController

class SleepTrackerPage(CTk):

    # CONSTRUCTOR
    # Menginisialisasi seluruh frame dan fungsionalitas dari SleepTrackerPage
    def __init__(self, master):
        # Menetapkan master dari SleepTrackerPage yaitu master
        self.master = master

        # Menginisialisasi keberadaan objek controller
        self.sleep_controller = SleepTrackerController()

        # Menciptakan frame pertama tempat mengubah data sleep
        self.sleep_modif_frame = CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.sleep_modif_frame.grid_columnconfigure(1, weight=1)

        sleep_logo_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "images")
        sleep_logo_image = CTkImage(Image.open(os.path.join(sleep_logo_path, "logo.png")), size=(150,30))
        self.sleep_logo_image_label = CTkLabel(self.sleep_modif_frame, text="", image=sleep_logo_image)
        self.sleep_logo_image_label.grid(row=0, column=1, padx=(0,50), pady=(10,0), sticky="ne")

        self.date_label = CTkLabel(self.sleep_modif_frame, text="Date : ", font=CTkFont(size=30, weight="bold"))
        self.date_label.grid(row=1, column=0, padx=10, pady=50, columnspan=2)

        self.time_frame = CTkFrame(self.sleep_modif_frame, corner_radius=0, fg_color="transparent")
        self.time_frame.grid(row=2, column=0, columnspan=2)
        self.start_hour = StringVar()
        self.start_hour_spin = Spinbox(self.time_frame, from_=0, to=23, wrap=True, textvariable=self.start_hour, width=2, justify=CENTER)
        self.start_hour_spin.grid(row=1, column=0, padx=(50,0), pady=10)

        self.start_minute = StringVar()
        self.start_minute_spin = Spinbox(self.time_frame, from_=0, to=59, wrap=True, textvariable=self.start_minute, width=2, justify=CENTER)
        self.start_minute_spin.grid(row=1, column=1, padx=(50,0), pady=10)

        self.end_hour = StringVar()
        self.end_hour_spin = Spinbox(self.time_frame, from_=0, to=23, wrap=True, textvariable=self.end_hour, width=2, justify=CENTER)
        self.end_hour_spin.grid(row=1, column=2, padx=(50,0), pady=10)

        self.end_minute = StringVar()
        self.end_minute_spin = Spinbox(self.time_frame, from_=0, to=59, wrap=True, textvariable=self.end_minute, width=2, justify=CENTER)
        self.end_minute_spin.grid(row=1, column=3, padx=(50,0), pady=10)

        self.rating = CTkLabel(self.sleep_modif_frame, text="", font=CTkFont(size=20, weight="bold"))
        self.rating.grid(row=3, column=0, padx=110, pady=10, columnspan=2)
        self.rating_slider = CTkSlider(self.sleep_modif_frame, from_=1, to=5, number_of_steps=5, width=1000)
        self.rating_slider.grid(row=3, column=0, padx=100, pady=50, columnspan=2)

        self.save_button = CTkButton(self.sleep_modif_frame, text="Save", command=self.save_button_event)
        self.save_button.grid(row=4, column=1, padx=(50,0), pady=175)

    # GETTER
    # Mengembalikan frame pertama dan utama dari SleepTrackerPage
    def get_frame(self):
        return self.sleep_modif_frame
        
    
    # EVENT ACTION
    # Menyimpan record yang telah diubah oleh pengguna di frame ke file data
    def save_button_event(self):
        pass