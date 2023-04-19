# File : DiaryModificationPage.py 
# Berisi kelas boundary DiaryModificationPage, yang bertanggung jawab untuk
# Mengatur hubungan antara kelas controller DiaryModificationController dengan pengguna luar 

import customtkinter
import os
import tkinter as tk
from PIL import Image
from tkcalendar import Calendar, DateEntry

class DiaryModificationPage(customtkinter.CTk):

    # CONSTRUCTOR
    # Menginisialisasi seluruh frame dan fungsionalitas dari DiaryModificationPage
    def __init__(self, master):
        # Menetapkan master dari DiaryModificationPage yaitu master
        self.master = master

        # Menciptakan frame pertama tempat mengubah data diary
        self.diary_modif_frame = customtkinter.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.diary_modif_frame.grid_columnconfigure(1, weight=1)
        
        diary_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "images")
        self.diary_logo_image = customtkinter.CTkImage(Image.open(os.path.join(diary_image_path, "logo.png")), size=(150,30))
        self.diary_logo_image_label = customtkinter.CTkLabel(self.diary_modif_frame, text="", image=self.diary_logo_image)
        self.diary_logo_image_label.grid(row=0, column=1, padx=(0,50), pady=(10,0), sticky="ne")
        
        self.diary_date_label = customtkinter.CTkLabel(self.diary_modif_frame, text="")
        self.diary_date_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        self.diary_textbox = customtkinter.CTkTextbox(self.diary_modif_frame, width=750, height=500, border_width=2)
        self.diary_textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.diary_textbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.diary_entry = customtkinter.CTkButton(self.diary_modif_frame, text= "Previous Entry", command=self.diary_open_calendar)
        self.diary_entry.grid(row=8, column=0, padx=(400,0), pady=10)
        
        self.diary_save = customtkinter.CTkButton(self.diary_modif_frame, text="Save", command=self.diary_save_button_event)
        self.diary_save.grid(row=8, column=1, padx=100, pady=10)

    # GETTER
    # Mengembalikan frame pertama dan utama dari DiaryModificationPage
    def get_frame(self):
        return self.diary_modif_frame
    
    # EVENT ACTION
    # Membuka kalendar untuk melihat data pada hari itu
    def diary_open_calendar(self):
        self.calendar = Calendar(self, selectmode='day', date_pattern='dd-mm-yyyy')
        self.calendar.grid(row=9, column=0, padx=10)
        self.open_button = tk.Button(self, text="Open Date", command=self.diary_open_data)
        self.open_button.grid(row=10, column=0, padx=10, pady=10)

    # Megubah data pada hari itu
    def diary_open_data(self):
        selected_date = self.calendar.selection_get().strftime('%d-%m-%Y')
        # print(f"Membuka data untuk tanggal {selected_date}")

    # Menyimpan record yang telah diubah oleh pengguna di frame ke file data
    def diary_save_button_event(self):
        print("Save")