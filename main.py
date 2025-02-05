import tkinter as tk
import os
import qrcode
from datetime import datetime
from tkinter import filedialog
from PIL import Image, ImageTk


class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.label = tk.Label(root, text="Enter text or URL:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save QR Code", command=self.save_qr_code)
        self.save_button.pack()

        self.qr_code_image = tk.Label(root)
        self.qr_code_image.pack()

    def generate_qr_code(self):
        data = self.entry.get()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_code_img = img

        photo = ImageTk.PhotoImage(self.qr_code_img)

        self.qr_code_image.configure(image=photo)
        self.qr_code_image.image = photo

    def save_qr_code(self):
        current_datetime = datetime.now()
        file_name = (f"{current_datetime.day}_{current_datetime.month}_{current_datetime.year}_{current_datetime.hour}_"
                     f"{current_datetime.minute}.png")
        if hasattr(self, 'qr_code_img'):
            save_dir = filedialog.askdirectory()
            if save_dir:
                file_path = os.path.join(save_dir, file_name)
                self.qr_code_img.save(file_path)


if __name__ == "__main__":
    window = tk.Tk()
    qr_generator_app = QRCodeGenerator(window)
    window.mainloop()