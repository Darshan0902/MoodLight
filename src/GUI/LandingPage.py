# File : LandingPage.py 
# Berisi kelas boundary LandingPage, yang bertanggung jawab untuk
# Mengatur hubungan antara kelas DiaryModificationPage, MoodModificationPage, QuotesModificationPage, SleepTrackerPage dengan pengguna luar 

import os
from customtkinter import *
from PIL import Image
import random
from GUI.MoodModificationPage import MoodModificationPage
from GUI.SleepTrackerPage import SleepTrackerPage
from GUI.DiaryModificationPage import DiaryModificationPage
from GUI.QuotesModificationPage import QuotesModificationPage
from Quote.QuoteModificationController import QuoteModificationController

set_widget_scaling(0.85)

class LandingPage(CTk):

    MAX_TEXT_LENGTH = 50
    # CONSTRUCTOR
    # Menginisialisasi seluruh frame dan fungsionalitas dari LandingPage
    def __init__(self):
        super().__init__()

        # Menginisiasi pembuatan window
        self.title("MoodLight")
        self.geometry("1344x648")

        # Membuat Konfigurasi Grid Layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Membuat konfigurasi gambar
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "img")
        self.logo_image = CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(150,30))
        self.large_logo_image = CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(900,180))
        self.home_image = CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(40,40))
        self.mood_image = CTkImage(Image.open(os.path.join(image_path, "mood.png")), size=(40,40))
        self.sleep_image = CTkImage(Image.open(os.path.join(image_path, "sleep.png")), size=(40,40))
        self.diary_image = CTkImage(Image.open(os.path.join(image_path, "diary.png")), size=(40,40))
        self.quotes_image = CTkImage(Image.open(os.path.join(image_path, "quotes.png")), size=(40,40))

        # Membuat frame navigasi 
        self.navigation_frame = CTkFrame(self, corner_radius=0, fg_color="#305f72")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.logo_image_label = CTkLabel(self.navigation_frame, text="", image=self.logo_image)
        self.logo_image_label.grid(row=0, column=0, padx=(20,19), pady=(20,20))

        self.home_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", font=CTkFont(size=20,weight="bold"),
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew", pady=20)

        self.mood_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Mood", font=CTkFont(size=20,weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.mood_image, anchor="w", command=self.mood_button_event)
        self.mood_button.grid(row=2, column=0, sticky="ew", pady=20)

        self.sleep_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Sleep", font=CTkFont(size=20,weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.sleep_image, anchor="w", command=self.sleep_button_event)
        self.sleep_button.grid(row=3, column=0, sticky="ew", pady=20)

        self.diary_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Diary", font=CTkFont(size=20,weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.diary_image, anchor="w", command=self.diary_button_event)
        self.diary_button.grid(row=4, column=0, sticky="ew", pady=20)

        self.quotes_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Quotes", font=CTkFont(size=20,weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.quotes_image, anchor="w", command=self.quotes_button_event)
        self.quotes_button.grid(row=5, column=0, sticky="ew", pady=20)

        # Membuat home frame
        self.home_frame = CTkFrame(self, corner_radius=0, fg_color="#568ea6")
        self.home_frame.grid_columnconfigure(6, weight=1)

        self.home_frame_large_logo_label = CTkLabel(self.home_frame, text="", image=self.large_logo_image)
        self.home_frame_large_logo_label.grid(row=0, column=0, padx=250, pady=(150, 60))

        self.home_quote_label = CTkLabel(self.home_frame, width=300, font=CTkFont(size=30,weight="bold"), text_color="white", padx=30, pady=30)
        self.home_quote_label.grid(row=1, column=0, padx=100, pady=50)

        # Membuat mood frame
        self.mood_frame = None
        self.sleep_frame = None
        self.diary_frame = None
        self.quotes_frame = None

        # Menetapkan default value
        set_appearance_mode("Light")
        self.select_frame("home")

    # EVENT ACTION
    # Memilih frame mana yang akan ditampilkan ketika button pada navigation frame di tekan 
    def select_frame(self, name):
        # Menetapkan warna button ketika di tekan
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.mood_button.configure(fg_color=("gray75", "gray25") if name == "mood" else "transparent")
        self.sleep_button.configure(fg_color=("gray75", "gray25") if name == "sleep" else "transparent")
        self.diary_button.configure(fg_color=("gray75", "gray25") if name == "diary" else "transparent")
        self.quotes_button.configure(fg_color=("gray75", "gray25") if name == "quotes" else "transparent")

        # Menampilkan frame yang dipilih
        if name == "home":
            self.show_random_quote()
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "mood":
            if self.mood_frame == None:
                self.mood_frame = MoodModificationPage(self).get_frame()
            self.mood_frame.grid(row=0, column=1, sticky="nsew")
        else:
            if self.mood_frame != None:
                self.mood_frame.grid_forget()

        if name == "sleep":
            if self.sleep_frame == None:
                self.sleep_frame = SleepTrackerPage(self).get_frame()
            self.sleep_frame.grid(row=0, column=1, sticky="nsew")
        else:
            if self.sleep_frame != None:
                self.sleep_frame.grid_forget()

        if name == "diary":
            if self.diary_frame == None:
                self.diary_frame = DiaryModificationPage(self).get_frame()
            self.diary_frame.grid(row=0, column=1, sticky="nsew")
        else:
            if self.diary_frame != None:
                self.diary_frame.grid_forget()

        if name == "quotes":
            if self.quotes_frame == None:
                self.quotes_frame = QuotesModificationPage(self).get_frame()
            self.quotes_frame.grid(row=0, column=1, sticky="nsew")
        else:
            if self.quotes_frame != None:
                self.quotes_frame.grid_forget()

    # Memilih frame home
    def home_button_event(self):
        self.select_frame("home")

    # Memilih frame mood
    def mood_button_event(self):
        self.select_frame("mood")

    # Memilih frame sleep
    def sleep_button_event(self):
        self.select_frame("sleep")

    # Memilih frame diary
    def diary_button_event(self):
        self.select_frame("diary")

    # Memilih frame quotes
    def quotes_button_event(self):
        self.select_frame("quotes")
    
    # Memilih quotes acak
    def show_random_quote(self) :
        quote_controller = QuoteModificationController()
        i = random.randint(1,len(quote_controller.data))
        _, author, content = quote_controller.readRecord(i)
        quoteText = str(content + " ~ " + author)
        if (len(quoteText) > LandingPage.MAX_TEXT_LENGTH) :
            words = quoteText.split(" ")
            charCount = 0
            quoteText = ""
            for w in words :
                if (w == "~") :
                    w = "\n~ "
                    charCount = 0
                elif (charCount + len(w) >= LandingPage.MAX_TEXT_LENGTH) :
                    w += "\n"
                    charCount = 0
                else :
                    charCount += len(w)
                    w += " "
                quoteText += w
        self.home_quote_label.configure(text=quoteText)