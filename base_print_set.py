import customtkinter as ctk
from PIL import Image
import os

class BaseScreen(ctk.CTkFrame):  
    def __init__(self, parent, title, button_labels, close_command):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="both", expand=True)

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(1, weight=1)

        self.create_title_frame(title, close_command)
        self.create_left_content(button_labels)
        self.create_right_content()

    def create_title_frame(self, title, command):
        self.title_frame = ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky="new")

        self.title_label = ctk.CTkLabel(
            self.title_frame,text=title,fg_color="#A83232",
            anchor="center",text_color="white",font=("Arial", 20, "bold")
        )
        self.title_label.grid(row=0, column=0, pady=5, padx=0, sticky="new")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "images", "close_icon.png")

        try:
            image = ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button = ctk.CTkButton(
                self.title_frame,text="", image=image,
                command=command,hover_color="#A83232",fg_color="#A83232",
            )
            self.close_button.grid(row=0, column=0, sticky="e", padx=10)
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_left_content(self, button_labels):
        self.left_content = ctk.CTkFrame(self, fg_color="#C4E3ED", corner_radius=0)
        self.left_content.columnconfigure(0, weight=1)
        self.left_content.grid(row=1, column=0, sticky='news')

        self.create_buttons(button_labels)

    def create_buttons(self, button_labels):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(script_dir, "images")

        for index, (text, icon, command) in enumerate(button_labels):
            image_path = os.path.join(image_dir, icon)
            try:
                image = ctk.CTkImage(dark_image=Image.open(image_path), size=(25, 25))
                button = ctk.CTkButton(
                    self.left_content,font=("Arial", 20),corner_radius=0,command=command,
                    text=text,anchor="w",height=100,width=200,image=image, hover_color="#FF00FF",
                    compound="left",text_color="black",fg_color="#C4E3ED",
                )
                button.grid(row=index, column=0, sticky="news")
            except FileNotFoundError:
                print(f"Error: Image not found at {image_path}")
            except Exception as e:
                print(f"An error occurred while creating button '{text}': {e}")

    def create_right_content(self):
        self.right_content = ctk.CTkFrame(self, fg_color='white', corner_radius=0)
        self.right_content.grid(row=1, column=1, sticky='news')
        self.right_content.columnconfigure(0, weight=1)
        
        
    def add_label_switch(self, text, row, col_label=0, col_switch=0, command=None):
        label = ctk.CTkLabel(self.right_content, text=text, text_color='black', font=("Arial", 20), fg_color="white")
        label.grid(row=row, column=col_label, padx=10, pady=(20, 25), sticky='w')

        switch_var = ctk.StringVar(value='off')
        switch = ctk.CTkSwitch(self.right_content, variable=switch_var, font=("Arial", 20), command=command)
        switch.grid(row=row, column=col_switch, padx=10, pady=(20, 25), sticky='e')

        return switch_var
    
    def add_button_with_arrow(self, text, row, col_button=0, col_arrow=0, command = None):
        button = ctk.CTkButton(self.right_content, text=text,text_color='black',font=("Arial", 20),fg_color="white",anchor='w', command = command)
        button.grid(row=row, column=col_button, padx=10, pady=(20, 25), sticky='w')
        
        arrow = ctk.CTkLabel(self.right_content, text=">",text_color='black', font=("Arial", 20),fg_color="white",)
        arrow.grid(row=row, column=col_arrow, padx=10, pady=(20, 25), sticky='e')

    def clear_right_content(self):
        for widget in self.right_content.winfo_children():
            widget.destroy()
            
    def clear_left_content(self):
        for widget in self.left_content.winfo_children():
            widget.destroy()
            
    def update_left_content(self, new_button_labels):
        self.clear_left_content()  # Clear existing buttons
        self.create_buttons(new_button_labels) 
