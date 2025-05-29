import customtkinter as ctk
from PIL import Image
import os

# def main_window(label_text):  # Changed parameter name to label_text
#     root = ctk.CTk()
#     root.title("Main Window")
#     root.geometry("300x100")
    
#     button = ctk.CTkButton(root, text="Open Popup", command=lambda: open_popup_box(root, label_text))  # Pass label_text
#     button.pack(padx=20, pady=30)
    
#     root.mainloop()

def open_popup_box(label_text):  # Added label_text as parameter
    popup_box = ctk.CTkToplevel()  
    popup_box.title("Popup")
    popup_box.geometry("450x300")  
    popup_box.resizable(False, False) 
    
    # Ensure the pop-up appears on top of the root window
    popup_box.transient()  
    popup_box.grab_set()       
    popup_box.focus_force()
    
    title_label(popup_box, label_text)  # Pass label_text here
    
def title_label(popup_box, label_text):  # Renamed parameter to label_text
    # Title label 
    label = ctk.CTkLabel(popup_box, text=label_text, width=450, height=30, fg_color="#A83232", text_color="white", font=("Arial", 20, 'bold'))
    label.grid(row=0, column=0, columnspan=4)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
    image_dir = "images\\"
    image_path = os.path.join(image_dir, "close_icon.png")
    
    # Close Button Icon
    try:
        image = ctk.CTkImage(dark_image=Image.open(image_path))
        close_button = ctk.CTkButton(popup_box, text="", image=image, command=popup_box.destroy, 
                                    hover_color="#A83232", fg_color="#A83232",
                                    width=50, height=30, corner_radius=0)
        close_button.grid(row=0, column=0, columnspan=4, sticky='e')
        
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    entry = ctk.CTkEntry(popup_box, fg_color="#96ddf3", height=50, justify="center", corner_radius=0, border_width=0, font=("Arial", 22, 'bold'))
    entry.grid(row=1, column=0, columnspan=4, padx=10, pady=20, sticky="news")
    
    create_buttons(popup_box, entry)
    
def create_buttons(popup_box, entry):
    # Button label list
    button_texts = [
        "0", "1", "2", "3",
        "4", "5", "6", "7",
        "8", "9", "<--", "OK"
    ]
    
    # For loop to arrange buttons 
    for i, text in enumerate(button_texts):
        row = i // 4
        col = i % 4
        button = ctk.CTkButton(popup_box, text=text, fg_color="#C4E3ED", width=80, height=40, 
                                corner_radius=0, text_color="black", font=("Arial", 18),
                                command=lambda value=text: click_button(value, entry))
        button.grid(row=row + 2, column=col, padx=10, pady=10, sticky="news")
        
def click_button(text, entry):
    current_value = entry.get()
    if text == "<--":
        entry.delete(len(current_value) - 1, 'end')     
    elif text == "OK":
        print(f'Entered value: {current_value}')
    else:
        entry.insert('end', text)
        

    