# File : DiaryModificationPage.py 
# Berisi kelas boundary DiaryModificationPage, yang bertanggung jawab untuk
# Mengatur hubungan antara kelas controller DiaryModificationController dengan pengguna luar 

import customtkinter
import os
import tkinter as tk
from PIL import Image
from tkcalendar import Calendar
from datetime import date
from Utility.Date import Date
from Diary.DiaryModificationController import DiaryModificationController

class DiaryModificationPage(customtkinter.CTk):

    # CONSTRUCTOR
    # Menginisialisasi seluruh frame dan fungsionalitas dari DiaryModificationPage
    def __init__(self, master):
        # Menetapkan master dari DiaryModificationPage yaitu master
        self.master = master

        # Membuat objek controller untuk memodifikasi data diary
        self.diary_controller = DiaryModificationController()

        # Menciptakan frame pertama tempat mengubah data diary
        self.diary_modif_frame = customtkinter.CTkFrame(self.master, corner_radius=0, fg_color="#568ea6")
        self.diary_modif_frame.grid_columnconfigure(1, weight=1)
        
        diary_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "img")
        self.diary_logo_image = customtkinter.CTkImage(Image.open(os.path.join(diary_image_path, "logo.png")), size=(150,30))
        self.diary_logo_image_label = customtkinter.CTkLabel(self.diary_modif_frame, text="", image=self.diary_logo_image)
        self.diary_logo_image_label.grid(row=0, column=1, padx=(0,50), pady=(10,0), sticky="ne")
        
        self.date = date.today().strftime('%d-%m-%Y')
        self.curr_date = self.date

        self.diary_date_label = customtkinter.CTkLabel(self.diary_modif_frame, text="Date : " + self.curr_date, font=customtkinter.CTkFont(family="Segoe Script", size=35, weight="bold"), text_color="white")
        self.diary_date_label.grid(row=1, column=0, padx=190, pady=(50,10), columnspan=2, sticky="w")
        
        self.diary_textbox = customtkinter.CTkTextbox(self.diary_modif_frame, width=1000, height=500, border_width=2)
        self.diary_textbox.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.diary_textbox.delete("0.0","end")
        if (self.diary_controller.isInRecord(self.curr_date)) :
            _, content = self.diary_controller.readRecord(self.curr_date)
            self.diary_textbox.insert("0.0",content)

        self.diary_entry = customtkinter.CTkButton(self.diary_modif_frame, text= "Previous Entry", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.diary_open_calendar, height=40, fg_color="#305f72")
        self.diary_entry.grid(row=8, column=0, padx=(400,0), pady=10)
        
        self.diary_save = customtkinter.CTkButton(self.diary_modif_frame, text="Save", font=customtkinter.CTkFont(size=15, weight="bold"), command=self.diary_save_button_event, height=40, fg_color="#305f72")
        self.diary_save.grid(row=8, column=1, padx=100, pady=10)

        self.top_window = None

    # GETTER
    # Mengembalikan frame pertama dan utama dari DiaryModificationPage
    def get_frame(self):
        return self.diary_modif_frame
    
    # EVENT ACTION
    # Membuka kalendar untuk melihat data pada hari itu
    def diary_open_calendar(self):
        if self.top_window is None or not self.top_window.winfo_exists() :
            self.top_window = customtkinter.CTkToplevel()
            self.top_window.title("Calendar")
        self.top_window.grab_set()
        self.calendar = Calendar(self.top_window, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendar.grid(row=0, column=0, padx=10)
        self.open_button = tk.Button(self.top_window, text="Open Date", command=self.diary_open_data)
        self.open_button.grid(row=1, column=0, padx=10, pady=10)
        self.error_label = customtkinter.CTkLabel(self.top_window, text="", text_color="red")
        self.error_label.grid(row=2, column=0, padx=1, pady=10)

    # Megubah data pada hari itu
    def diary_open_data(self):
        selected_date = self.calendar.selection_get().strftime('%d-%m-%Y')
        if(Date(selected_date) > Date(self.date)): # Tanggal yang dipilih tidak valid (lebih dari tanggal hari ini)
            self.error_label.configure(text="Date not valid")
        else:
            self.curr_date = selected_date
            self.diary_date_label.configure(text="Date : " + self.curr_date)
            self.diary_textbox.delete("0.0","end")
            if (self.diary_controller.isInRecord(self.curr_date)) :
                _, content = self.diary_controller.readRecord(self.curr_date)
                self.diary_textbox.insert("0.0",content)
        
            self.top_window.destroy()

    # Menyimpan record yang telah diubah oleh pengguna di frame ke file data
    def diary_save_button_event(self):
        if(self.diary_controller.isInRecord(self.curr_date)) :
            if (self.diary_textbox.get("0.0", "end").strip() != "") :
                self.diary_controller.updateRecord(self.curr_date, self.diary_textbox.get("0.0", "end"))
            else :
                self.diary_controller.deleteRecord(self.curr_date)
        elif (self.diary_textbox.get("0.0", "end").strip() != "") :
            self.diary_controller.createRecord(self.curr_date, self.diary_textbox.get("0.0", "end"))