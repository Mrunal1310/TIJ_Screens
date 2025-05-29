import customtkinter as ctk
from PIL import Image
import os

class FileScreen(ctk.CTkFrame):
    def __init__(self, parent, go_home_callback):
        super().__init__(parent)
        
        self.configure(fg_color="white")
        self.go_home_callback = go_home_callback
        
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.rowconfigure((0), weight=0)
        self.rowconfigure((1), weight=1)
        
        self.title_frame()
        self.button_frame()
        self.display_frame()
        
    def title_frame(self):
        self.frame=ctk.CTkFrame(self, fg_color="#A83232", corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.grid(row=0, column=0, columnspan=2, sticky="new")
        
        self.label=ctk.CTkLabel(self.frame, text="File list",  fg_color="#A83232", corner_radius=0, anchor='center',text_color="white",font=("Arial", 20, 'bold'))
        self.label.grid(row=0, column=0, pady=5, padx=0,)
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir="images\\"
        image_path = os.path.join(image_dir, "multiple_choice_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.multiple_button=ctk.CTkButton(self.frame, text="Multiple Choice", image=image, fg_color="#A83232", corner_radius=0, anchor='w',text_color="white",font=("Arial", 20, 'bold'))
            self.multiple_button.grid(row=0, column=0, pady=5, padx=5, sticky="w")
            image.close()
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
        image_dir="images\\"
        image_path = os.path.join(image_dir, "close_icon.png")
        
        try:
            image=ctk.CTkImage(dark_image=Image.open(image_path))
            self.close_button=ctk.CTkButton(self.frame, text="", image=image, command=self.go_home_callback, hover=False, fg_color="#A83232",bg_color="#A83232",width=50, height=20, corner_radius=0)
            self.close_button.grid(row=0, column=0, sticky='e')
            image.close()
            
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def button_frame(self):
        
        self.frame=ctk.CTkFrame(self, fg_color="white",border_width=2, corner_radius=0,)
        self.frame.columnconfigure((0), weight=1)
        self.frame.rowconfigure((0,1,), weight=0)
        self.frame.grid(row=1, column=0,pady=10,padx=10, sticky="news")
        
        self.button_list=["Test file" ]
        
        for index, text in enumerate(self.button_list):
            button = ctk.CTkButton(self.frame, text=text, text_color="black", anchor="w", command=lambda t=text: self.system_button(t),
                                    fg_color="white", hover_color="#FF00FF", font=("Arial", 20,), corner_radius=0)
            button.grid(row=index + 1, column=0, padx=10, pady=5, sticky="news")
        
        
    def display_frame(self):
        
        self.frame=ctk.CTkFrame(self, fg_color="white",corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0,1,), weight=1)
        self.frame.grid(row=1, column=1, padx=5,pady=10, sticky="news")
        
        self.entry=ctk.CTkEntry(self.frame, placeholder_text="",height=40, corner_radius=10, border_width=1, border_color="black", ) 
        self.entry.grid(row=0, column=0,padx=5, pady=(30, 0), sticky='ew')
        
        self.format_butn=ctk.CTkButton(self.frame, text="Delete", text_color="white",fg_color="#A83232",font=("Arial", 22,),corner_radius=0, command=self.open_warnings )
        self.format_butn.grid(row=1, column=0, padx=10, pady=50, sticky="es")
        
        self.open_butn=ctk.CTkButton(self.frame, text="Open",  text_color="white",fg_color="#A83232", font=("Arial", 22,), corner_radius=0,)
        self.open_butn.grid(row=1, column=0, padx=10,pady=10,sticky="es")
        
        self.label=ctk.CTkLabel(self.frame, text="", font=('Arial', 18), anchor='nw',text_color="black", height=150,fg_color="#C4E3ED")
        self.label.grid(row=0, column=0,padx=5, pady=5, sticky="new")
        
    def open_warnings(self):
        self.warning=ctk.CTkToplevel(self)  
        self.warning.title("Warning")
        self.warning.geometry("450x150")  
        self.warning.resizable(False, False)  
        
        self.warning.transient(self)  
        self.warning.grab_set()       
        self.warning.focus_force() 
        
        self.frame=ctk.CTkFrame(self.warning,fg_color="white",width=450,height=150, corner_radius=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0,1,2,3),weight=1)
        self.frame.grid(row=0, column=0, sticky="news")
        
        self.label=ctk.CTkLabel(self.frame, text="Warning",text_color="white", fg_color="#A83232",width=450, anchor="w",font=("Arial", 18, 'bold'))
        self.label.grid(row=0, column=0, sticky="news")
        
        self.label=ctk.CTkLabel(self.frame, text="Test file",text_color="black", fg_color="white", anchor="w", font=("Arial", 16,))
        self.label.grid(row=1, column=0, padx=10,pady=5,sticky="news")
        
        self.label=ctk.CTkLabel(self.frame, text="\nDelete?",text_color="black", fg_color="white", anchor="w", font=("Arial", 16,))
        self.label.grid(row=2, column=0, padx=10,pady=0,sticky="news")
        
        self.button=ctk.CTkButton(self.frame, text="OK",text_color="black",anchor="center", fg_color="white",border_width=1,corner_radius=0,command=self.warning.destroy, font=("Arial", 16,))
        self.button.grid(row=3, column=0, padx=40, pady=10,sticky="w")
        
        self.button=ctk.CTkButton(self.frame, text="Back",text_color="black", anchor="center",fg_color="white",border_width=1,corner_radius=0,command=self.warning.destroy, font=("Arial", 16,))
        self.button.grid(row=3, column=0, padx=60, pady=10,sticky="e")
        
        
    def system_button(self, text):
        if text == "Test file":
            self.label.configure(text="Test file\n26.9KB\nFile\n2023-07-27 12:00:00")
        
# def main():
#     root=ctk.CTk()
#     app=FileList(root)
#     root.mainloop()
    
# if __name__=="__main__":
#     main()
    
# Adding of serach bar icon is remaining