import customtkinter as ctk
from PIL import Image
import os

from popup_box import open_popup_box


# Class of Calendar Window
class CalendarWindow(ctk.CTkFrame):
    def __init__(self, parent,title, button_list,rows, close_button_command=None):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="white")
        self.pack(fill="both", expand=True)

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        # Create UI
        self.create_title_frame(title, close_button_command)
        self.create_button_frame(rows)
        
        self.button_list=button_list
        self.create_buttons(button_list)

    def create_title_frame(self, title, command):
        self.title_frame = ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.grid(row=0, column=0, sticky="new")

        self.label = ctk.CTkLabel(
            self.title_frame,
            text=title,
            fg_color="#A83232",
            text_color="white",
            anchor='center',
            font=("Arial", 20, 'bold')
        )
        self.label.grid(row=0, column=0, pady=5, sticky="new")

        # Load close icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "images", "close_icon.png")

        try:
            image = ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button = ctk.CTkButton(
                self.title_frame,
                text="",
                image=image,
                command=command,
                hover_color="#A83232",
                fg_color="#A83232",
                width=50,
                height=30,
                corner_radius=0
            )
            self.close_button.grid(row=0, column=0, sticky='e', padx=60)
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_button_frame(self, rows):
        self.button_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.button_frame.columnconfigure((0, 1, 2), weight=1)
        self.button_frame.rowconfigure(tuple(range(rows)), weight=1)
        self.button_frame.grid(row=1, column=0, pady=20, sticky="news")

    def create_buttons(self, button_list):
        
        
        def clicked_button(button_text):
            print(f"Button clicked: {button_text}")
            
        
        for index, label in enumerate(button_list):
            button = ctk.CTkButton(
                self.button_frame,
                text=label,
                corner_radius=0,
                fg_color="#FF00FF",
                text_color="black",
                font=("Arial", 20),
                command=lambda lbl=label: clicked_button(lbl),
            )
            
            if label == '(0)Year':
                button.configure(command=lambda: open_popup_box(" Year"))
            elif label == '(0)Month':
                button.configure(command=lambda: open_popup_box(" Month"))
            elif label == '(0)Day':
                button.configure(command=lambda: open_popup_box(" Day"))
            else:
                command = lambda t=label: print(f"Button clicked: {t}")
            
            
            button.grid(row=index, column=1, padx=40, pady=20, sticky="ew")
            