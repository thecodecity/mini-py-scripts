from transformers import BlipProcessor, BlipForConditionalGeneration
from tkinter import Tk, filedialog, Label, Button
from PIL import Image, ImageTk

# Load pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate captions
def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs)
    return processor.decode(outputs[0], skip_special_tokens=True)

# Function to handle image upload
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        caption = generate_caption(file_path)
        img = Image.open(file_path).resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        image_label.configure(image=img_tk)
        image_label.image = img_tk
        caption_label.config(text=f"Caption: {caption}")

# GUI Setup
root = Tk()
root.title("Image Caption Generator")
root.geometry("400x500")

Label(root, text="Upload an Image to Generate a Caption", font=("Arial", 14)).pack(pady=10)

image_label = Label(root)
image_label.pack(pady=10)

Button(root, text="Upload Image", command=upload_image).pack(pady=10)

caption_label = Label(root, text="", wraplength=350, font=("Arial", 12))
caption_label.pack(pady=20)

root.mainloop()