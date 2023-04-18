import customtkinter
import os
from PIL import Image
from Quotes.QuoteModificationController import QuoteModificationController

class QuotesModificationPage(customtkinter.CTk):
    def __init__(self, master):
        self.master = master
        self.quotes_controller = QuoteModificationController()
        self.quotes_modif_frame = customtkinter.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        quotes_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "images")
        self.quotes_logo_image = customtkinter.CTkImage(Image.open(os.path.join(quotes_image_path, "logo.png")), size=(400,80))
        self.quotes_logo_image_label = customtkinter.CTkLabel(self.quotes_modif_frame, text="", image=self.quotes_logo_image)
        self.quotes_logo_image_label.grid(row=0, column=0, padx=0, pady=0)

        self.quotes_list_frame = customtkinter.CTkScrollableFrame(self.quotes_modif_frame,width=700,height=500,corner_radius=0,fg_color="transparent")
        self.quotes_list_frame.grid(row=1,column=0,padx=400,pady=30)
        self.quotes_textboxes = []
        for i in range(len(self.quotes_controller.data)) :
            self.quotes_textboxes.append(customtkinter.CTkTextbox(self.quotes_list_frame,width=650,height=30))
            self.quotes_textboxes[i].insert("0.0", self.quotes_controller.data[i].getContent() + " ~ " + self.quotes_controller.data[i].getAuthor())
            self.quotes_textboxes[i].grid(row=i,column=0,padx=10,pady=10)
        
        self.quotes_add = customtkinter.CTkButton(self.quotes_modif_frame, text="Add Quotes", command=self.quotes_add_button_event)
        self.quotes_add.grid(row=2, column=0, padx=100, pady=10)
        self.quotes_save = customtkinter.CTkButton(self.quotes_modif_frame, text="Save", command=self.quotes_save_button_event)
        self.quotes_save.grid(row=3, column=0, padx=100, pady=10)

    def quotes_save_button_event(self):
        id = 1
        for txt in (self.quotes_textboxes) :
            text = txt.get("0.0","end").strip()
            if (text != "") : # Jika tidak kosong, simpan sebagai quotes baru
                try :
                    content,author = text.split(" ~ ")
                except :
                    txt.destroy()
                    continue
                self.quotes_controller.createRecord(id,author,content)
                id += 1
            elif(self.quotes_controller.isInRecord(id)) :
                self.quotes_controller.deleteRecord(id)
            txt.destroy()
        self.quotes_textboxes.clear()
        
        for i in range(len(self.quotes_controller.data)) :
            self.quotes_textboxes.append(customtkinter.CTkTextbox(self.quotes_list_frame,width=650,height=30))
            self.quotes_textboxes[i].insert("0.0", self.quotes_controller.data[i].getContent() + " ~ " + self.quotes_controller.data[i].getAuthor())
            self.quotes_textboxes[i].grid(row=i,column=0,padx=10,pady=10)
    
    def quotes_add_button_event(self):
        self.quotes_textboxes.append(customtkinter.CTkTextbox(self.quotes_list_frame,width=650,height=30,))
        self.quotes_textboxes[len(self.quotes_textboxes)-1].grid(row=len(self.quotes_textboxes)-1,column=0,padx=10,pady=10)
    
    def get_frame(self):
        return self.quotes_modif_frame