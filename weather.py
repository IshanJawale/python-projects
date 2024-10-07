from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather App")
root.iconbitmap('gojo.ico')
root.geometry("400x200")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=E54C7DB9-ABB6-435B-8186-35723D45184D

def ziplookup():
    
    pin = zip.get()
    try:
        
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(pin) + "&distance=5&API_KEY=E54C7DB9-ABB6-435B-8186-35723D45184D")
        api = json.loads(api_request.content)
        area = api[0]['ReportingArea']
        aqi = api[0]['AQI']
        name = api[0]['Category']['Name']

        if name == "Good":
            weather_colour = "#0C0"
        elif name == "Moderate":
            weather_colour = "#FFFF00"
        elif name == "Unhealthy for Sensitive Groups":
            weather_colour = "#ff9900"
        elif name == "Unhealthy":
            weather_colour = "#FF0000"
        elif name == "Very Unhealthy":
            weather_colour = "#990066"
        elif name == "Hazardous":
            weather_colour = "#660000"

        root.configure(background=weather_colour)
        Label(root, text=str(area) + " " + str(aqi) + " " + str(name), background=weather_colour).pack()
    except Exception as e:
        api = "Error..."





zip = Entry(root)
zip.pack()
zipButton = Button(root, text="Lookup zipcode", command=ziplookup)
zipButton.pack()
root.mainloop()