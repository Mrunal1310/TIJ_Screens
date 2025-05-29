import customtkinter as ctk
from PIL import Image
import os

class DateBaseScreen(ctk.CTkFrame):
    def __init__(self, parent, title, button_list, rows, columns, close_button_command=None):
        super().__init__(parent)
        self.parent = parent
        # self.controller = controller
        
        self.configure(fg_color = 'white')
        self.pack(fill="both", expand=True)

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        # Initialize UI components
        self.create_title_frame(title, close_button_command)
        self.button_frame(rows, columns)
        
        self.button_list = button_list
        self.create_buttons(button_list, columns)
        
        if button_list:
            self.create_buttons(button_list, columns)

    def create_title_frame(self, title, command):
        self.title_frame = ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.grid(row=0, column=0, sticky="new")

        # Title label (Corrected bg_color)
        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text=title,
            bg_color="#A83232",  # Changed from fg_color to bg_color
            anchor="center",
            text_color="white",
            font=("Arial", 20, "bold")
        )
        self.title_label.grid(row=0, column=0, pady=5, padx=0, sticky="new")

        # Load close button icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = "images/"
        image_path = os.path.join(script_dir, image_dir, "close_icon.png")

        try:
            image = ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button = ctk.CTkButton(
                self.title_frame,
                text="", image=image,
                command=command,
                hover_color="#A83232",
                fg_color="#A83232",
            )
            self.close_button.grid(row=0, column=0, padx=10, pady=5, sticky="e")  # Fixed position
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def button_frame(self, rows, columns):
        self.frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.frame.columnconfigure(tuple(range(columns)), weight=1)
        self.frame.rowconfigure(tuple(range(rows)), weight=1)
        self.frame.grid(row=1, column=0, pady=(50,0),sticky="news")

    def create_buttons(self, button_list, columns, command=None):
        # Function after clicking button
        def clicked_button(button_text):
            print(f"Button clicked: {button_text}")

        for (index, label) in enumerate(button_list):
            row = index // columns
            col = index % columns
            
            button = ctk.CTkButton(
                self.frame,
                text=label,
                command=command,
                corner_radius=0,
                fg_color='#FF00FF',
                text_color="black",
                font=("Arial", 15,)
            )
            # fg_color = "#C4E3ED" if label == "Term" and 'Handwriting' in label else "#FF00FF"
            if label == "Term":
                button.configure(fg_color="#C4E3ED", command = lambda: self.parent.show_frame("term"))
                
            elif label == 'Handwriting':
                button.configure(fg_color='#C4E3ED', command = lambda: self.parent.show_frame("handwriting"))
            else:
                button.configure(command = lambda t=label: print(f"Button clicked: {t}"))

            button.grid(row=row, column=col, padx=40, sticky="ew")
