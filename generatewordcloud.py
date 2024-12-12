from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog, Button, Label, Text, END

# Generate word cloud
def generate_wordcloud():
    text = text_box.get("1.0", END).strip()
    if text:
        wc = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.show()

# Open a text file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_box.delete("1.0", END)
            text_box.insert(END, file.read())

# GUI Setup
root = Tk()
root.title("Word Cloud Generator")
root.geometry("500x400")

Label(root, text="Enter text below or upload a file:", font=("Arial", 12)).pack(pady=10)

text_box = Text(root, wrap='word', height=10)
text_box.pack(pady=10, padx=10, fill='both', expand=True)

Button(root, text="Generate Word Cloud", command=generate_wordcloud).pack(pady=10)
Button(root, text="Upload Text File", command=open_file).pack(pady=5)

root.mainloop()
