import customtkinter as ctk
import os
from PIL import Image

info_dict = {
    "Language Pack": "V108011",
    "Hardware version": "V70146",
    "Software version": "SU1DBSV15.8.9-12.7",
    "Firmware version": "V230620",
    "Date version": "V1039",
    "Build time": "Mar 27 2024",
    "Rfid version": "RF0115"
}

def create_software_frame(parent, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    frame.pack(fill="both", expand=True)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    create_software_title_frame(frame, "Software", controller)
    create_software_info_frame(frame)

    return frame


def create_software_title_frame(parent, title, command):
    frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="new")

    label = ctk.CTkLabel(frame, text=title, fg_color="#A83232", corner_radius=0,
                         anchor='center', text_color="white", font=("Arial", 20, 'bold'))
    label.grid(row=0, column=0, pady=5, padx=10, sticky="new")

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "images", "close_icon.png")
        image = ctk.CTkImage(light_image=Image.open(image_path))

        close_button = ctk.CTkButton(frame, text="", image=image, command=command,
                                     hover_color="#A83232", fg_color="#A83232",
                                     width=50, height=20, corner_radius=0)
        close_button.grid(row=0, column=0, sticky="e", padx=30)

    except FileNotFoundError:
        print(f"Image not found: {image_path}")
    except Exception as e:
        print(f"Error loading image: {e}")


def create_software_info_frame(parent):
    frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=0)
    frame.grid(row=1, column=0, pady=70, padx=30, sticky="news")
    frame.columnconfigure((0, 1), weight=1)

    for i, (key, value) in enumerate(info_dict.items()):
        ctk.CTkLabel(frame, text=f"{key}:", text_color="#A83232", anchor='center',
                     font=("Arial", 20)).grid(row=i, column=0, padx=100, pady=25, sticky="w")
        ctk.CTkLabel(frame, text=value, text_color="#A83232", font=("Arial", 20)).grid(
            row=i, column=1, padx=0, pady=25, sticky="w")

    check_button = ctk.CTkButton(frame, text="Check", text_color="#A83232",
                                 fg_color="#C4E3ED", font=("Arial", 20), corner_radius=0)
    check_button.grid(row=len(info_dict), column=0, pady=(30,0), sticky="ws")

    reboot_button = ctk.CTkButton(frame, text="Reboot", text_color="#A83232",
                                  fg_color="#C4E3ED", font=("Arial", 20), corner_radius=0)
    reboot_button.grid(row=len(info_dict), column=0, columnspan=2, padx=500, pady=(30,0), sticky="ws")

