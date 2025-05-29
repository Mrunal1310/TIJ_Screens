import customtkinter as ctk
from PIL import Image
import os

def create_base_frame(parent, title, button_list, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    frame.pack(fill="both", expand=True)
    
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)
    
    create_title_frame(frame, title, controller)
    create_button_frame(frame, button_list)
    
    return frame

# Title bar with label, close and check icons

def create_title_frame(parent, title, command):
    frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="new")

    label = ctk.CTkLabel(frame, text=title, fg_color="#A83232", corner_radius=0,
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

def create_button_frame(parent, button_list):
    scroll = ctk.CTkScrollableFrame(parent, orientation="vertical", fg_color='white')
    scroll.columnconfigure((0, 1), weight=1)
    scroll.rowconfigure(0, weight=1)
    scroll.grid(row=1, column=0, pady=10, sticky='news')

    for indx, text in enumerate(button_list):
        row = indx // 2
        column = indx % 2
        btn = ctk.CTkButton(scroll, text=text, text_color="black", anchor="w",
                            hover_color="pink", border_width=1, fg_color="white",
                            corner_radius=0, font=("Arial", 20), command=lambda lbl= text: clicked_button(lbl))
        btn.grid(row=row, column=column, ipadx=10, ipady=20, sticky="ew")
        
def create_check_button():
    print("Check button clicked")

def clicked_button(button_text):
    print(f"Button clicked: {button_text}")
    
    
# Language Screen - Button list of languages
def create_language_types_buttons():
    button_list = [
        "简体中文", "繁體中文", "English", "русский язык",
        "日本語", "Deutsch", "Français", "한국어",
        "Italiano", "Polska Yu", "Nederlands", "Suomen kieli",
        "لغة عربية", "Dansk sprog", "Česko", "Svenskt språk",
        "Tiếng Việt", "Ελληνική γλώσσα", "Turco", "Español",
        "Português", "فارسی", "ภาษาไทย", "O'zbek",
        "বাংলার ভাষা", "Swahili", "Українська", "Indonesia"
    ]
    return button_list


def show_language(base_ref):
    buttons = create_language_types_buttons()
    create_button_frame(base_ref, buttons) 
    
    
def create_font_buttons():
    button_list = ["SongTi", "KaiTi",
                        "LiShu", "XingKai",
                        "HeiTi", "FangSong",
                        "YaHei", "YouYuan",
                        "ShuTi", "YaoTi",
                        "ZhunYuan", "FZHeiTi",
                        "FZKaiTi",  "ShaoEr",
                        "FZXingKai", "HWLiShu",
                        "HWXinWei", "HWKaiTi",
                        "HWZhongSong", "HWXiHei",
                        "HWHuPo", "HWXingKai",
                        "HwFangSong", "GuangGao",
                        "ShouXie", "NiuNiu",
                        "Hollow","SYHeiTi",
                        "PenMa Dot", "Batang",
                        "Garamond", "New Roman",
                        "Arial Unicode", "Rockwell",
                        "ShuZi Dot", "ASCII Dot",
                        "Round Dot", "KPN Dot",
                        "Chinese Dot", "Paco",
                        "USB Disk",
                        ]
    return button_list



def show_font(base_ref):
    buttons = create_font_buttons()
    create_button_frame(base_ref, buttons)
    
    

# def create_base_frame(parent, title, button_list, controller):
#     frame = ctk.CTkFrame(parent, fg_color="white")
#     frame.pack(fill="both", expand=True)
    
#     frame.columnconfigure(0, weight=1)
#     frame.rowconfigure(0, weight=0)
#     frame.rowconfigure(1, weight=1)
    
#     create_title_frame(frame, title, controller)
#     create_button_frame(frame, button_list)
    
#     return frame


# # Title bar with label, close and check icons

# def create_text_symbol(parent, title, button_list, controller):
#     frame = ctk.CTkFrame(parent, fg_color="white")
    
#     frame.columnconfigure(0, weight=1)
#     frame.rowconfigure(0, weight=0)
#     frame.rowconfigure(1, weight=1)

#     create_title_frame(frame, title, controller)
#     create_button_frame(frame, button_list)

#     return frame

# def create_title_frame(parent, title, close_command):
#     frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
#     frame.grid(row=0, column=0, sticky="ew")
#     frame.columnconfigure(0, weight=1)
#     frame.columnconfigure(1, weight=0)

#     # Title Label
#     title_label = ctk.CTkLabel(
#             frame,text=title,fg_color="#A83232",
#             anchor="center",text_color="white",font=("Arial", 20, "bold")
#         )
#     title_label.grid(row=0, column=0, pady=5, padx=0, sticky="new")

#     # Load close icon
#     try:
#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         image_path = os.path.join(script_dir, "images", "close_icon.png")

#         close_image = ctk.CTkImage(dark_image=Image.open(image_path), size=(20, 20))
#         close_button = ctk.CTkButton(frame, text="", image=close_image,
#             command=close_command, hover_color="#A83232", fg_color="#A83232",
#             width=40, height=20, corner_radius=0)
        
#         close_button.grid(row=0, column=0, padx=(0, 50), sticky="e")
        
#     except FileNotFoundError:
#             print(f"Error: Image not found at {image_path}")
#     except Exception as e:
#         print(f"An error occurred loading close button: {e}")

# def create_button_frame(parent, button_list):
#     scroll = ctk.CTkScrollableFrame(parent, fg_color='white') #orientation="vertical",
#     # scroll.columnconfigure((0), weight=1)
#     # scroll.rowconfigure(0, weight=1)
#     scroll.grid(row=1, column=0, pady=20, sticky='news')

#     for indx, text in enumerate(button_list):
#         row = indx // 18
#         column = indx % 18
#         btn = ctk.CTkButton(scroll, text=text,
#                 command=lambda lbl=text: clicked_button(lbl),  # Correct lambda binding
#                 corner_radius=0,height=50, width=50,
#                 fg_color="#FF00FF",
#                 text_color="black",
#                 font=("Arial", 15,))
#         btn.grid(row=row, column=column,padx=(7),pady=7)


# def clicked_button(button_text):
#     print(f"Button clicked: {button_text}")
    

# def create_text_symbol_buttons():
#     button_list = [
#         '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', ':',
#         '<', '=', '>', '?', '@', '℃', '[', '\\', ']', '^', '_', 'ʹ', '˝', '`', '͊', '‘', '’',
#         '{', '|', '}', '~', '≃', '¥', '͞', '–', '·', '̌', '¨', '°', '¯', '‖', '⌈', '⌋', '…',
#         '“', '”', '⟦', '⟧', '⟮', '⟯', '⟨', '⟩', '⟪', '⟫', '×', '÷', '±', '∧', '∨', '∑', 'π',
#         '∷', '√', '⊙', '≡', '⍺', '≈', '≠', '⊥', '⌒', '≤', '≥', '˭', '★', '☆', '○', '●', '■',
#         '□', '▲', '△', '←', '↑', '→', '↓', '™', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii',
#         'viii', 'ix', 'x', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.',
#         '11.', '12.', '13.', '14.', '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)',
#         '(9)', '(10)', '(11)', '(12)', '(13)', '(14)', '(15)', '(16)', '(17)', '(18)',
#         '(19)', '(20)', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '（一）','（二）','（三）',
#         '（四）','（五）', '（六）', '（七）','（八）', '（九）', '（十）','Ⅰ', 'Ⅱ', 'Ⅲ',
#         'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', '₢', '₱', '₹', 'Rs', '₨', '₣', '₤',
#         '€', '£', '¥', '₿', 'ɸ', '⌀', 'ḍ'
#     ]
#     return button_list


# def show_text_symbol(base_ref):
#     buttons = create_text_symbol_buttons()
#     base_ref.create_buttons(buttons)



