import requests
from tkinter import Tk, Label, Entry, Canvas, StringVar
from tkinter.ttk import Style, Frame, Button, Label as TtkLabel
from PIL import Image, ImageTk

API_KEY = '3434037233ac86f7ad772ec6f5892e4a'

def get_weather():
    city = entry_var.get()
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    weather = response.json()

    if response.status_code == 200:
        temp = weather['main']['temp']
        description = weather['weather'][0]['description'].capitalize()
        icon_code = weather['weather'][0]['icon']
        
        # Update weather result label
        result_var.set(f"{city.title()}: {temp}°C, {description}")

        # Load weather icon
        icon_response = requests.get(f"http://openweathermap.org/img/wn/{icon_code}@2x.png", stream=True)
        if icon_response.status_code == 200:
            icon_data = Image.open(icon_response.raw)
            icon_image = ImageTk.PhotoImage(icon_data)
            icon_label.config(image=icon_image)
            icon_label.image = icon_image
    else:
        result_var.set("Error: City not found")

# Create the main window
root = Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#f5f5f5")

# Style configuration
style = Style()
style.configure("TFrame", background="#ffffff", padding=10)
style.configure("TButton", font=("Roboto", 12), padding=5)
style.configure("TLabel", background="#f5f5f5", font=("Roboto", 14))

# Main frame
frame = Frame(root, style="TFrame")
frame.pack(expand=True, fill="both", padx=10, pady=10)

# City entry and button
TtkLabel(frame, text="Enter City:", font=("Roboto", 16), background="#ffffff").pack(pady=5)
entry_var = StringVar()
entry = Entry(frame, textvariable=entry_var, font=("Roboto", 14), width=25)
entry.pack(pady=5)
Button(frame, text="Get Weather", command=get_weather, style="TButton").pack(pady=10)

# Weather result and icon
result_var = StringVar()
result_label = TtkLabel(frame, textvariable=result_var, font=("Roboto", 16), background="#ffffff", wraplength=300)
result_label.pack(pady=10)

icon_label = Label(frame, bg="#ffffff")
icon_label.pack(pady=10)

# Placeholder for icons
TtkLabel(frame, text="Temperature Trends", font=("Roboto", 14), background="#ffffff").pack(pady=10)
graph_canvas = Canvas(frame, width=300, height=100, bg="#e0e0e0", highlightthickness=0)
graph_canvas.pack(pady=10)

# Start the main loop
root.mainloop()