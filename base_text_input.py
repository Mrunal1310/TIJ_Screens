import customtkinter as ctk
from PIL import Image
import os


class TextInput(ctk.CTkFrame):
    def __init__(self,parent, button_name, title, image_list, close_command, open_command):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="both", expand=True)
        self.configure(fg_color='white')

        self.is_caps = False
        self.buttons = {}

        self.title_label(button_name, title, image_list, close_command, open_command)
        self.text_editor()
        self.entry_box()
        self.keyboard_frame()

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2), weight=0)
        self.rowconfigure(3, weight=1)

    def title_label(self, button_name, title, image_list, close_command, open_command):
        title_frame = ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        title_frame.grid(row=0, column=0, sticky="ew")
        title_frame.columnconfigure((0), weight=1)

        label = ctk.CTkLabel(
            title_frame,
            text=title,
            fg_color="#A83232",
            corner_radius=0,
            anchor="center",
            text_color="white",
            font=("Arial", 20, "bold"),
        )
        label.grid(row=0, column=0, sticky="ew")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = "images"

        for image_name in image_list:
            try:
                image_path = os.path.join(script_dir, image_dir, image_name)
                image = ctk.CTkImage(dark_image=Image.open(image_path), size=(20, 20))

                if image_name == "close_icon.png":
                    close_button = ctk.CTkButton(
                        title_frame,
                        text="",
                        image=image,
                        command=close_command,
                        hover_color="#D32F2F",
                        fg_color="#A83232",
                        width=30,
                        height=30,
                        corner_radius=0,
                    )
                    close_button.grid(row=0, column=0, sticky="e", padx=60)

                elif image_name == "check_icon.png":
                    check_button = ctk.CTkButton(
                        title_frame,
                        text="",
                        image=image,
                        hover_color="#388E3C",
                        fg_color="#A83232",
                        width=30,
                        height=30,
                        corner_radius=0,
                        command=lambda: print("Check button clicked"),
                    )
                    check_button.grid(row=0, column=0, sticky="e", padx=(50, 130))

                elif image_name == image_list[-1]:
                    font_button = ctk.CTkButton(
                        title_frame,
                        text=button_name,
                        image=image,
                        anchor='w',
                        fg_color="#A83232",
                        text_color="white",
                        font=("Arial", 20, "bold"),
                        hover=True,
                        corner_radius=0,
                        command=open_command
                    )
                    font_button.grid(row=0, column=0, sticky='w', padx=10)

            except FileNotFoundError:
                print(f"Error: Image not found - {image_name}")
            except Exception as e:
                print(f"An error occurred: {e}")

    def text_editor(self):
        self.font_size = 20
        self.text_box = ctk.CTkTextbox(
            self, text_color='black', fg_color="white",
            wrap="none", font=('Arial', self.font_size)
        )
        self.text_box.grid(row=1, column=0, pady=10, padx=10, sticky='nsew')

    def entry_box(self):
        entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        entry_frame.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
        entry_frame.columnconfigure((0, 1, 2, 3), weight=0)

        self.entry = ctk.CTkEntry(
            entry_frame, text_color='black', width=730,
            corner_radius=0, border_width=0,
            fg_color="#C4E3ED", font=("Arial", 15)
        )
        self.entry.grid(row=0, column=0, sticky='w')

        button_texts = ['<', '>', '<---']
        commands = [self.move_cursor_left, self.move_cursor_right, self.delete_last_char]
        button_position = [(20, 10), (10, 10), (10, 10)]
        
        for i, (text, cmd, position) in enumerate(zip(button_texts, commands, button_position), start=1):
            button = ctk.CTkButton(
                entry_frame, text=text, text_color='black',width=130,
                fg_color="#C4E3ED", corner_radius=0,
                font=("Arial", 15), command=cmd, 
            )
            button.grid(row=0, column=i, padx=position, sticky='e')

    def keyboard_frame(self):
        self.frame = ctk.CTkFrame(self, fg_color="#96ddf3", corner_radius=0)
        self.frame.grid(row=3, column=0, pady=10, padx=10, sticky='news')
        self.frame.columnconfigure(tuple(range(10)), weight=1)

        row1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        row2 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        row3 = ['', "A", "S", "D", "F", "G", "H", "J", "K", "L", '']
        row4 = ["CAPS", "Z", "X", "C", "V", "B", "N", "M", "Enter"]
        row5 = ['ABC', '123', 'YY', 'Space', 'Symbol']
        rows_data = [row1, row2, row3, row4, row5]

        for r_idx, keys in enumerate(rows_data):
            row_frame = ctk.CTkFrame(self.frame, fg_color="#96ddf3")
            row_frame.pack(fill="x", expand=True)
            row_frame.columnconfigure(tuple(range(len(keys))), weight=1)

            for c_idx, label in enumerate(keys):
                width = 20
                display_text = label
                padx = (10 if c_idx > 0 else 5)

                if label == '':
                    continue
                elif label in ["CAPS", "Enter"]:
                    width = 70
                elif label == "Space":
                    width = 300
                elif label == "Symbol":
                    width = 100
                elif label in ["ABC", '123', 'YY']:
                    width = 65

                button = ctk.CTkButton(
                    row_frame, text=display_text, width=width, height=40,
                    text_color='black', font=("Arial", 25),
                    fg_color="#C4E3ED", corner_radius=0
                )

                if label == "CAPS":
                    button.configure(fg_color='#A83232',command=self.toggle_caps)
                elif label == "Enter":
                    button.configure(fg_color='#A83232',command=lambda: self.text_box.insert(ctk.INSERT, '\n'))
                elif label == "Space":
                    button.configure(command=lambda: self.text_box.insert(ctk.INSERT, ' '))
                elif label == "ABC":
                    button.configure(command=lambda: self.parent.show_frame('language'))
                elif label in '123':
                    button.configure(text_color = '#A83232',command=lambda: self.parent.show_frame('number_setting'))
                elif label == 'YY':
                    button.configure(text_color = '#A83232',command=lambda: self.parent.show_frame('date_input_text'))
                elif label == 'Symbol':
                    button.configure(command=lambda: self.parent.show_frame('text_symbols'))
                elif label.isalpha() or label.isdigit():
                    button.configure(command=lambda t=label: self.on_button_press(t))

                button.grid(row=0, column=c_idx, padx=padx, pady=5, sticky="ew")
                self.buttons[label] = button

    def on_button_press(self, char):
        if char.isalpha():
            char = char.lower() if self.is_caps else char.upper()
        self.text_box.insert(ctk.INSERT, char)

    def toggle_caps(self):
        self.is_caps = not self.is_caps
        self.update_caps_buttons()

    def update_caps_buttons(self):
        excluded_keys = {"Enter", "Space", "ABC", "123", "YY", "Symbol"}

        for char, button in self.buttons.items():
            if char in excluded_keys:
                continue
            if char.isalpha():
                button.configure(text=char.lower() if self.is_caps else char.upper())

    def delete_last_char(self):
        current_text = self.text_box.index(ctk.INSERT)
        if current_text:
            self.text_box.delete(f"{current_text}-1c", ctk.INSERT)

    def move_cursor_left(self):
        current_text = self.text_box.index(ctk.INSERT)
        new_position = self.text_box.index(f"{current_text}-1c")
        self.text_box.mark_set(ctk.INSERT, new_position)

    def move_cursor_right(self):
        current_text = self.text_box.index(ctk.INSERT)
        new_position = self.text_box.index(f"{current_text}+1c")
        self.text_box.mark_set(ctk.INSERT, new_position)

    def number_button(self):
        print("123 or YY button clicked (customize behavior)")

    def abc_button(self):
        print("ABC button clicked (customize behavior)")
        

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

def create_text_symbol(parent, title, button_list, controller):
    frame = ctk.CTkFrame(parent, fg_color="white")
    
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=0)
    frame.rowconfigure(1, weight=1)

    create_title_frame(frame, title, controller)
    create_button_frame(frame, button_list)

    return frame

def create_title_frame(parent, title, close_command):
    frame = ctk.CTkFrame(parent, fg_color="#A83232", corner_radius=0)
    frame.grid(row=0, column=0, sticky="ew")
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=0)

    # Title Label
    title_label = ctk.CTkLabel(
            frame,text=title,fg_color="#A83232",
            anchor="center",text_color="white",font=("Arial", 20, "bold")
        )
    title_label.grid(row=0, column=0, pady=5, padx=0, sticky="new")

    # Load close icon
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "images", "close_icon.png")

        close_image = ctk.CTkImage(dark_image=Image.open(image_path), size=(20, 20))
        close_button = ctk.CTkButton(frame, text="", image=close_image,
            command=close_command, hover_color="#A83232", fg_color="#A83232",
            width=40, height=20, corner_radius=0)
        
        close_button.grid(row=0, column=0, padx=(0, 50), sticky="e")
        
    except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred loading close button: {e}")

def create_button_frame(parent, button_list):
    scroll = ctk.CTkScrollableFrame(parent, fg_color='white') #orientation="vertical",
    # scroll.columnconfigure((0), weight=1)
    # scroll.rowconfigure(0, weight=1)
    scroll.grid(row=1, column=0, pady=20, sticky='news')

    for indx, text in enumerate(button_list):
        row = indx // 18
        column = indx % 18
        btn = ctk.CTkButton(scroll, text=text,
                command=lambda lbl=text: clicked_button(lbl),  # Correct lambda binding
                corner_radius=0,height=50, width=50,
                fg_color="#FF00FF",
                text_color="black",
                font=("Arial", 15,))
        btn.grid(row=row, column=column,padx=6,pady=7)


def clicked_button(button_text):
    print(f"Button clicked: {button_text}")
    

def create_text_symbol_buttons():
    button_list = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', ':',
        '<', '=', '>', '?', '@', '℃', '[', '\\', ']', '^', '_', 'ʹ', '˝', '`', '͊', '‘', '’',
        '{', '|', '}', '~', '≃', '¥', '͞', '–', '·', '̌', '¨', '°', '¯', '‖', '⌈', '⌋', '…',
        '“', '”', '⟦', '⟧', '⟮', '⟯', '⟨', '⟩', '⟪', '⟫', '×', '÷', '±', '∧', '∨', '∑', 'π',
        '∷', '√', '⊙', '≡', '⍺', '≈', '≠', '⊥', '⌒', '≤', '≥', '˭', '★', '☆', '○', '●', '■',
        '□', '▲', '△', '←', '↑', '→', '↓', '™', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii',
        'viii', 'ix', 'x', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.',
        '11.', '12.', '13.', '14.', '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)',
        '(9)', '(10)', '(11)', '(12)', '(13)', '(14)', '(15)', '(16)', '(17)', '(18)',
        '(19)', '(20)', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '（一）','（二）','（三）',
        '（四）','（五）', '（六）', '（七）','（八）', '（九）', '（十）','Ⅰ', 'Ⅱ', 'Ⅲ',
        'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', '₢', '₱', '₹', 'Rs', '₨', '₣', '₤',
        '€', '£', '¥', '₿', 'ɸ', '⌀', 'ḍ'
    ]
    return button_list


def show_text_symbol(base_ref):
    buttons = create_text_symbol_buttons()
    base_ref.create_buttons(buttons)






