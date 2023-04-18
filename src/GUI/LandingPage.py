import os
import customtkinter
from PIL import Image
from GUI.MoodModificationPage import MoodModificationPage
from GUI.SleepTrackerPage import SleepTrackerPage
from GUI.DiaryModificationPage import DiaryModificationPage
from GUI.QuotesModificationPage import QuotesModificationPage

class LandingPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MoodLight")
        self.geometry("700x450")

        # Set Grid Layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Load Images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(150,30))
        self.large_logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(450,90))
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(26,26))
        self.mood_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "mood.png")), size=(26,26))
        self.sleep_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "sleep.png")), size=(26,26))
        self.diary_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "diary.png")), size=(26,26))
        self.quotes_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "quotes.png")), size=(26,26))

        # Create Navigation Frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.logo_image_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image)
        self.logo_image_label.grid(row=0, column=0, padx=0, pady=(20,20))

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew", pady=10)

        self.mood_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Mood",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.mood_image, anchor="w", command=self.mood_button_event)
        self.mood_button.grid(row=2, column=0, sticky="ew", pady=10)

        self.sleep_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Sleep",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.sleep_image, anchor="w", command=self.sleep_button_event)
        self.sleep_button.grid(row=3, column=0, sticky="ew", pady=10)

        self.diary_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Diary",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.diary_image, anchor="w", command=self.diary_button_event)
        self.diary_button.grid(row=4, column=0, sticky="ew", pady=10)

        self.quotes_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Quotes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.quotes_image, anchor="w", command=self.quotes_button_event)
        self.quotes_button.grid(row=5, column=0, sticky="ew", pady=10)

        # Create Home Frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(6, weight=1)

        self.home_frame_large_logo_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_logo_image)
        self.home_frame_large_logo_label.grid(row=0, column=0, padx=450, pady=100)

        self.home_textbox = customtkinter.CTkTextbox(self.home_frame, width=750)
        self.home_textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 1)
        self.home_textbox.grid(row=1, column=0, padx=100, pady=50)

        # create mood frame
        self.mood_frame = None
        self.sleep_frame = None
        self.diary_frame = None
        self.quotes_frame = None

        # Set default values
        customtkinter.set_appearance_mode("Light")
        self.select_frame("home")
        
    def select_frame(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.mood_button.configure(fg_color=("gray75", "gray25") if name == "mood" else "transparent")
        self.sleep_button.configure(fg_color=("gray75", "gray25") if name == "sleep" else "transparent")
        self.diary_button.configure(fg_color=("gray75", "gray25") if name == "diary" else "transparent")
        self.quotes_button.configure(fg_color=("gray75", "gray25") if name == "quotes" else "transparent")

        # show selected frame
        if name == "home":
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

    def home_button_event(self):
        self.select_frame("home")

    def mood_button_event(self):
        self.select_frame("mood")

    def sleep_button_event(self):
        self.select_frame("sleep")

    def diary_button_event(self):
        self.select_frame("diary")

    def quotes_button_event(self):
        self.select_frame("quotes")