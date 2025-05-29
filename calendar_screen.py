import customtkinter as ctk

from popup_box import open_popup_box


def create_calender_buttons():
    buttons = [
        "Gregorian calendar", "Jalali date", "Islamic calendar"
    ]
    return buttons

def show_calender(base_ref):
    
    buttons = create_calender_buttons()
    base_ref.create_buttons(buttons)
    
    
    
def create_ink_shortage_alaram_buttons():
    buttons = [
        "OFF", "Built in buzzer", "External alarm"
    ]
    return buttons

def show_ink_shortage_alaram(base_ref):
    
    buttons = create_calender_buttons()
    base_ref.create_buttons(buttons)
    
    
def create_text_input_format_buttons():
    buttons = [
        "routine", "Arabic", "farsi", "Thai", "Portuguese",
    ]
    return buttons

def show_text_input_format(base_ref):
    
    buttons = create_calender_buttons()
    base_ref.create_buttons(buttons)
    
    
def create_printer_printset_buttons():
    buttons = [
        "Right", "Left", "Both print"
    ]
    return buttons

def show_printer_print_set(base_ref):
    
    buttons = create_printer_printset_buttons()
    base_ref.create_buttons(buttons)
    
def create_print_sound_buttons():
    buttons = [
        "OFF", "Start only", "Complete only", "Satrt to finish"
    ]
    return buttons

def show_print_sound(base_ref):
    
    buttons = create_print_sound_buttons()
    base_ref.create_buttons(buttons)
    
    
# Font Screen Buttons 
def create_style_buttons():
    buttons = [
        "Entity", "Lattice", "Delete type",
    ]
    return buttons

def show_style(base_ref):
    
    buttons = create_style_buttons()
    base_ref.create_buttons(buttons)
    
def create_glyph_buttons():
    buttons = [
        "routine", "Bold", "Italics", "Bold italics"
    ]
    return buttons

def show_glyph_buttons(base_ref):
    
    buttons = create_glyph_buttons()
    base_ref.create_buttons(buttons)
    
    
def create_term_buttons():
    buttons = [
        '(0)Year', '(0)Month', '(0)Day'
    ]
    return buttons

def show_term_buttons(base_ref):

    buttons = create_term_buttons()
    for text in buttons:
        button = ctk.CTkButton(base_ref, text=text)
        if text == '(0)Year':
            button.configure(command=lambda: open_popup_box(" Year"))
        elif text == '(0)Month':
            button.configure(command=lambda: open_popup_box(" Month"))
        elif text == '(0)Day':
            button.configure(command=lambda: open_popup_box(" Day"))
        
    base_ref.create_buttons(buttons)