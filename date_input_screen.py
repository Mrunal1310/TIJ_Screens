import customtkinter as ctk
from PIL import Image
import os


def create_title_frame(parent_frame, close_command, open_sub_screen):
    title_frame = ctk.CTkFrame(parent_frame, fg_color="#A83232", corner_radius=0)
    title_frame.grid(row=0, column=0, sticky="new")
    title_frame.grid_columnconfigure(0, weight=1)

    label = ctk.CTkLabel(
        title_frame,
        text="Date input",
        fg_color="#A83232",
        corner_radius=0,
        anchor="center",
        text_color="white",
        font=("Arial", 20, "bold"),
    )
    label.grid(row=0, column=0, sticky="nsew")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = "images"
    image_list = ["close_icon.png", "term_icon.png"]

    for image_name in image_list:
        try:
            image_path = os.path.join(script_dir, image_dir, image_name)
            image = ctk.CTkImage(dark_image=Image.open(image_path), size=(20, 20))

            if image_name == "close_icon.png":
                close_button = ctk.CTkButton(
                    title_frame,
                    text="",
                    image=image,
                    command=close_command,
                    fg_color="#A83232",
                    width=30,
                    height=30,
                    corner_radius=0,
                )
                close_button.grid(row=0, column=0, sticky="e", padx=60)

            elif image_name == "term_icon.png":
                term_button = ctk.CTkButton(
                    title_frame,
                    text="Term",
                    image=image,
                    anchor='w',
                    fg_color="#A83232",
                    text_color="white",
                    font=("Arial", 20, "bold"),
                    hover=True,
                    corner_radius=0,
                    command=lambda:open_sub_screen('term')
                )
                term_button.grid(row=0, column=0, sticky="w", padx=10)

        except FileNotFoundError:
            print(f"Error: Image not found - {image_name}")
        except Exception as e:
            print(f"An error occurred: {e}")

    return title_frame


def create_button_frame(parent_frame):
    button_frame = ctk.CTkFrame(parent_frame, fg_color="white", corner_radius=0)
    button_frame.grid(row=1, column=0, pady=50, sticky="news")
    button_frame.grid_columnconfigure((0, 1, 2), weight=1)

    button_list = [
        '(2025)Year', '(25)Year', '(03)Month',
        '(10)Day', '(069)Day<001~365>', '(14)Hour',
        '(35)Minutes', '(20)Second', '(MAR)Code:Month',
        '(O)Code:Hour', '(MON)Code:Week', '(J)Code:Day',
    ]

    for index, text in enumerate(button_list):
        row = index // 3
        col = index % 3
        button = ctk.CTkButton(
            button_frame,
            text=text,
            corner_radius=0,
            fg_color='#FF00FF',
            text_color="black",
            font=("Arial", 15),
            command=lambda t=text: print(f"Button clicked: {t}"),
        )
        button.grid(row=row, column=col, padx=30, pady=50, sticky="ew")

    return button_frame


def create_bottom_buttons(parent_frame, show_frame_callback):
    bottom_frame = ctk.CTkFrame(parent_frame, fg_color='white', corner_radius=0)
    bottom_frame.grid(row=2, column=0, pady=20, sticky='ew')
    bottom_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    labels = ["Month", "Hour", "Week", "Day"]
    for i, label in enumerate(labels):
        button = ctk.CTkButton(
            bottom_frame,
            text=f'Code set({label})',
            command=lambda l=label.lower(): show_frame_callback(f'code_set_{l}'),
            corner_radius=0,
            fg_color='#B7410E',
            font=('Arial', 15),
            text_color='white'
        )
        button.grid(row=0, column=i, padx=20, pady=5, sticky="ew")

    return bottom_frame


def create_date_input_screen(parent, controller, close_command):
    frame = ctk.CTkFrame(parent, fg_color="white")

    frame.grid_rowconfigure(0, weight=0)  # title
    frame.grid_rowconfigure(1, weight=1)  # button
    frame.grid_rowconfigure(2, weight=0)  # bottom
    frame.grid_columnconfigure(0, weight=1)

    create_title_frame(frame, close_command, controller.show_frame)
    create_button_frame(frame)
    create_bottom_buttons(frame, controller.show_frame)

    return frame
