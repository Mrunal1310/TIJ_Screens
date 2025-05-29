import customtkinter as ctk
from base_print_set import BaseScreen

from warning_popup import open_warning
from popup_box import open_popup_box

def create_label(container, text, row, padx=20, pady=(20, 25), column=0):
    label = ctk.CTkLabel(
        container, text=text, text_color='black',
        font=("Arial", 20), fg_color="white", anchor='w'
    )
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky='w')
    return label

def create_entry(container, row, padx, pady=(0, 25), column=0, command=None):
    entry = ctk.CTkEntry(
        container, width=130, height=40, border_width=0,
        text_color='black', font=("Arial", 20),
        corner_radius=0, fg_color="#C4E3ED"
    )
    entry.grid(row=row, column=column, padx=padx, pady=pady, sticky='w')
    if command:
        entry.bind("<Button-1>", lambda e: command())
    return entry

def create_separator(container, symbol, row, padx, pady=(0, 30), column=0):
    label = ctk.CTkLabel(
        container, text=symbol, text_color='black',
        font=("Arial", 30), fg_color="white", anchor='w'
    )
    label.grid(row=row, column=column, padx=padx, pady=pady, sticky='w')
    return label

# 👉 Fix: Add "commands" parameter properly
def create_entry_group(container, row, separator, start_padx=20, commands=None, spacing=40):
    x_offset = start_padx
    for i in range(3):
        command = commands[i] if commands else None
        create_entry(container, row=row, padx=(x_offset, 20), command=command)
        x_offset += 230
        if i < 2:
            create_separator(container, separator, row=row, padx=(x_offset - 50, 20))

# --- Settings Pages ---

def time_setting(base):
    base.clear_right_content()
    base.add_button_with_arrow("Calender", row=0, command = lambda: base.parent.show_frame('calendar_screen'))
    base.add_button_with_arrow("Date jump time", row=1, command=lambda: open_popup_box("Date jump time"))

    create_label(base.right_content, 'Date', row=3)
    create_entry_group(
        base.right_content, row=4, separator='/',
        commands=[
            lambda: open_popup_box("Year"),
            lambda: open_popup_box("Month"),
            lambda: open_popup_box("Day")
        ]
    )

    create_label(base.right_content, 'Time', row=5)
    create_entry_group(
        base.right_content, row=6, separator=':',
        commands=[
            lambda: open_popup_box("Hour"),
            lambda: open_popup_box("Minute"),
            lambda: open_popup_box("Second")
        ]
    )

def import_export(base):
    base.clear_right_content()
    base.add_button_with_arrow("Import", row=0, command = lambda: base.parent.show_frame('import_file'))
    base.add_button_with_arrow("Export", row=1, command = lambda: base.parent.show_frame('export_file'))

def sensor(base):
    base.clear_right_content()
    base.add_button_with_arrow("Photoelectric signal", row=0)
    base.add_button_with_arrow("Encoder", row=1)
    base.add_button_with_arrow("Encoder speed measurement", row=2, command = lambda: base.parent.show_frame('encoder_speed_measurement'))

def information(base):
    base.clear_right_content()
    base.add_button_with_arrow("Check update", row=0, command = lambda: open_warning())
    base.add_button_with_arrow("Manufacture information", row=1, command= lambda: base.parent.show_frame('manufacture_info'))
    base.add_button_with_arrow("Output clearing", row=2, command = lambda: open_warning())
    base.add_button_with_arrow("Factory model", row=3, command = lambda: open_warning())
    base.add_button_with_arrow("Software", row=4,command = lambda: open_warning())
    base.add_button_with_arrow("About", row=5, command= lambda: base.parent.show_frame('about'))
    base.add_button_with_arrow("User management", row=6, command= lambda: base.parent.show_frame('user_management'))

def setting(base):
    base.clear_right_content()
    base.add_label_switch("Key tone", row=0)
    base.add_button_with_arrow("Restore", row=1, command = lambda: open_warning())
    base.add_button_with_arrow("Touch screen test", row=2)
    base.add_button_with_arrow("Screen off", row=3, command=lambda: open_popup_box("Screen off"))
    base.add_button_with_arrow("Ink shortage alarm", row=4, command= lambda: base.parent.show_frame('ink_shortage_alarm'))
    base.add_button_with_arrow("Alarm value", row=5, command=lambda: open_popup_box("Alarm value"))
    base.add_button_with_arrow("Multi frame cache", row=6, command= lambda: base.parent.show_frame('multi_frame_cache'))
    base.add_button_with_arrow("Printer", row=7, command = lambda: base.parent.show_frame('printer'))

def language(base):
    base.clear_right_content()
    base.add_button_with_arrow("Language", row=0, command= lambda: base.parent.show_frame('language_types'))
    base.add_button_with_arrow("Text Input Format", row=1, command = lambda: base.parent.show_frame('text_input_format'))
    
    
# 👉 Fix: remove command= parameter (you were mixing command/commands)
def create_settings_buttons(base_ref):
    return [
        ("Time setting", "time_setting_icon.png", lambda: time_setting(base_ref)),
        ("Import and export", "import_export_icon.png", lambda: import_export(base_ref)),
        ("Sensor", "sensor_icon.png", lambda: sensor(base_ref)),
        ("Information", "information_icon.png", lambda: information(base_ref)),
        ("Setting", "setting_setting_icon.png", lambda: setting(base_ref)),
        ("Language", "language_icon.png", lambda: language(base_ref)),
    ]



# This code is for encoder speed measurement in setting screen
def encoder_speed_measurement_screen(base):
    
    base.add_button_with_arrow("Encoder pulse number", row=0, command=lambda: open_popup_box("Encoder pulse number"))
    base.add_button_with_arrow("Diameter of synchronnous wheel", row=1, command=lambda: open_popup_box("Diameter of synchronnous wheel"))
    
    # base.create_encoderspeedmeasurement_buttons()
    
def create_encoderspeedmeasurement_buttons(base_ref):
    return[
        ("Encoder speed measurement", "encoder_speed_icon.png", lambda: encoder_speed_measurement_screen(base_ref))
    ]
    
    
def printer(base):
    
    base.add_button_with_arrow("P1", row=0, command=lambda: open_popup_box("P1"))
    base.add_button_with_arrow("P2", row=1, command=lambda: open_popup_box("P2"))
    base.add_button_with_arrow("Check update", row=3, command=lambda: open_warning())
    
    # base.create_encoderspeedmeasurement_buttons()
    
def create_printer_buttons(base_ref):
    return[
        ("Printer", "information_icon.png", lambda: printer(base_ref))
    ]

# User Management screen 

def administrator_screen(base):
    base.clear_right_content()
    base.add_label_switch("Enable", row=0)
    base.add_button_with_arrow("User name", row=1, command= lambda: base.parent.show_frame('text_input'))

def user_1_screen(base):
        base.clear_right_content()
        base.add_label_switch("Enable", row=0)
        base.add_button_with_arrow("User name", row=1, command=lambda: base.parent.show_frame('text_input'))
        base.add_button_with_arrow("Password", row=2, command=lambda: open_popup_box(" Set password"))
        base.add_button_with_arrow('Permission settings', row=3, command=lambda: base.parent.show_frame('permission'))


def user_2_screen(base):
        base.clear_right_content()
        base.add_label_switch("Enable", row=0)
        base.add_button_with_arrow("User name", row=1,command=lambda: base.parent.show_frame('text_input'))
        base.add_button_with_arrow("Password", row=2, command=lambda: open_popup_box(" Set password"))
        base.add_button_with_arrow('Permission settings', row=3, command=lambda: base.parent.show_frame('permission'))


def user_3_screen(base):
        base.clear_right_content()
        base.add_label_switch("Enable", row=0)
        base.add_button_with_arrow("User name", row=1, command=lambda: base.parent.show_frame('text_input'))
        base.add_button_with_arrow("Password", row=2, command=lambda: open_popup_box(" Set password"))
        base.add_button_with_arrow('Permission settings', row=3, command=lambda: base.parent.show_frame('permission'))


def user_4_screen(base):
        base.clear_right_content()
        base.add_label_switch("Enable", row=0)
        base.add_button_with_arrow("User name", row=1, command=lambda: base.parent.show_frame('text_input'))
        base.add_button_with_arrow("Password", row=2, command=lambda: open_popup_box(" Set password"))
        base.add_button_with_arrow('Permission settings', row=3, command=lambda: base.parent.show_frame('permission'))


def user_5_screen(base):
        base.clear_right_content()
        base.add_label_switch("Enable", row=0)
        base.add_button_with_arrow("User name", row=1, command=lambda: base.parent.show_frame('text_input'))
        base.add_button_with_arrow("Password", row=2, command=lambda: open_popup_box(" Set password"))
        base.add_button_with_arrow('Permission settings', row=3, command=lambda: base.parent.show_frame('permission'))

def create_user_management_buttons(base_ref):
    return[
        ("Administrator", "administrator_icon.png", lambda: administrator_screen(base_ref)),
        ("User 1", "user_icon.png", lambda: user_1_screen(base_ref)),
        ("User 2", "user_icon.png", lambda: user_2_screen(base_ref)),
        ("User 3", "user_icon.png", lambda: user_3_screen(base_ref)),
        ("User 4", "user_icon.png", lambda: user_4_screen(base_ref)),
        ("User 5", "user_icon.png", lambda: user_5_screen(base_ref)),
    ]

