import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime
import os

from warning_popup import open_warning


class EditScreen(ctk.CTkFrame):
    def __init__(self, parent, go_home_callback, open_sub_screen):
        super().__init__(parent)
        self.parent=parent
        
        self.go_home_callback = go_home_callback 
        self.open_sub_screen = open_sub_screen
        self.font_size = 20
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.create_title_frame()
        self.create_widget_frame()
        self.create_text_editor()
        self.create_button_frame()
        
    def create_title_frame(self):
        self.title_bar = ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        self.title_bar.columnconfigure(0, weight=1)
        self.title_bar.grid(row=0, column=0, sticky="new")

        self.date_time = ctk.CTkLabel(self.title_bar, text="", anchor='e', text_color="white", font=('Arial', 20))
        self.date_time.grid(row=0, column=0, padx=10, sticky='e')

        try:
            image_path = os.path.join(os.path.dirname(__file__), "images", "maximize_icon.png")
            image = ctk.CTkImage(dark_image=Image.open(image_path))
            button = ctk.CTkButton(self.title_bar, text="Test file", anchor='w', image=image, command=lambda: self.parent.show_frame('inkjet_editor'),
                                   fg_color="#A83232", text_color="white", font=('Arial', 20))
            button.grid(row=0, column=0, padx=10, sticky='nw')
        except Exception as e:
            print(f"Title bar error: {e}")

        self.update_time()

    def update_time(self):
        self.date_time.configure(text=datetime.now().strftime("%Y/%m/%d  %H:%M:%S"))
        self.after(1000, self.update_time)

    def create_widget_frame(self):
        self.widget_frame = ctk.CTkFrame(self, fg_color="#C4E3ED", corner_radius=0)
        self.widget_frame.columnconfigure(0, weight=1)
        self.widget_frame.rowconfigure((0, 1), weight=1)
        self.widget_frame.grid(row=1, column=0, sticky="nsew")

        button_list = [
            ("info_icon.png", "Info", lambda: self.parent.show_frame('file')), ("new_icon.png", "New", lambda: open_warning()), ("save_icon.png", "Save", lambda: open_warning()),
            ("copy_icon.png", "Copy", lambda: open_warning()), ("rename_icon.png", "Rename", lambda:self.parent.show_frame('rename')), ("edit_edit_icon.png", "Edit", lambda: open_warning()),
            ("delete_icon.png", "Delete", lambda: self.delete_button_click(self.text_box))
        ]
        
        for idx, (image_name, label, command) in enumerate(button_list):
            try:
                image_path = os.path.join(os.path.dirname(__file__), "images", image_name)
                image = ctk.CTkImage(dark_image=Image.open(image_path), size=(25, 25))
                button = ctk.CTkButton(self.widget_frame, text=label, image=image,
                                       hover_color="#A83232", text_color='black', command= command,
                                       border_width=1, fg_color="#C4E3ED")
                button.grid(row=0, column=0, padx=(10+ idx * 175, 10), pady=10, sticky='w')
            except Exception as e:
                print(f"Widget error: {e}")

    def create_text_editor(self):
        self.text_box = ctk.CTkTextbox(self.widget_frame, text_color='black', fg_color="white",
                                       wrap="none", font=('Arial', self.font_size))
        self.text_box.grid(row=1, column=0, columnspan=6, pady=10, padx=10, sticky='nsew')

    def create_button_frame(self):
        self.button_frame = ctk.CTkFrame(self.widget_frame, fg_color="#96ddf3", width=900, corner_radius=20)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nw')

        buttons = [
            ("edit_text_icon.png", "Text",lambda:self.parent.show_frame('text_input')), ("date_icon.png", "Date", lambda:self.parent.show_frame('date')), ("number_icon.png", "Number",lambda: self.parent.show_frame('number_setting')),
            ("barcode_icon.png", "Barcode", lambda:self.parent.show_frame('barcode')), ("edit_table_icon.png", "Table", lambda:self.parent.show_frame('table')), ("symbol_icon.png", "Symbols", lambda:self.parent.show_frame('symbols')),
            ("image_icon.png", "Image", lambda:self.parent.show_frame('file')), ("txt_icon.png", "TXT file", lambda:self.parent.show_frame('file')), ("edit_xlsx_icon.png", "EXCEL", lambda:self.parent.show_frame('file')),
            ("paragraph_icon.png", "Paragraph",lambda: self.insert_vertical_line(self.text_box))
        ]

        for idx, (img, label, command) in enumerate(buttons):
            try:
                path = os.path.join(os.path.dirname(__file__), "images", img)
                image = ctk.CTkImage(dark_image=Image.open(path), size=(40, 40))
                button = ctk.CTkButton(self.button_frame, text=label, image=image, command=command,
                                       compound="top", text_color='black', fg_color="#96ddf3", font=('Arial', 18))
                button.grid(row=idx // 5, column=idx % 5, pady=10)
            except Exception as e:
                print(f"Button frame error: {e}")
                
        self.exit_print_button()
        self.round_button()
        self.create_button_on_image()

    def round_button(self):
        self.canvas = ctk.CTkCanvas(self.button_frame, width=360, height=350, bg="#96ddf3")
        self.canvas.grid(row=0, column=5, rowspan=2, pady=10, padx=15, sticky='nw')

        try:
            path = os.path.join(os.path.dirname(__file__), "images", 'edit_button.png')
            self.tk_image = ImageTk.PhotoImage(Image.open(path))
            self.canvas.create_image(0, 0, image=self.tk_image, anchor="nw")
        except Exception as e:
            print(f"Canvas image error: {e}")

    def create_button_on_image(self):
        self.add_buttons_on_image('_left_icon.png', (30, 30), '#2F98EE', (40, 100, 20, 90), self.left_button_click)
        self.add_buttons_on_image('_right_icon.png', (30, 30), '#2F98EE', (40, 100, 230, 90), self.right_button_click)
        self.add_buttons_on_image('_up_icon.png', (30, 30), '#2F98EE', (100, 40, 100, 20), self.up_button_click)
        self.add_buttons_on_image('_down_icon.png', (30, 30), '#2F98EE', (100, 40, 100, 220), self.down_button_click)
        self.add_buttons_on_image('_zoom_in_icon.png', (26, 26), '#116CB6', (40, 100, 100, 90), self.zoom_in_button_click)
        self.add_buttons_on_image('_zoom_out_icon.png', (28, 28), '#116CB6', (40, 100, 150, 90), self.zoom_out_button_click)

    def add_buttons_on_image(self, image_file, size, fg, pos, command):
        try:
            image_path = os.path.join(os.path.dirname(__file__), "images", image_file)
            image = ctk.CTkImage(dark_image=Image.open(image_path), size=size)
            button = ctk.CTkButton(self.canvas, text="", image=image,
                                   fg_color=fg, bg_color=fg, corner_radius=0,
                                   width=pos[0], height=pos[1], command=command)
            button.place(x=pos[2], y=pos[3])
        except Exception as e:
            print(f"Overlay button error: {e}")

    def zoom_in_button_click(self):
        self.font_size += 2
        self.text_box.configure(font=('Arial', self.font_size))

    def zoom_out_button_click(self):
        if self.font_size > 6:
            self.font_size -= 2
            self.text_box.configure(font=('Arial', self.font_size))

    def left_button_click(self):
        print("Left clicked")

    def right_button_click(self):
        print("Right clicked")

    def up_button_click(self):
        print("Up clicked")

    def down_button_click(self):
        print("Down clicked")

    def exit_print_button(self):
        self.side_frame = ctk.CTkFrame(self.widget_frame, fg_color="#96ddf3", width=40, corner_radius=20)
        self.side_frame.grid(row=2, column=0, padx=10, pady=10, sticky='ne')

        buttons = [
            ("exit_icon.png", "Exit", self.go_home_callback),
            ("edit_print_icon.png", "Print", lambda: self.parent.show_frame('print'))
        ]

        for idx, (image_name, label, command) in enumerate(buttons):
            try:
                path = os.path.join(os.path.dirname(__file__), "images", image_name)
                image = ctk.CTkImage(dark_image=Image.open(path), size=(50, 50))
                button = ctk.CTkButton(self.side_frame, text=label, image=image, command=command,
                                       compound="top", text_color='black', fg_color="#96ddf3", font=('Arial', 18))
                button.grid(row=idx, column=idx % 1, padx=5, pady=30)
            except Exception as e:
                print(f"Exit/Print button error: {e}")

    def print_action(self):
        print("Print action triggered")
        
    def insert_vertical_line(self, textbox, lines=10, column=0):
        for _ in range(lines):
            line = " " * column + "|\n"
            textbox.insert("insert", line)
            
    def delete_button_click(self):
        self.text_box.configure('end', delete)
    
    
# if __name__ == "__main__":
    
#     root = ctk.CTk()
#     app = EditScreen(root)
#     root.mainloop()
