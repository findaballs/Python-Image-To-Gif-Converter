import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import sys

class ImageToGifConverter:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Image to GIF Converter")
        self.root.geometry("500x250")
        self.root.resizable(False, False)
        
        self.source_path = None
        
        self._setup_ui()
        
    def _setup_ui(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        self.lbl_instruction = tk.Label(
            main_frame, 
            text="Select an image to convert", 
            font=("Helvetica", 12)
        )
        self.lbl_instruction.pack(pady=(0, 15))
        
        self.lbl_path = tk.Label(
            main_frame, 
            text="No file selected", 
            fg="gray", 
            wraplength=450
        )
        self.lbl_path.pack(pady=(0, 20))
        
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=10)
        
        self.btn_select = tk.Button(
            btn_frame, 
            text="Browse Image", 
            command=self.select_image,
            height=2,
            width=20
        )
        self.btn_select.pack(side='left', padx=(0, 10), expand=True)
        
        self.btn_convert = tk.Button(
            btn_frame, 
            text="Convert to GIF", 
            command=self.convert_image,
            state='disabled',
            height=2,
            width=20,
            bg="#e1e1e1"
        )
        self.btn_convert.pack(side='right', padx=(10, 0), expand=True)
        
        self.status_bar = tk.Label(
            self.root, 
            text="Ready", 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def select_image(self):
        filetypes = (
            ('Images', '*.jpg *.jpeg *.png *.bmp *.tiff *.webp'),
            ('All files', '*.*')
        )
        
        filename = filedialog.askopenfilename(
            title="Open Image",
            initialdir=os.getcwd(),
            filetypes=filetypes
        )
        
        if filename:
            self.source_path = filename
            self.lbl_path.config(text=filename, fg="black")
            self.btn_convert.config(state='normal', bg="#4CAF50", fg="white")
            self.status_bar.config(text="Image loaded. Ready to convert.")

    def convert_image(self):
        if not self.source_path:
            return
            
        try:
            save_path = filedialog.asksaveasfilename(
                title="Save GIF",
                defaultextension=".gif",
                filetypes=(("GIF Image", "*.gif"),),
                initialfile=os.path.splitext(os.path.basename(self.source_path))[0] + ".gif"
            )
            
            if not save_path:
                return
                
            with Image.open(self.source_path) as img:
                self.status_bar.config(text="Converting...")
                self.root.update()
                
                rgb_img = img.convert('RGB')
                rgb_img.save(save_path, format='GIF')
                
            self.status_bar.config(text=f"Saved to: {save_path}")
            messagebox.showinfo("Success", "Image converted to GIF successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert image:\n{str(e)}")
            self.status_bar.config(text="Error occurred during conversion.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToGifConverter(root)
    root.mainloop()