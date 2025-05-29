import customtkinter as ctk
from PIL import Image
from datetime import datetime
import os


# Main screens
from print_screen import PrintScreen
from file_screen import FileScreen
from edit_screen import EditScreen
from File_list import ImportExport

# Base/Date/Calendar/Utility
from base_print_set import BaseScreen
from base_date import DateBaseScreen
from base_calendar import CalendarWindow
from Font_Language import create_base_frame, create_language_types_buttons, create_font_buttons 
from about_software import create_software_frame
from symbol_size import create_symbol_screen
from number_window import create_number_screen
from base_text_input import TextInput ,create_text_symbol, create_text_symbol_buttons
from permission_setting import create_permission_settings
from qr_code import create_qr_screen


# Buttons & settings
from print_set import create_printset_buttons, printing_direction, create_splicing_settings, nozzle_delay, create_font, font, create_table, table
from setting_window_buttons import create_settings_buttons, time_setting, create_encoderspeedmeasurement_buttons, encoder_speed_measurement_screen, create_printer_buttons, printer, create_user_management_buttons,administrator_screen
from date_screen import (create_roundtripprinting_buttons,create_dpi_buttons, 
                         create_jet_times, create_ink_heating, create_multi_frame_cache, 
                         create_date_buttons, create_language_buttons, create_code_set_month, create_code_set_hour, create_code_set_week, create_code_set_day)
from calendar_screen import create_calender_buttons, create_ink_shortage_alaram_buttons, create_text_input_format_buttons, create_printer_printset_buttons, create_print_sound_buttons, create_style_buttons, create_glyph_buttons, create_term_buttons
from date_input_screen import create_date_input_screen

from inkjet_editor import InkjetEditor


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("CustomTkinter App")
        self.frames = {}

        self.init_frames()
        self.show_frame("home")

    def init_frames(self):
        self.frames["home"] = HomeScreen(self)
        self.frames["print"] = PrintScreen(self, self.show_home, self.show_print_set)
        self.frames["file"] = FileScreen(self, self.show_home)
        self.frames["edit"] = EditScreen(self, self.show_home,  self.show_text_input)

        # BaseScreen examples
        self.add_screen("print_set", BaseScreen, "Print Set", create_printset_buttons, printing_direction, self.show_print_screen)
        self.add_screen("splicing_settings", BaseScreen, "Splicing settings", create_splicing_settings, nozzle_delay, self.show_print_set)
        self.add_screen("setting", BaseScreen, "Setting", create_settings_buttons, time_setting, self.show_home)
        self.add_screen("encoder_speed_measurement", BaseScreen, "Encoder speed measurement", create_encoderspeedmeasurement_buttons, encoder_speed_measurement_screen, self.show_setting_screen)
        self.add_screen("user_management", BaseScreen, "User Management", create_user_management_buttons, administrator_screen, self.show_setting_screen)
        self.add_screen("printer", BaseScreen, "Printer", create_printer_buttons, printer, self.show_setting_screen)
        self.add_screen("font", BaseScreen, "Font", create_font, font, self.show_text_input)
        self.add_screen('table', BaseScreen, 'Table', create_table, table, self.show_edit_screen)
        
        # DateBaseScreen examples
        self.add_date_screen("roundtripprinting", "Round trip printing", create_roundtripprinting_buttons, 6, 3, self.show_print_set)
        self.add_date_screen("dpi", "DPI", create_dpi_buttons, 3, 2, self.show_print_set)
        self.add_date_screen("jettimes", "Jet times", create_jet_times, 5, 2, self.show_print_set)
        self.add_date_screen("ink_heating", "Ink heating", create_ink_heating, 3, 2, self.show_print_set)
        self.add_date_screen("multi_frame_cache", "Multi frame cache", create_multi_frame_cache, 4, 3, self.show_setting_screen)


        # CalendarWindow examples
        self.add_calendar_screen("calendar_screen", "Calendar", create_calender_buttons, 3, self.show_setting_screen)
        self.add_calendar_screen("ink_shortage_alarm", "Ink shortage alarm", create_ink_shortage_alaram_buttons, 3, self.show_setting_screen)
        self.add_calendar_screen("text_input_format", "Text Input Format", create_text_input_format_buttons, 5, self.show_setting_screen)
        self.add_calendar_screen("printer_print_set", "Printer", create_printer_printset_buttons, 3, self.show_print_set)
        self.add_calendar_screen("print_sound", "Print sound", create_print_sound_buttons, 4, self.show_print_set)
        
        # Language + About Software
        language_buttons = create_language_types_buttons()
        self.frames["language_types"] = create_base_frame(self, "Language", language_buttons, self.show_setting_screen)
        
        self.frames["about"] = create_software_frame(self, self.show_setting_screen)
        
        # Edit screen -Text Button window
        text_screen = TextInput(self, 'Font', 'Text input',["close_icon.png", "check_icon.png", "font_icon.png"], self.show_edit_screen, self.show_font)
        self.frames['text_input'] = text_screen
        
        rename_button_screen = TextInput(self, '', 'Rename',["close_icon.png", "check_icon.png", ""], self.show_edit_screen,  self.show_frame('font'))
        self.frames['rename'] = rename_button_screen
        
        manufacture_info_screen = TextInput(self, '', 'Manufacture information',["close_icon.png", "check_icon.png", ""], self.show_setting_screen,  self.show_frame('font'))
        self.frames['manufacture_info'] = manufacture_info_screen
        
        barcode_screen = TextInput(self, 'Select code', 'QR',["close_icon.png", "check_icon.png", "qr_code_icon.png"], self.show_edit_screen, self.show_barcode_screen)
        self.frames['barcode'] = barcode_screen
        
        self.add_date_screen("date", "Date input", create_date_buttons, 6, 3, self.show_edit_screen)
        self.frames["symbols"] = create_symbol_screen(self, self.show_edit_screen)
        self.frames["number_setting"] = create_number_screen(self, self.show_edit_screen)
        
        font_buttons = create_font_buttons()
        self.frames["font_types"] = create_base_frame(self, "Font", font_buttons, self.show_font)
        
        self.add_calendar_screen("style", "Style", create_style_buttons, 3, self.show_font)
        self.add_calendar_screen("glyph", "Glyph", create_glyph_buttons, 4, self.show_font)
        
        
        button_list=[("Import all"),("Import")]
        button_command=None
        
        self.frames["import_file"] = ImportExport(self, "Import", button_list, self.show_setting_screen)
        
        button_list=[ ("Export all"),("Export")]
        button_command=None
        
        self.frames["export_file"] = ImportExport(self, "Export", button_list, self.show_setting_screen)

        self.add_calendar_screen("term", "Term", create_term_buttons, 4, self.show_date_input_text)

        self.add_date_screen("language", "Language", create_language_buttons, 7, 3, self.show_text_input)

        symbol_buttons = create_text_symbol_buttons()
        self.frames["text_symbols"] = create_text_symbol(self, "Symbols", symbol_buttons, self.show_text_input)

        self.frames["permission"] = create_permission_settings(self, "Permission", self.show_setting_screen)

        self.frames["date_input_text"] = create_date_input_screen(parent=self, controller=self, close_command=self.show_text_input)

        self.frames['qrcode']= create_qr_screen(self, self.show_text_input)

        self.add_date_screen("code_set_month", "Code set(Month)", create_code_set_month, 4, 3, self.show_date_input_text)
        self.add_date_screen("code_set_hour", "Code set(Hour)", create_code_set_hour, 6, 4, self.show_date_input_text)
        self.add_date_screen("code_set_week", "Code set(Week)", create_code_set_week, 4, 2, self.show_date_input_text)
        self.add_date_screen("code_set_day", "Code set(Day)", create_code_set_day, 8, 4, self.show_date_input_text)
        
        self.frames['inkjet_editor'] = InkjetEditor(self, self.show_edit_screen)

        # Hide all frames initially
        for frame in self.frames.values():
            frame.pack_forget()

    def add_screen(self, name, screen_class, title, button_func, content_func, back_cmd):
        screen = screen_class(self, title, [], back_cmd)
        buttons = button_func(screen)
        screen.create_buttons(buttons)
        content_func(screen)
        self.frames[name] = screen

    def add_date_screen(self, name, title, button_func, row, col, back_cmd):
        screen = DateBaseScreen(self, title, [], row, col, back_cmd)
        buttons = button_func()
        screen.create_buttons(buttons, col)
        self.frames[name] = screen

    def add_calendar_screen(self, name, title, button_func, rows, back_cmd):
        screen = CalendarWindow(self, title, [], rows, back_cmd)
        buttons = button_func()
        screen.create_buttons(buttons)
        self.frames[name] = screen
        

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

    def show_home(self):
        self.show_frame("home")

    def show_print_screen(self):
        self.show_frame("print")
    
    def show_edit_screen(self):
        self.show_frame('edit')

    def show_print_set(self):
        self.show_frame("print_set")

    def show_setting_screen(self):
        self.show_frame("setting")
        
    def show_text_input(self):
        self.show_frame('text_input')
        
    def show_barcode_screen(self):
        self.show_frame('qrcode')
        
    def show_font(self):
        self.show_frame('font')
        
    def show_term(self):
        self.show_frame('term')
        
    def show_language(self):
        self.show_frame('language')
        
    def show_permission(self):
        self.show_frame('permission')

    def show_text_symbol(self):
        self.show_frame('symbol')

    def show_date_input_text(self):
        self.show_frame('date_input_text')
        
    def show_code_set_month(self):
        self.show_frame('code_set_month')

    def show_code_set_hour(self):
        self.show_frame('code_set_hour')

    def show_code_set_week(self):
        self.show_frame('code_set_week')

    def show_code_set_day(self):
        self.show_frame('code_set_day')
        
    def show_inkjet_editor(self):
        self.show_frame('inkjet_editor')

class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(fg_color="#318CE7")
        ctk.set_appearance_mode("light")

        self.columnconfigure((0, 2), weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure((0, 2), weight=0)
        self.rowconfigure((1,), weight=2)

        self.time_date_day_label()
        self.update_time()
        self.create_buttons()

    def time_date_day_label(self):
        self.time_label = ctk.CTkLabel(self, text="", text_color="white", fg_color="#318CE7", font=("Arial", 50))
        self.time_label.grid(row=0, column=1, sticky='nw', pady=(100, 0))

        self.date_day_label = ctk.CTkLabel(self, text="", text_color="white", fg_color="#318CE7", font=("Arial", 25))
        self.date_day_label.grid(row=0, column=1, sticky='w', pady=(150, 0))

        self.version_label = ctk.CTkLabel(self, text="V15.8.9", text_color="white", bg_color="#318CE7", font=("Arial", 20))
        self.version_label.grid(row=2, column=2, sticky='e', padx=(10, 10), pady=10)

    def update_time(self):
        now = datetime.now()
        self.time_label.configure(text=now.strftime("%H:%M:%S"))
        self.date_day_label.configure(text=now.strftime("\n%Y/%m/%d %A"))
        self.after(1000, self.update_time)

    def create_buttons(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(script_dir, "images")

        def load_image(name, size):
            return ctk.CTkImage(dark_image=Image.open(os.path.join(image_dir, name)), size=size)

        buttons = [
            ("Print", "print_icon.png", "#87CEFF", self.parent.show_print_screen, (0, 0)),
            ("File", "files_icon.png", "#5CACEE", lambda: self.parent.show_frame("file"), (0, 200)),
            ("Edit", "edit_icon.png", "#EE3B3B", lambda: self.parent.show_frame("edit"), (200, 0)),
            ("Setting", "setting_icon.png", "#B452CD", lambda: self.parent.show_frame("setting"), None),
        ]

        for i, (text, icon, color, cmd, padx) in enumerate(buttons):
            image = load_image(icon, (60, 60) if text != "Edit" and text != "Setting" else (50, 50))
            btn = ctk.CTkButton(
                self, text=text, image=image, command=cmd,
                fg_color=color, bg_color="#318CE7", hover=False,
                width=150, height=200, compound="top",
                corner_radius=10, font=("Arial", 20)
            )
            btn.grid(row=1, column=1, padx=padx or 0, sticky="w" if i == 0 else "e" if text == "Setting" else "")


if __name__ == "__main__":
    app = App()
    app.mainloop()
