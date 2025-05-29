import customtkinter as ctk
from PIL import Image
import os

def create_number_screen(parent, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    frame.pack(fill="both", expand=True)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    create_title_frame(frame, controller)
    create_button_frame(frame)

    return frame


def create_title_frame(parent, command):
    title_frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    title_frame.columnconfigure(0, weight=1)
    title_frame.rowconfigure(0, weight=0)
    title_frame.grid(row=0, column=0, sticky="new")

    label = ctk.CTkLabel(
        title_frame,
        text="Number Setting",
        fg_color="#A83232",
        corner_radius=0,
        anchor="center",
        text_color="white",
        font=("Arial", 20, "bold"),
    )
    label.grid(row=0, column=0, sticky="new")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, "images")

    image_list = ["close_icon.png", "check_icon.png"]

    for image_name in image_list:
        try:
            image_path = os.path.join(image_dir, image_name)
            image = ctk.CTkImage(dark_image=Image.open(image_path))

            if image_name == "close_icon.png":
                close_button = ctk.CTkButton(
                    title_frame,
                    text="",
                    image=image,
                    command=command,
                    hover_color="#A83232",
                    fg_color="#A83232",
                    width=50,
                    height=20,
                    corner_radius=0,
                )
                close_button.grid(row=0, column=0, sticky="e", padx=50)
            elif image_name == "check_icon.png":
                check_button = ctk.CTkButton(
                    title_frame,
                    text="",
                    image=image,
                    hover_color="#A83232",
                    fg_color="#A83232",
                    width=50,
                    height=20,
                    corner_radius=0,
                    command=lambda: print("Checked!"),
                )
                check_button.grid(row=0, column=0, sticky="e", padx=(50, 130))

        except FileNotFoundError:
            print(f"Error: Image not found - {image_name}")
        except Exception as e:
            print(f"An error occurred: {e}")


def create_button_frame(parent):
    frame = ctk.CTkFrame(parent, fg_color="white", bg_color="white")
    frame.grid(row=1, column=0, padx=100, pady=50, sticky="news")
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

    option_menus = [
        ("Hex", ["Decimal", "Hexadecimal"]),
        ("Repeat", ["0/1"]),
        ("Bit", [str(i) for i in range(1, 16)]),
        ("Stepping", ["0"]),
        ("Supply", ["Yes", "No"]),
        ("Max value", ["9999"]),
        ("Change", ["Increment", "Reduction"]),
        ("Min value", ["0"]),
        ("Current value", ["0"]),
    ]

    for indx, (label_text, values) in enumerate(option_menus):
        row = indx // 2
        col = indx % 2
        label = ctk.CTkLabel(
            frame,
            text=label_text,
            fg_color="white",
            anchor="w",
            text_color="#A83232",
            font=("Arial", 20)
        )
        label.grid(row=row, column=col, padx=15, pady=30, sticky="nwe")

        option_menu = ctk.CTkComboBox(
            frame,
            values=values,
            corner_radius=0,
            fg_color="white",
            height=30,
            width=30,
            text_color="black",
            font=("Arial", 20),
            border_color="black",
            border_width=1
        )
        option_menu.grid(row=row, column=col, padx=10, pady=20, sticky="swe")
