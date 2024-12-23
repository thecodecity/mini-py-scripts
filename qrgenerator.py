import qrcode
from PIL import Image, ImageDraw, ImageFilter
import customtkinter as ctk
from tkinter import filedialog

# **1. Artistic QR Code Generation**
def generate_qr_code(data, color="black", background="white", logo_path=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color=color, back_color=background).convert("RGBA")

    # Add logo if provided
    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")
        logo.thumbnail((qr_img.size[0] // 4, qr_img.size[1] // 4))
        
        # Paste logo at the center
        logo_pos = (
            (qr_img.size[0] - logo.size[0]) // 2,
            (qr_img.size[1] - logo.size[1]) // 2,
        )
        qr_img.paste(logo, logo_pos, logo)

    return qr_img

# **2. Save QR Code to File**
def save_qr_code(image, output_path="artistic_qr.png"):
    image.save(output_path)

# **3. GUI for QR Code Generator**
def browse_logo_image():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    logo_label.configure(text=f"Selected Logo: {logo_path}")

def create_qr_code():
    global logo_path
    data = data_entry.get()
    color = color_entry.get()
    background = background_entry.get()
    
    if not data:
        result_label.configure(text="Error: Please provide data for the QR code.")
        return
    
    qr_img = generate_qr_code(data, color=color, background=background, logo_path=logo_path)
    qr_img.save("artistic_qr.png")
    result_label.configure(text="QR code saved as 'artistic_qr.png'.")
    qr_img.show()

# Initialize customtkinter GUI
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Artistic QR Code Generator")
root.geometry("600x500")

# Title Label
title_label = ctk.CTkLabel(root, text="Artistic QR Code Generator", font=("Arial", 20))
title_label.pack(pady=10)

# Data Input Section
data_label = ctk.CTkLabel(root, text="Enter Data (Text/URL):")
data_label.pack(pady=5)
data_entry = ctk.CTkEntry(root, width=400)
data_entry.pack(pady=5)

# Color Customization
color_label = ctk.CTkLabel(root, text="QR Code Color (e.g., black, blue):")
color_label.pack(pady=5)
color_entry = ctk.CTkEntry(root, width=200)
color_entry.insert(0, "black")
color_entry.pack(pady=5)

background_label = ctk.CTkLabel(root, text="Background Color (e.g., white, yellow):")
background_label.pack(pady=5)
background_entry = ctk.CTkEntry(root, width=200)
background_entry.insert(0, "white")
background_entry.pack(pady=5)

# Logo Upload Section
logo_path = None
upload_logo_button = ctk.CTkButton(root, text="Upload Logo", command=browse_logo_image)
upload_logo_button.pack(pady=10)

logo_label = ctk.CTkLabel(root, text="Selected Logo: None")
logo_label.pack(pady=5)

# Generate QR Code Button
generate_button = ctk.CTkButton(root, text="Generate QR Code", command=create_qr_code)
generate_button.pack(pady=10)

# Result Label
result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=10)

# Run the Tkinter GUI
root.mainloop()
