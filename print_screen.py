# main.py
import customtkinter as ctk
from PIL import Image
from datetime import datetime
import os

class PrintScreen(ctk.CTkFrame):
    def __init__(self, parent, go_home_callback, open_settings_callback):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="#2F98EE")
        
        self.open_settings_callback = open_settings_callback
        self.go_home_callback = go_home_callback
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.title_frame()
        self.update_time()
        self.widget_frame()
        self.text_editor()

    def title_frame(self):
        self.title_label = ctk.CTkLabel(self, text="Test file", text_color='white', bg_color="#2F98EE",
                                        corner_radius=0, font=('Arial', 20))
        self.title_label.grid(row=0, column=0, padx=20, sticky='nw')

        self.date_time = ctk.CTkLabel(self, text="", anchor='ne', text_color="white", bg_color="#2F98EE",
                                      font=('Arial', 20))
        self.date_time.grid(row=0, column=0, padx=10, sticky='ne')

        self.version_label = ctk.CTkLabel(self, text="V15.8.9", text_color='yellow', bg_color="#2F98EE",
                                          font=('Arial', 20))
        self.version_label.grid(row=3, column=0, pady=10, padx=10, sticky='sw')

    def text_editor(self):
        self.text_area = ctk.CTkTextbox(self, text_color="black", width=1000, height=250,
                                        bg_color="#2F98EE", font=('Arial', 20), corner_radius=20)
        self.text_area.grid(row=1, column=0, padx=(20, 10), pady=10, sticky='nw')
        self.create_widget_button_()

    def create_widget_button_(self):
        self.create_button('previous_icon.png', 'Previous', 90, "green", 1, 30)
        self.create_button('play_icon.png', 'Next', 90, "blue", 1, (150, 10))
        self.create_button('print_exit_icon.png', 'Exit', 170, "#FFC300", 2, (10, 10), command= self.go_home_callback)

    def create_button(self, image_name, text, height, fg_color, row, pady, command=None):
        image_path = os.path.join("images", image_name)
        try:
            image = ctk.CTkImage(dark_image=Image.open(image_path), size=(30, 30))
            button = ctk.CTkButton(self, text=text, image=image, compound='top', command=command,
                                   height=height, hover=False, fg_color=fg_color, bg_color="#2F98EE",
                                   font=('Arial', 20), corner_radius=20)
            button.grid(row=row, column=0, padx=(0, 20), pady=pady, sticky='ne')
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_time(self):
        current_time = datetime.now().strftime("%Y/%m/%d  %H:%M:%S")
        self.date_time.configure(text=current_time)
        self.after(1000, self.update_time)

    def widget_frame(self):
        self.frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#2F98EE")
        self.frame.grid(row=2, column=0, padx=(150, 0), pady=10)

        self.create_frame()
        self.create_widget_buttons()

    def create_frame(self):
        self.ink_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#2F98EE")
        self.ink_frame.grid(row=2, column=0, padx=(100, 100), pady=(0, 0), sticky='w')

        for i, pad in enumerate([(20, 5), ((100, 20), 5)]):
            bar = ctk.CTkProgressBar(self.ink_frame, orientation='vertical', height=200, width=50,
                                     corner_radius=0, fg_color='white', progress_color="#17B250")
            bar.grid(row=0, column=i, padx=pad[0], pady=pad[1], sticky='w')

    def create_widget_buttons(self):
        self.create_button_frame('print_set_icon.png', (50, 50), 'Print Set', 200, 120, "#87CEEB", (50, 0), (0, 200), 'w', command=lambda: self.parent.show_frame('print_set'))
        self.create_button_frame('print_file_icon.png', (50, 50), 'File', 200, 120, "#96DDF3", (50, 0), (120, 0), 'w', command=lambda: self.parent.show_frame('file'))
        self.create_button_frame('print_printing_icon.png', (60, 60), 'Start printing', 290, 170, "#2AAA8A", (300, 0), (0, 0), 'nw')

    def create_button_frame(self, image_name, size, text, width, height, fg_color, padx, pady, sticky, command=None):
        image_path = os.path.join("images", image_name)
        try:
            image = ctk.CTkImage(dark_image=Image.open(image_path), size=size)
            button = ctk.CTkButton(self.frame, text=text, image=image, compound='top', command=command,
                                   hover=False, fg_color=fg_color, corner_radius=20,
                                   font=('Arial', 20), width=width, height=height)
            button.grid(row=0, column=0, padx=padx, pady=pady, sticky=sticky)
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
