import customtkinter as ctk

from popup_box import open_popup_box

def printing_direction(base):
    base.clear_right_content()
    base.add_label_switch("Reverse (Printer 1)", row=0)
    base.add_label_switch("Nozzle turnover (Printer 1)", row=1)
    base.add_label_switch("Reverse (Printer 2)", row=2)
    base.add_label_switch("Nozzle turnover (Printer 2)", row=3)
    base.add_button_with_arrow("Round trip printing", row=4, command=lambda: base.parent.show_frame("roundtripprinting"))

def photoelectric_setting(base):
    base.clear_right_content()
    base.add_label_switch("Photoelectricity", row=0)
    base.add_label_switch("Sensor phase", row=1)
    base.add_button_with_arrow("Sensor shielding distance", row=2, command = lambda: open_popup_box("Sensor shielding distance"))
    base.add_button_with_arrow("Continuous printing times", row=3, command = lambda: open_popup_box("Continuous printing times"))
    base.add_button_with_arrow("Print interval", row=4, command = lambda: open_popup_box("Print interval"))
    base.add_button_with_arrow("Delay(1)", row=5, command = lambda: open_popup_box("Delay"))
    base.add_button_with_arrow("Delay(2)", row=6, command = lambda: open_popup_box("Delay"))
    
def continuous_setting(base):
    base.clear_right_content()
    base.add_label_switch("Reverse (Printer 1)", row=0)
    base.add_button_with_arrow("Print interval", row=1, command = lambda: open_popup_box("Print Interval"))
    base.add_button_with_arrow("Consecutive times", row=2, command = lambda: open_popup_box("Consecutive times"))

def control(base):
    base.clear_right_content()
    base.add_label_switch("Encoder switch", row=0)
    base.add_button_with_arrow("Encoder div", row=1, command = lambda: open_popup_box("Encoder div"))
    base.add_button_with_arrow("Speed", row=2, command = lambda: open_popup_box("Speed"))
    base.add_button_with_arrow("frequency doubling", row=3, command = lambda: open_popup_box("frequency doubling"))
    base.add_button_with_arrow("DPI", row=4, command=lambda: base.parent.show_frame("dpi"))

    
def printer(base):
    base.clear_right_content()
    base.add_button_with_arrow("Left or Right", row=0, command = lambda: base.parent.show_frame("printer_print_set"))
    base.add_button_with_arrow("Voltage", row=1, command = lambda: open_popup_box("Voltage"))
    base.add_button_with_arrow("Pulse width", row=2, command = lambda: open_popup_box("Pulse width"))
    base.add_button_with_arrow("Jet times", row=3, command = lambda: base.parent.show_frame('jettimes'))
    base.add_button_with_arrow("Printer", row=4, )
    base.add_button_with_arrow("Splicing settings", row=5, command = lambda: base.parent.show_frame('splicing_settings'))
    base.add_button_with_arrow("Ink heating", row=6, command = lambda: base.parent.show_frame('ink_heating'))
    
def others(base):
    base.clear_right_content()
    base.add_button_with_arrow("Print sound", row=0, command = lambda: base.parent.show_frame("print_sound"))
    base.add_label_switch("screen refresh", row=1)
    base.add_button_with_arrow("Print times", row=2, command = lambda: open_popup_box("Print times"))
    base.add_button_with_arrow("Spay times", row=3, command = lambda: open_popup_box("Spay times"))
    base.add_label_switch("High DPI", row=4)
    base.add_label_switch("Gap free printing", row=5)
    base.add_label_switch("Real printing time", row=6)

def create_printset_buttons(base_ref):
    return [
        ("Printing direction", "printing_direction_icon.png", lambda: printing_direction(base_ref)),
        ("Photoelectric setting", "photoelectric_setting_icon.png", lambda: photoelectric_setting(base_ref)),
        ("Continuous setting", "continuous-printing_icon.png", lambda: continuous_setting(base_ref)),
        ("Control", "control_icon.png", lambda: control(base_ref)),
        ("Printer", "printer_icon.png", lambda: printer(base_ref)),
        ("Others", "other_icon.png", lambda: others(base_ref)),
    ]
    
    
# This code is to call splicing settings in print set
def nozzle_delay(base):
    base.clear_right_content()
    base.add_button_with_arrow("P1", row=0, command=lambda: open_popup_box("Nozzle delay"))
    base.add_button_with_arrow("P2", row=1, command=lambda: open_popup_box("Nozzle delay"))

def overlap(base):
    base.clear_right_content()
    base.add_button_with_arrow("P1-P2", row=0, command=lambda: open_popup_box("Overlap"))

def create_splicing_settings(base_ref):
    return [
        ("Nozzle delay", "nozzle_icon.png", lambda: nozzle_delay(base_ref)),
        ("Overlap", "overlap_icon.png", lambda: overlap(base_ref)),
    ]
    
    
# Font button screen
def font(base):
    base.clear_right_content()
    base.add_button_with_arrow("Font", row=0, command = lambda: base.parent.show_frame('font_types'))
    base.add_button_with_arrow("Style", row=1, command = lambda: base.parent.show_frame("style"))
    base.add_button_with_arrow("Height", row=2, command = lambda: open_popup_box("Font Height"))
    base.add_button_with_arrow("Width", row=3, command = lambda: open_popup_box("Font Width"))
    base.add_button_with_arrow("Interval", row=4, command = lambda: open_popup_box("Interval") )
    base.add_button_with_arrow("Font Angle", row=5, command = lambda: open_popup_box('Font Angle'))
    base.add_button_with_arrow("Glyph", row=6, command = lambda: base.parent.show_frame('glyph'))

def create_font(base_ref):
    return [
        ("Font", "font_button_icon.png", lambda: font(base_ref)),
    ]
    
    
def table(base):
    base.clear_right_content()
    base.add_button_with_arrow("Rows", row=0, command = lambda: open_popup_box("Rows:"))
    base.add_button_with_arrow("Columns", row=1, command = lambda: open_popup_box("Columns:"))
    base.add_button_with_arrow("Border", row=2, command = lambda: open_popup_box("Border:") )
    
def size(base):
    base.clear_right_content()
    base.add_button_with_arrow("Row height", row=0, command = lambda: open_popup_box("Row height"))
    base.add_button_with_arrow("Column width", row=1, command = lambda: open_popup_box("Column width"))
    base.add_label_switch("Merge", row=2)

def text(base):
    base.clear_right_content()
    base.add_button_with_arrow("Text", row=1, command = lambda: base.parent.show_frame('text_input'))
    base.add_label_switch("Center", row=2)
    
def create_table(base_ref):
    return [
        ("Table", "table_icon.png", lambda: table(base_ref)),
        ("Size", "size_icon.png", lambda: size(base_ref)),
        ("Text", "text_icon.png", lambda: text(base_ref)),
    ]