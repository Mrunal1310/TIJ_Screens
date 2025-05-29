import customtkinter as ctk

def create_roundtripprinting_buttons():
    
    buttons = [
            "OFF", "+1", "+2","+3", "+4", "+5",
            "+6", "+7", "+8","+9", "+10", "+11",
            "+12", "+13", "+14",
    ]
    return buttons

def show_roundtripprinting(base_ref):
    
    buttons = create_roundtripprinting_buttons()
    base_ref.create_buttons(buttons)
    
    
def create_dpi_buttons():
    
    buttons = [
            "300*300", "150*300", "300*150", "150*150", "300*100", "150*100",
    ]
    return buttons

def show_dpi_settings(base_ref):

    buttons = create_dpi_buttons()
    base_ref.create_buttons(buttons)


def create_jet_times():
    
    buttons = [
            "routine", "Bold", "Double", "Triple","Fourfold", "Five times",
            "Six times", "Seven times","Eight times", "Nine times",
    ]
    return buttons

def show_jet_times(base_ref):
    
    buttons = create_jet_times()
    base_ref.create_buttons(buttons)
    


def create_ink_heating():
    
    buttons = [
            "OFF", "+5°C", "+10°C", "+15°C", "+20°C", "+25°C",
    ]
    return buttons

def show_ink_heating(base_ref):
    
    buttons = create_ink_heating()
    base_ref.create_buttons(buttons)
    
def create_multi_frame_cache():
    
    buttons = [
            "OFF", "X2", "X3", "X4", "X5", "X6",
            "X7", "X8", "X9", "X10", "X11",
    ]
    return buttons
    
def show_multi_frame_cache(base_ref):
    
    buttons = create_multi_frame_cache()
    base_ref.create_buttons(buttons)
    
def create_language_buttons():
    buttons = [
            "English", "PY", "Russian","Arabic", "French","German","Polish language","Vietnamese", "Japanese", "Greek", 
            "Korean", "Turkish language","Spanish", "Italian", "Uzbek","Portuguese", "farsi", "Thai","Ukrainian", "Handwriting",
    ]
    return buttons

def show_language(base_ref):
    
    buttons = create_language_buttons()
    base_ref.create_buttons(buttons)
    

def create_date_buttons():
    buttons = [
        "2025-01-07", "2025/01/07", "2025年01月07日",
        "25/01/07", "25-01-07", "25.01.07",
        "25 01 07", "25 Jan 07", "01/07/25",
        "01-07-2025", "01.07.25", "JAN 07 25",
        "07/01/25", "07-01-25", "07.01.25",
        "23:57:54", "23:57", "Term"
    ]
    return buttons

def show_date_(base_ref):
    buttons = create_date_buttons()
    base_ref.create_buttons(buttons)

def create_date_input_buttons():
    return [
        '(2025)Year', '(25)Year', '(03)Month',
        '(10)Day', '(069)Day<001~365>', '(14)Hour',
        '(35)Minutes', '(20)Second', '(MAR)Code:Month',
        '(O)Code:Hour', '(MON)Code:Week', '(J)Code:Day',
    ]

def show_date_input(base_ref):
    buttons = create_date_input_buttons()

    # Render main buttons in a 3-column layout
    base_ref.create_buttons(buttons)
    
def create_code_set_month():
    buttons = [
        'Month-1:JAN','Month-2:FEB','Month-3:MAR',
        'Month-4:APR','Month-5:MAY','Month-6:JUN',
        'Month-7:JUL','Month-8:AUG','Month-9:SEP',
        'Month-10:OCT','Month-11:NOV','Month-12:DEC',
    ]
    return buttons

def show_code_set_month(base_ref):

    buttons = create_code_set_month()
    base_ref.create_buttons(buttons)

def create_code_set_hour():
    buttons = [
        'Hour-00:A','Hour-01:B','Hour-02:C','Hour-03:D',
        'Hour-04:E','Hour-05:F','Hour-06:G','Hour-07:H',
        'Hour-08:I','Hour-09:J','Hour-10:K','Hour-11:L',
        'Hour-12:M','Hour-13:N','Hour-14:O','Hour-15:P',
        'Hour-16:Q','Hour-17:R','Hour-18:S','Hour-19:T',
        'Hour-20:U','Hour-21:V','Hour-22:W','Hour-23:X',
    ]
    return buttons

def show_code_set_hour(base_ref):

    buttons = create_code_set_hour()
    base_ref.create_buttons(buttons)

def create_code_set_week():
    buttons = [
        'Week-1:MON', 'Week-2:TUE',
        'Week-3:WED','Week-4:THU',
        'Week-5:FRI','Week-6:SAT',
        'Week-7:SUN',
    ]
    return buttons

def show_code_set_week(base_ref):

    buttons = create_code_set_week()
    base_ref.create_buttons(buttons)

def create_code_set_day():
    buttons = [
        'Day-1:A', 'Day-2:B','Day-3:C','Day-4:D',
        'Day-5:E','Day-6:F','Day-7:G','Day-8:H',
        'Day-9:I','Day-10:J','Day-11:K','Day-12:L',
        'Day-13:M','Day-14:N','Day-15:O','Day-16:P',
        'Day-17:Q','Day-18:R','Day-19:S','Day-20:T',
        'Day-21:U','Day-22:V','Day-23:W','Day-24:X',
        'Day-25:Y','Day-26:Z','Day-27:AA','Day-28:AB',
        'Day-29:AC','Day-30:AD','Day-31:AE',
    ]
    return buttons

def show_code_set_day(base_ref):

    buttons = create_code_set_day()
    base_ref.create_buttons(buttons)