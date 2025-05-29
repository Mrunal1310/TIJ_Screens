import customtkinter as ctk
from PIL import Image
import os

from popup_box import open_popup_box


def create_qr_screen(parent, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    frame.pack(fill="both", expand=True)
    
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)
    
    create_title_frame(frame, controller)
    create_button_frame(frame)
    
    return frame

# Title bar with label, close and check icons

def create_title_frame(parent, command):
    frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="new")

    label = ctk.CTkLabel(frame, text='Select code', fg_color="#A83232", corner_radius=0,
                         anchor='center', text_color="white", font=("Arial", 20, 'bold'))
    label.grid(row=0, column=0, pady=5, padx=10, sticky="new")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, "images")
    image_list = ["close_icon.png", "check_icon.png"]

    for image_name in image_list:
        try:
            image_path = os.path.join(image_dir, image_name)
            image = ctk.CTkImage(dark_image=Image.open(image_path))

            if image_name == "close_icon.png":
                close_button = ctk.CTkButton(frame, text="", image=image,
                    command=command, hover_color="#A83232", fg_color="#A83232",
                    width=50, height=20, corner_radius=0)
                close_button.grid(row=0, column=0, sticky="e", padx=60)

            elif image_name == "check_icon.png":
                check_button = ctk.CTkButton(frame, text="", image=image,
                    hover_color="#A83232", fg_color="#A83232",
                    width=50, height=20, corner_radius=0,
                    command=lambda: print("Button clicked"))
                check_button.grid(row=0, column=0, sticky="e", padx=(50, 130))

        except FileNotFoundError:
            print(f"Error: Image not found - {image_name}")
        except Exception as e:
            print(f"An error occurred: {e}")

def create_button_frame(parent):
    frame = ctk.CTkFrame(parent, fg_color='white')
    frame.columnconfigure((0, 1, 2), weight=1)
    frame.rowconfigure(0, weight=1)
    frame.grid(row=1, column=0, pady=10, sticky='news')

    code_option = ctk.CTkComboBox(frame, 
                                    values = ['UPCA', 'UPCE', 'EAN2/5/8/13', 'EAN14',
                                            'INT25','CODE39', 'CODE128', 'EAN128', 
                                            'PDF417', 'DATAMATRIX', 'QR', 'HANXIN'],
                                    command=lambda x: print(f"Option selected: {x}"), corner_radius=0,fg_color="white",
            height=30,
            width=30,
            text_color="black",
            font=("Arial", 20),
            border_color="black",
            border_width=1)
    code_option.grid(row=0, column=0, padx=10,pady=10, sticky='ews')
    
    code_option = ctk.CTkComboBox(frame, 
                                    values = ['Nothing', 'Small', 'Medium', 'Large'],
                                    command=lambda x: print(f"Option selected: {x}"), corner_radius=0,
            fg_color="white",
            height=30,
            width=30,
            text_color="black",
            font=("Arial", 20),
            border_color="black",
            border_width=1)
    code_option.grid(row=0, column=1, padx=10,pady=50, sticky='ews')
    size_button= ctk.CTkButton(frame, text='Size: ',text_color='black',fg_color='white',anchor='w', border_width=1, corner_radius=0,font=("Arial", 20), command=lambda: open_popup_box('Size'))
    size_button.grid(row=0, column=1,padx=10, pady=10, sticky='ews')
    code_option = ctk.CTkComboBox(frame,
                                    values = ['Nothing', 'Box-1', 'Box-2', 'Box-3', 'Bind-1', 'Bind-2', 'Bind-3','Bind-4'],
                                    command=lambda x: print(f"Option selected: {x}"),corner_radius=0,
            fg_color="white",
            height=30,
            width=30,
            text_color="black",
            font=("Arial", 20),
            border_color="black",
            border_width=1)
    code_option.grid(row=0, column=2, padx=10,pady=50, sticky='ews')
    size_button= ctk.CTkButton(frame, text='Transverse stretch: ',text_color='black',fg_color='white',anchor='w',border_width=1,corner_radius=0,font=("Arial", 20), command=lambda: open_popup_box('Size'))
    size_button.grid(row=0, column=2,padx=10, pady=10, sticky='ews')

    check_box = ctk.CTkCheckBox(frame, text="GS1", font=('Arial', 20),corner_radius=5, height=50, width=50, border_width=1)
    check_box.grid(row=0, column=4,padx=10, pady=10, sticky='ews')