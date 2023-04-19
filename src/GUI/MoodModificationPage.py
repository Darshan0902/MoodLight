import customtkinter
import os
import tkinter as tk
from PIL import Image
from tkcalendar import Calendar
from datetime import date
from Mood.MoodModificationController import MoodModificationController
from Utility.Date import Date

class MoodModificationPage(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.mood_controller = MoodModificationController()
        self.mood_modif_frame = customtkinter.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.mood_modif_frame.grid_columnconfigure(1, weight=1)
        mood_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "images")
        self.mood_logo_image = customtkinter.CTkImage(Image.open(os.path.join(mood_image_path, "logo.png")), size=(150,30))
        self.mood_logo_image_label = customtkinter.CTkLabel(self.mood_modif_frame, text="", image=self.mood_logo_image)
        self.mood_logo_image_label.grid(row=0, column=1, padx=(0,50), pady=(10,0), sticky="ne")

        self.today_date = date.today().strftime('%d-%m-%Y')
        self.curr_date = self.today_date
        self.mood_label_1 = customtkinter.CTkLabel(self.mood_modif_frame, text="Date : " + self.curr_date, font=customtkinter.CTkFont(size=30, weight="bold"))
        self.mood_label_1.grid(row=1, column=0, padx=10, pady=50, columnspan=2)
        self.mood_label_2 = customtkinter.CTkLabel(self.mood_modif_frame, text="How would you rate your mood today ?", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.mood_label_2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        
        self.sliderRate = customtkinter.CTkSlider(self.mood_modif_frame, from_=1, to=5, number_of_steps=5, width=1000)
        self.sliderRate.grid(row=3, column=0, padx=100, pady=50, columnspan=2)
        self.rate = customtkinter.CTkLabel(self.mood_modif_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.rate.grid(row=3, column=0, padx=110, pady=10, columnspan=2)
        self.sliderRelax = customtkinter.CTkSlider(self.mood_modif_frame, from_=1, to=5, number_of_steps=5, width=1000)
        self.sliderRelax.grid(row=5, column=0, padx=100, pady=50, columnspan=2)
        self.relax = customtkinter.CTkLabel(self.mood_modif_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.relax.grid(row=5, column=0, padx=110, pady=10, columnspan=2)
        self.sliderEnergy = customtkinter.CTkSlider(self.mood_modif_frame, from_=1, to=5, number_of_steps=5, width=1000)
        self.sliderEnergy.grid(row=7, column=0, padx=100, pady=50, columnspan=2)
        self.energy = customtkinter.CTkLabel(self.mood_modif_frame, text="", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.energy.grid(row=7, column=0, padx=110, pady=10, columnspan=2)

        if self.mood_controller.isInRecord(self.curr_date) : # Jika data ada, ambil dari file
            _, rate, relax, energy = self.mood_controller.readRecord(self.curr_date)
            self.sliderRate.set(int(rate))
            self.sliderRelax.set(int(relax))
            self.sliderEnergy.set(int(energy))

        self.mood_label_3 = customtkinter.CTkLabel(self.mood_modif_frame, text="How relaxed are you ?", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.mood_label_3.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        self.mood_label_4 = customtkinter.CTkLabel(self.mood_modif_frame, text="How would you rate your mood today ?", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.mood_label_4.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

        self.mood_history = customtkinter.CTkButton(self.mood_modif_frame, text="Mood History", command=lambda:self.mood_history_button_event(self.mood_modif_frame))
        self.mood_history.grid(row=8, column=0, padx=(500,0), pady=10)
        
        self.mood_save = customtkinter.CTkButton(self.mood_modif_frame, text="Save", command=self.save_button_event)
        self.mood_save.grid(row=8, column=1, padx=(50,0), pady=10)

    def mood_history_button_event(self, master):
        # self.mood_modif_frame.grid_forget()
        # self.master = master
        self.mood_label_1.grid_forget()
        self.mood_label_2.grid_forget()
        self.sliderRate.grid_forget()
        self.rate.grid_forget()
        self.sliderRelax.grid_forget()
        self.relax.grid_forget()
        self.sliderEnergy.grid_forget()
        self.energy.grid_forget()
        self.mood_label_3.grid_forget()
        self.mood_label_4.grid_forget()
        self.mood_history.grid_forget()
        self.mood_save.grid_forget()
        self.mood_history_label_1 = customtkinter.CTkLabel(self.mood_modif_frame, text="Your mood in the past week ", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.mood_history_label_1.grid(row=1, column=0, padx=10, pady=50, columnspan=2)
        # self.graph = 
        self.mood_edit_history = customtkinter.CTkButton(self.mood_modif_frame, text="Edit Record", command=self.open_calendar)
        self.mood_edit_history.grid(row=8, column=0, padx=(500,0), pady=10)
        self.mood_return = customtkinter.CTkButton(self.mood_modif_frame, text="Return", command=self.mood_return_button_event)
        self.mood_return.grid(row=8, column=1, padx=100, pady=10)

    def open_calendar(self):
        self.calendar = Calendar(self.mood_modif_frame, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendar.grid(row=9, column=0, padx=10)
        self.open_button = tk.Button(self.mood_modif_frame, text="Open Date", command=self.open_data)
        self.open_button.grid(row=10, column=0, padx=10, pady=10)
        self.error_label = customtkinter.CTkLabel(self.mood_modif_frame, text="", text_color="red")
        self.error_label.grid(row=11, column=0, padx=10, pady=10)

    def open_data(self):
        selected_date = self.calendar.selection_get().strftime('%d-%m-%Y')
        # print(f"Membuka data untuk tanggal {selected_date}")
        if (Date(selected_date) > Date(self.today_date)) : # Tanggal yang dipilih tidak valid (lebih dari tanggal hari ini)
            self.error_label.configure(text="Date not valid")
        else :
            self.curr_date = selected_date
            self.mood_label_1.configure(text="Date : " + self.curr_date)
            if self.mood_controller.isInRecord(self.curr_date) : # Jika data ada, ambil dari file
                _, rate, relax, energy = self.mood_controller.readRecord(self.curr_date)
                self.sliderRate.set(int(rate))
                self.sliderRelax.set(int(relax))
                self.sliderEnergy.set(int(energy))
            else : 
                self.sliderRate.set(1)
                self.sliderRelax.set(1)
                self.sliderEnergy.set(1)
            # Mengembalikan tampilan ke tampilan modifikasi data
            self.mood_return_button_event()

    def mood_return_button_event(self):
        # Mengembalikan tampilan ke tampilan modifikasi data
        self.mood_label_1.grid(row=1, column=0, padx=10, pady=50, columnspan=2)
        self.mood_label_2.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.sliderRate.grid(row=3, column=0, padx=100, pady=50, columnspan=2)
        self.rate.grid(row=3, column=0, padx=110, pady=10, columnspan=2)
        self.sliderRelax.grid(row=5, column=0, padx=100, pady=50, columnspan=2)
        self.relax.grid(row=5, column=0, padx=110, pady=10, columnspan=2)
        self.sliderEnergy.grid(row=7, column=0, padx=100, pady=50, columnspan=2)
        self.energy.grid(row=7, column=0, padx=110, pady=10, columnspan=2)
        self.mood_label_3.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
        self.mood_label_4.grid(row=6, column=0, padx=10, pady=10, columnspan=2)
        self.mood_history.grid(row=8, column=0, padx=(500,0), pady=10)
        self.mood_save.grid(row=8, column=1, padx=(50,0), pady=10)
        self.mood_history_label_1.grid_forget()
        self.mood_edit_history.grid_forget()
        self.mood_return.grid_forget()
        self.calendar.grid_forget()
        self.open_button.grid_forget()
        self.error_label.grid_forget()

    def save_button_event(self):
        if(self.mood_controller.isInRecord(self.curr_date)) :
            self.mood_controller.updateRecord(self.curr_date, int(self.sliderRate.get()), int(self.sliderRelax.get()), 
                                              int(self.sliderEnergy.get()))
        else :
            self.mood_controller.createRecord(self.curr_date, int(self.sliderRate.get()), int(self.sliderRelax.get()), 
                                              int(self.sliderEnergy.get()))
    
    def get_frame(self):
        return self.mood_modif_frame