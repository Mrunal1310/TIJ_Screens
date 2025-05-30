import customtkinter as ctk
from PIL import Image
import os

from warning_popup import open_warning


class FileScreen(ctk.CTkFrame):
    def __init__(self, parent, go_home_callback):
        super().__init__(parent)
        
        self.configure(fg_color="white")
        self.go_home_callback = go_home_callback
        
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0), weight=0)
        self.rowconfigure((1), weight=1)
        
        self.title_frame()
        self.button_frame()
        self.display_frame()
        
    def title_frame(self):
        self.frame=ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, columnspan=2, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="File list",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0,)
        
        try:
            image_path = os.path.join(os.path.dirname(__file__), "images", "multiple_choice_icon.png")
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.multiple_button=ctk.CTkButton(self.frame, text="Multiple Choice", image=image, fg_color="#A83232", corner_radius=0, anchor='w',text_color="white",font=("Arial", 20, 'bold'))
            self.multiple_button.grid(row=0, column=0, pady=5, padx=5, sticky="w")
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        try:
            image_path = os.path.join(os.path.dirname(__file__), "images", "close_icon.png")
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.go_home_callback, hover=False, fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
            
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def button_frame(self):
        
        self.frame=ctk.CTkFrame(self, fg_color="white",border_width=2, corner_radius=0,)
        self.frame.columnconfigure((0), weight=1)
        self.frame.rowconfigure((0,1,), weight=0)
        self.frame.grid(row=1, column=0,pady=10,padx=10, sticky="news")
        
        self.button_list=["Test file" ]
        
        for index, text in enumerate(self.button_list):
            button = ctk.CTkButton(self.frame, text=text, text_color="black", anchor="w", command=lambda t=text: self.system_button(t),
                                    fg_color="white", hover_color="#FF00FF", font=("Arial", 20,), corner_radius=0)
            button.grid(row=index + 1, column=0, padx=10, pady=5, sticky="news")
        
        
    def display_frame(self):
        
        self.frame=ctk.CTkFrame(self, fg_color="white",corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0,1,), weight=1)
        self.frame.grid(row=1, column=1, padx=5,pady=10, sticky="news")
        
        self.entry=ctk.CTkEntry(self.frame, placeholder_text="",height=40, corner_radius=10, border_width=1, border_color="black", ) 
        self.entry.grid(row=0, column=0,padx=5, pady=(30, 0), sticky='ew')
        
        self.format_butn=ctk.CTkButton(self.frame, text="Delete", text_color="white",fg_color="#A83232",font=("Arial", 22,), corner_radius=0, command=lambda: open_warning())
        self.format_butn.grid(row=1, column=0, padx=10, pady=50, sticky="es")
        
        self.open_butn=ctk.CTkButton(self.frame, text="Open",  text_color="white",fg_color="#A83232", font=("Arial", 22,), corner_radius=0,)
        self.open_butn.grid(row=1, column=0, padx=10,pady=10,sticky="es")
        
        self.label=ctk.CTkLabel(self.frame, text="", font=('Arial', 18), anchor='nw',text_color="black", height=150,fg_color="#C4E3ED")
        self.label.grid(row=0, column=0,padx=5, pady=5, sticky="new")
        
        
    def system_button(self, text):
        if text == "Test file":
            self.label.configure(text="Test file\n26.9KB\nFile\n2023-07-27 12:00:00")
        