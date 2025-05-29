import customtkinter as ctk
from PIL import Image
import os
from popup_box import open_popup_box

def create_symbol_screen(parent, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    frame.pack(fill="both", expand=True)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    create_title_frame(frame, controller)  # Pass root to create_title_frame
    create_button_frame(frame)  # Pass root to create_button_frame

    return frame

def create_title_frame(parent, command):
    title_frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    title_frame.columnconfigure(0, weight=1)
    title_frame.grid(row=0, column=0, sticky="new")

    label = ctk.CTkLabel(
        title_frame,
        text="Symbols",
        fg_color="#A83232",
        corner_radius=0,
        anchor="center",
        text_color="white",
        font=("Arial", 20, "bold"),
    )
    label.grid(row=0, column=0, sticky="new")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = "images\\"

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
                close_button.grid(row=0, column=0, sticky="e", padx=60)
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
                    command=lambda: print("Button clicked"),  # Use lambda to avoid immediate execution
                )
                check_button.grid(row=0, column=0, sticky="e", padx=(50, 130))

        except FileNotFoundError:
            print(f"Error: Image not found - {image_name}")
        except Exception as e:
            print(f"An error occurred: {e}")

def create_button_frame(parent):
    button_frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=0)
    button_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    button_frame.rowconfigure((0, 1), weight=1)
    button_frame.grid(row=1, column=0, pady=20, sticky="news")

    image_files = [f"Symbol_{i}_icon.png" for i in range(1, 15)]

    create_buttons(parent, button_frame, image_files)  # Pass root, button_frame, and image_files

def create_buttons(parent, button_frame, image_files):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = "images\\"

    for index, image_name in enumerate(image_files):
        row = index // 7
        col = index % 7

        image_path = os.path.join(image_dir, image_name)

        try:
            desired_width, desired_height = 120, 180
            image = ctk.CTkImage(dark_image=Image.open(image_path), size=(desired_width, desired_height))

            button = ctk.CTkButton(
                button_frame,
                text="",
                image=image,
                corner_radius=0,
                fg_color="white",
                hover_color="lightblue",
                command=lambda: print("Button clicked"), # Use lambda to avoid immediate execution
            )
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nswe")

        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    size_button = ctk.CTkButton(
        button_frame,
        command=lambda: open_popup_box("Size"),  # Pass root to open_popup_box
        text="Size",
        corner_radius=0,
        fg_color="#C4E3ED",
        text_color="black",
        font=("Arial", 20),
    )
    size_button.grid(row=2, column=0, columnspan=7, padx=0, pady=20, sticky="e")

# if __name__ == "__main__":
#     symbol_window()