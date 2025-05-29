import customtkinter as ctk
from PIL import Image
import os

def create_permission_settings(parent, title, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    create_title_frame(frame, title, controller)
    create_checkboxes(frame)

    return frame

def create_title_frame(parent, title, close_command):
    frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    frame.grid(row=0, column=0, sticky="ew")
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=0)

    # Title Label
    title_label = ctk.CTkLabel(
            frame,text=title,fg_color="#A83232",
            anchor="center",text_color="white",font=("Arial", 20, "bold")
        )
    title_label.grid(row=0, column=0, pady=5, padx=0, sticky="new")

    # Load close icon
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "images", "close_icon.png")

        close_image = ctk.CTkImage(dark_image=Image.open(image_path), size=(20, 20))
        close_button = ctk.CTkButton(frame, text="", image=close_image,
            command=close_command, hover_color="#A83232", fg_color="#A83232",
            width=40, height=20, corner_radius=0)
        
        close_button.grid(row=0, column=0, padx=(0, 50), sticky="e")
        
    except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred loading close button: {e}")

def create_checkboxes(parent):
    checkbox_labels = [
        "User : User1",
        "Edit",
        "Print",
        "Setting",
        "Print set",
        "File manage",
        "Load"
    ]

    frame = ctk.CTkFrame(parent, fg_color="white")
    frame.grid(row=1, column=0, pady=20, padx=50, sticky="nsew")
    frame.columnconfigure(0, weight=1)

    for i, label_text in enumerate(checkbox_labels):
        if i == 0:
            label = ctk.CTkLabel(frame, text=label_text, text_color="#A83232",
                                 font=("Arial", 20))
            label.grid(row=i, column=0, pady=(10, 20), sticky="w")
        else:
            checkbox = ctk.CTkCheckBox(frame, text=label_text, font=("Arial", 20),
                                       corner_radius=0, checkbox_width=40, checkbox_height=40,
                                       border_width=1, border_color="#A83232", checkmark_color="#A83232")
            checkbox.grid(row=i, column=0, pady=20, padx=20, sticky="w")
