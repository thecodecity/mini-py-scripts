import requests
from tkinter import Tk, Label, Entry, Button

API_KEY = '3434037233ac86f7ad772ec6f5892e4a'

def get_weather():
    city = entry.get()
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    weather = response.json()
    print(weather)
    result = f"{city.title()}: {weather['main']['temp']}°C, {weather['weather'][0]['description']}"
    label_result.config(text=result)

root = Tk()
Label(root, text="Enter City:").pack()
entry = Entry(root, width=20)
entry.pack()
Button(root, text="Get Weather", command=get_weather).pack()
label_result = Label(root, text="", font=("Helvetica", 12))
label_result.pack()
root.mainloop()
