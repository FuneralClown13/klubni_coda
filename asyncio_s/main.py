from tkinter import *
from tkinter import ttk
from weather import weather
from get_cities_list import get_cities_list
import re


def get_weather(city_key):
    try:
        city_and_weather.set('\n'.join([city for city in weather(city_key) if city]))
    except:
        print('error')
    return city_key is not None


root = Tk()
root.title("GETWEATHER")
root.geometry("250x250")

check = (root.register(get_weather), "%P")

city_and_weather = StringVar()

city_name = ttk.Entry(validate="key", validatecommand=check)
city_name.pack(padx=50, pady=5, anchor=NW)

city_weather = ttk.Label(foreground="black", textvariable=city_and_weather, wraplength=250)
city_weather.pack(padx=5, pady=5, anchor=NW)

if __name__ == '__main__':
    root.mainloop()
