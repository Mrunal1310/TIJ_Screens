import customtkinter as ctk
from PIL import Image
import os

class InkjetEditor(ctk.CTkFrame):
    def __init__(self, parent, go_home_callback):
        super().__init__(parent)
        
        # self.configure(fg_color="white")
        self.go_home_callback = go_home_callback

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)

        self.font_family = 'Arial'
        self.font_size = 20
        self.font = (self.font_family, self.font_size)

        self.text_frame()
        self.button_frame()

    def text_frame(self):
        self.frame = ctk.CTkFrame(self, fg_color='white', border_width=2)
        self.frame.grid(row=0, column=0, padx=10,pady=10, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.text = ctk.CTkTextbox(self.frame, fg_color='white', font=self.font, text_color='black')
        self.text.grid(row=0, column=0, sticky='nsew')

    def button_frame(self):
        self.button = ctk.CTkFrame(self, fg_color='white')
        self.button.grid(row=0, column=1, sticky='ns')

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(script_dir, "images")

        def load_image(filename, size):
            path = os.path.join(image_dir, filename)
            try:
                return ctk.CTkImage(dark_image=Image.open(path), size=size)
            except FileNotFoundError:
                print(f"Image not found: {path}")
                return None

        # Top button
        image = load_image("minimize_icon.png", (40, 40))
        if image:
            self.multiple_button = ctk.CTkButton(
                self.button, text="", image=image,
                fg_color="#A83232", corner_radius=0,
                text_color="white", font=("Arial", 20, 'bold'),
                command=self.go_home_callback
            )
            self.multiple_button.pack(padx=5, fill='x')

        # Zoom and Delete section
        zoom_frame = ctk.CTkFrame(self.button, fg_color="white", border_width=1, corner_radius=10)
        zoom_frame.pack(fill='x', pady=40, padx=50)

        zoom_image = load_image("text_zoom_icon.png", (40, 40))
        delete_image = load_image("delete_icon.png", (40, 40))

        self.zoom = ctk.CTkButton(zoom_frame, text='100%', text_color='black',
                                  font=('Arial', 18), fg_color='white', image=zoom_image)
        self.zoom.pack(side='top', pady=5)

        self.delete = ctk.CTkButton(zoom_frame, text='Delete', text_color='black',
                                    font=('Arial', 18), fg_color='white', image=delete_image)
        self.delete.pack(side='bottom', pady=5)

        # Arrow controls
        arrow_frame = ctk.CTkFrame(self.button, fg_color="white", border_width=1, corner_radius=10)
        arrow_frame.pack(fill='x', pady=(20, 50), padx=50)

        arrow_up = load_image("arrow_up_icon.png", (50, 50))
        arrow_down = load_image("arrow_down_icon.png", (50, 50))
        arrow_left = load_image("arrow_left_icon.png", (50, 50))
        arrow_right = load_image("arrow_right_icon.png", (50, 50))

        self.up = ctk.CTkButton(arrow_frame, text='', fg_color='white', image=arrow_up)
        self.up.pack(side='top', pady=2)
        self.down = ctk.CTkButton(arrow_frame, text='', fg_color='white', image=arrow_down)
        self.down.pack(side='bottom', pady=2)
        self.left = ctk.CTkButton(arrow_frame, text='', fg_color='white', image=arrow_left)
        self.left.pack(side='left', padx=10)
        self.right = ctk.CTkButton(arrow_frame, text='', fg_color='white', image=arrow_right)
        self.right.pack(side='right', padx=10)

        # Rotation and Font controls
        direction_frame = ctk.CTkFrame(self.button, fg_color="white", corner_radius=10)
        direction_frame.pack(fill='x', pady=5, padx=10)

        clockwise = load_image("clockwise_icon.png", (40, 40))
        anticlockwise = load_image("anticlockwise_icon.png", (40, 40))

        self.clock = ctk.CTkButton(direction_frame, text='', fg_color='#a1e6fa',
                                   border_width=1, image=clockwise)
        self.clock.pack(side='right', pady=2, padx=(0, 60))

        self.anticlock = ctk.CTkButton(direction_frame, text='', fg_color='#a1e6fa',
                                       border_width=1, image=anticlockwise)
        self.anticlock.pack(side='left', pady=2, padx=(60, 0))

        # Font size controls
        font_frame = ctk.CTkFrame(self.button, fg_color="white", corner_radius=10)
        font_frame.pack(fill='x', pady=5, padx=10)

        font_plus = load_image("font_+_icon.png", (40, 40))
        font_minus = load_image("font_-_icon.png", (40, 40))

        self.font_increase = ctk.CTkButton(font_frame, text='', fg_color='#031bab', border_width=1,
                                           image=font_plus, command=self.zoom_in)
        self.font_increase.pack(side='left', pady=20, padx=(60, 0))

        self.font_decrease = ctk.CTkButton(font_frame, text='', fg_color='#031bab', border_width=1,
                                           image=font_minus, command=self.zoom_out)
        self.font_decrease.pack(side='right', pady=0, padx=(0, 60))

        # Checkboxes
        self.lock = ctk.CTkCheckBox(self.button, text='Lock', font=('Arial', 18),
                                    corner_radius=0, border_width=2,
                                    checkbox_width=35, checkbox_height=35)
        self.lock.pack(anchor='w', padx=10, pady=(10, 5))

        self.center = ctk.CTkCheckBox(self.button, text='Center', font=('Arial', 18),
                                      corner_radius=0, border_width=2,
                                      checkbox_width=35, checkbox_height=35)
        self.center.pack(anchor='w', padx=10, pady=(5, 10))

    def zoom_in(self):
        self.font_size += 2
        self.update_font()

    def zoom_out(self):
        if self.font_size > 6:
            self.font_size -= 2
            self.update_font()

    def update_font(self):
        self.font = (self.font_family, self.font_size)
        self.text.configure(font=self.font)

