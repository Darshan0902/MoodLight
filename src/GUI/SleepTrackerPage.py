# File : SleepTrackerPage.py 
# Berisi kelas boundary SleepTrackerPage, yang bertanggung jawab untuk
# Mengatur hubungan antara kelas controller SleepTrackerController dengan pengguna luar 

import os
from datetime import date
from tkinter import Spinbox
from customtkinter import *
import tkinter as tk
from tkinter.font import Font
from PIL import Image
from tkcalendar import Calendar 
from Sleep.SleepTrackerController import SleepTrackerController
from Utility.Statistics import Statistics
from Utility.Date import Date

class SleepTrackerPage(CTk):

    # CONSTRUCTOR
    # Menginisialisasi seluruh frame dan fungsionalitas dari SleepTrackerPage
    def __init__(self, master):
        # Menetapkan master dari SleepTrackerPage yaitu master
        self.master = master

        # Menginisialisasi keberadaan objek controller, objek statistik, dan atribut dinamis
        self.sleep_controller = SleepTrackerController()
        self.initialize_frame_attributes()

        # Menginisiasi frame page dan membuat frame modif dan stats
        self.sleep_frame = CTkScrollableFrame(self.master, corner_radius=0, fg_color="#568ea6")
        self.sleep_frame.grid_columnconfigure(1, weight=1)
        self.create_modif_frame_elements()
        self.create_stats_frame_elements()

        # Konfigurasi data untuk frame pertama
        self.place_modif_frame()
        self.configure_modif_frame()

    # INITIALIZER
    # Menciptakan variabel-variabel dinamis page
    def initialize_frame_attributes(self):
        self.sleep_logo_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "img")
        self.start_hour = StringVar()
        self.start_minute = StringVar()
        self.end_hour = StringVar()
        self.end_minute = StringVar()
        self.evaluation = StringVar()
        self.today = date.today().strftime("%d-%m-%Y")
        self.selected_date = self.today

    # CREATOR
    # Menciptakan frame pertama tempat mengubah record sleep
    def create_modif_frame_elements(self):
        sleep_logo_image = CTkImage(Image.open(os.path.join(self.sleep_logo_path, "logo.png")), size=(150,30))
        self.sleep_logo_image_label = CTkLabel(self.sleep_frame, text="", image=sleep_logo_image)
        self.date_label = CTkLabel(self.sleep_frame, text="Date : " + self.selected_date, font=CTkFont(family="Segoe Script", size=35, weight="bold"), text_color="white")
        self.time_frame = CTkFrame(self.sleep_frame, corner_radius=0, fg_color="transparent")
        self.start_label = CTkLabel(self.time_frame, text="Sleep Time:", font=CTkFont(family = "Comic Sans MS", size=25, weight="bold"), text_color="white")
        self.start_hour_spin = Spinbox(self.time_frame, from_=0, to=23, wrap=True, textvariable=self.start_hour, width=4, justify=CENTER, font=Font(family='Helvetica', size=20))
        self.start_minute_spin = Spinbox(self.time_frame, from_=0, to=59, wrap=True, textvariable=self.start_minute, width=4, justify=CENTER, font=Font(family='Helvetica', size=20))
        self.end_label = CTkLabel(self.time_frame, text="Wake Time:", font=CTkFont(family = "Comic Sans MS", size=25, weight="bold"), text_color="white")
        self.end_hour_spin = Spinbox(self.time_frame, from_=0, to=23, wrap=True, textvariable=self.end_hour, width=4, justify=CENTER, font=Font(family='Helvetica', size=20))
        self.end_minute_spin = Spinbox(self.time_frame, from_=0, to=59, wrap=True, textvariable=self.end_minute, width=4, justify=CENTER, font=Font(family='Helvetica', size=20))
        self.rating_label = CTkLabel(self.sleep_frame, text="How good was your sleep?", font=CTkFont(family="Comic Sans MS", size=30, weight="bold"), text_color="white")
        self.rating_frame = CTkFrame(self.sleep_frame, corner_radius=0, fg_color="transparent")
        self.rating_slider = CTkSlider(self.rating_frame, from_=1, to=5, number_of_steps=4, width=1000, progress_color="#FAE900", button_color="white", button_hover_color="grey70")
        self.rating_start= CTkLabel(self.rating_frame, text="1", font=CTkFont(family="Comic Sans MS", size=30, weight="bold"), text_color="white")
        self.rating_end= CTkLabel(self.rating_frame, text="5", font=CTkFont(family="Comic Sans MS", size=30, weight="bold"), text_color="white")
        self.modif_bottom_frame = CTkFrame(self.sleep_frame, corner_radius=0, fg_color="transparent")
        self.history_button = CTkButton(self.modif_bottom_frame, text="Edit History", font=CTkFont(size=15, weight="bold"), command=self.history_button_event, height=40,fg_color="#305f72")
        self.save_button = CTkButton(self.modif_bottom_frame, text="Save", font=CTkFont(size=15, weight="bold"), command=self.save_button_event, height=40, fg_color="#305f72")

    # Menciptakan frame kedua tempat melihat statistik sleep
    def create_stats_frame_elements(self):
        self.stats_label = CTkLabel(self.sleep_frame, text="Your sleep in the past week ", font=CTkFont(family = "Comic Sans MS", size=40, weight="bold"), text_color="white")
        self.graph_image_label = CTkLabel(self.sleep_frame, text="")
        self.evaluation_label = CTkLabel(self.sleep_frame, textvariable=self.evaluation, font=CTkFont(family="Comic Sans MS", size=20), text_color="white")
        self.stats_bottom_frame = CTkFrame(self.sleep_frame, corner_radius=0, fg_color="transparent")
        self.edit_record_button = CTkButton(self.stats_bottom_frame, text="Edit Record", font=CTkFont(size=15, weight="bold"), command=self.edit_record_button_event, height=40, fg_color="#305f72")
        self.return_button = CTkButton(self.stats_bottom_frame, text="Return", font=CTkFont(size=15, weight="bold"), command=self.return_button_event, height=40, fg_color="#305f72")
        self.calendar_window = None

    # PLACER
    # Memasang seluruh elemen frame pertama pada grid yang sesuai
    def place_modif_frame(self):
        self.sleep_logo_image_label.grid(row=0, column=1, padx=(0,50), pady=(10,0), sticky="ne")
        self.date_label.grid(row=1, column=0, padx=(190,0), pady=(50, 40),sticky="w")
        self.time_frame.grid(row=2, column=0, pady=(50,20), columnspan=2)
        self.start_label.grid(row=0, column=0, padx=(20, 0))
        self.start_hour_spin.grid(row=0, column=1, padx=(50,0), pady=10)
        self.start_minute_spin.grid(row=0, column=2, padx=(50,0), pady=10)
        self.end_label.grid(row=0, column=3, padx=(200,0))
        self.end_hour_spin.grid(row=0, column=4, padx=(50,0), pady=10)
        self.end_minute_spin.grid(row=0, column=5, padx=(50,0), pady=10)
        self.rating_label.grid(row=3, column=0, padx=110, pady=(80,0), columnspan=2)
        self.rating_frame.grid(row=4, column=0, padx=100, pady=50, columnspan=2)
        self.rating_slider.grid(row=0, column=1)
        self.rating_start.grid(row=0, column=0)
        self.rating_end.grid(row=0, column=2)
        self.history_button.grid(row=0, column=0, padx=(200, 180))
        self.save_button.grid(row=0, column=1, padx=200)
        self.modif_bottom_frame.grid(row=5, column=0, columnspan=2, pady=(60,0))

    # Memasang seluruh elemen frame kedua pada grid yang sesuai
    def place_stats_frame(self):
        self.sleep_logo_image_label.grid(row=0, column=1, padx=(0,50), pady=(10,0), sticky="ne")
        self.stats_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))
        self.graph_image_label.grid(row=2, column=0,padx=50, pady=10, sticky="nsew", columnspan=2)
        self.evaluation_label.grid(row=3, column=0, columnspan=2, padx=50,pady=(10,0))
        self.stats_bottom_frame.grid(row=4, column=0, pady=(30,0), columnspan=2)
        self.edit_record_button.grid(row=0, column=0, padx=(0, 100))
        self.return_button.grid(row=0, column=1, padx=(100,0))

    # CONFIGURATOR
    # Mengubah data-data pada frame pertama
    def configure_modif_frame(self):
        if (self.sleep_controller.isInRecord(self.selected_date)):
            dateString, startTime, finishTime, rating = self.sleep_controller.readRecord(self.selected_date) 
            self.start_hour.set(startTime[0:2])
            self.start_minute.set(startTime[3:])
            self.end_hour.set(finishTime[0:2])
            self.end_minute.set(finishTime[3:])
            self.rating_slider.set(int(rating))
        else:
            self.start_hour.set("0")
            self.start_minute.set("0")
            self.end_hour.set("0")
            self.end_minute.set("0")
            self.rating_slider.set(1)


    # Mengubah data-data pada frame kedua
    def configure_stats_frame(self):
        sleep_statistics = Statistics(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "data","Sleep.csv"),"Sleep")
        sleep_statistics.generateStatistics()
        graph_image = CTkImage(Image.open(os.path.join(self.sleep_logo_path, "result.png")), size=(1000, 500))
        self.graph_image_label.configure(image=graph_image)
        self.evaluation.set(sleep_statistics.showInsights())

    # FORGETER
    # Menghapus seluruh elemen frame pertama
    def forget_modif_frame(self):
        self.sleep_logo_image_label.grid_forget()
        self.date_label.grid_forget()
        self.time_frame.grid_forget()
        self.rating_label.grid_forget()
        self.rating_frame.grid_forget()
        self.modif_bottom_frame.grid_forget()
    
    # Menghapus seluruh elemen frame kedua
    def forget_stats_frame(self):
        self.sleep_logo_image_label.grid_forget()
        self.stats_label.grid_forget()
        self.graph_image_label.grid_forget()
        self.evaluation_label.grid_forget()
        self.stats_bottom_frame.grid_forget()

    # GETTER
    # Mengembalikan frame pertama dan utama dari SleepTrackerPage
    def get_frame(self):
        return self.sleep_frame
    
    def get_start_time(self):
        start_time = f"0{self.start_hour.get()}:" if len(self.start_hour.get()) == 1 else f"{self.start_hour.get()}:"
        start_time += f"0{self.start_minute.get()}" if len(self.start_minute.get()) == 1 else f"{self.start_minute.get()}"
        return start_time
    
    def get_end_time(self):
        end_time = f"0{self.end_hour.get()}:" if len(self.end_hour.get()) == 1 else f"{self.end_hour.get()}:"
        end_time += f"0{self.end_minute.get()}" if len(self.end_minute.get()) == 1 else f"{self.end_minute.get()}"
        return end_time
    

    # EVENT ACTION
    # Menyimpan record yang telah diubah oleh pengguna di frame ke file data
    def save_button_event(self):
        if (0 <= int(self.start_hour.get()) <= 23 and 0 <= int(self.start_minute.get()) <= 59 and
            0 <= int(self.end_hour.get()) <= 23 and 0 <= int(self.end_minute.get()) <= 59):
            if (self.sleep_controller.isInRecord(self.selected_date)):
                self.sleep_controller.updateRecord(self.selected_date, self.get_start_time(), self.get_end_time(), int(self.rating_slider._output_value))
            else:
                self.sleep_controller.createRecord(self.selected_date, self.get_start_time(), self.get_end_time(), int(self.rating_slider._output_value))

    # Mengubah frame dari frame modif ke frame stats
    def history_button_event(self):
        self.forget_modif_frame()
        self.place_stats_frame()
        self.configure_stats_frame()

    # Mengubah frame dari frame stats ke frame modif
    def return_button_event(self):
        self.forget_stats_frame()
        self.place_modif_frame()
        self.configure_modif_frame()
        if(not self.calendar_window is None) :
            self.calendar_window.destroy()

    # Memunculkan kalendar untuk memilih tanggal record
    def edit_record_button_event(self):
        if self.calendar_window is None or not self.calendar_window.winfo_exists() :
            self.calendar_window = CTkToplevel()
            self.calendar_window.title("Calendar")
        self.calendar = Calendar(self.calendar_window, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendar.grid(row=0, column=0, padx=10)
        self.open_button = CTkButton(self.calendar_window, text="Open Date", command=self.open_date_event)
        self.open_button.grid(row=1, column=0, padx=10, pady=(10, 3))
        self.error_label = CTkLabel(self.calendar_window, text="", text_color="red")
        self.error_label.grid(row=2, column=0, padx=10, pady=10)
        self.calendar_window.grab_set()

    # Memunculkan record pada tanggal tertentu
    def open_date_event(self):
        chosen = self.calendar.selection_get().strftime('%d-%m-%Y')
        if (Date(chosen) > Date(self.today)):
            self.error_label.configure(text="Date not valid")
        else:
            self.selected_date = chosen
            self.date_label.configure(text="Date : " + self.selected_date)
            self.return_button_event()