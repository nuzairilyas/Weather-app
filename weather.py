import tkinter as tk
import requests
import time
from tkinter import PhotoImage
 
def getWeather(canvas):
  try:
      city = textField.get()
      api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7488737015aafb969b8f51329b765a5c"
    
      json_data = requests.get(api).json()
      condition = json_data['weather'][0]['main']
      temp = int(json_data['main']['temp'] - 273.15)
      min_temp = int(json_data['main']['temp_min'] - 273.15)
      max_temp = int(json_data['main']['temp_max'] - 273.15)
      pressure = json_data['main']['pressure']
      humidity = json_data['main']['humidity']
      wind = json_data['wind']['speed']
      sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
      sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

      final_info = condition + "\n" + str(temp) + "°C" 
      final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
  except:
        final_info = 'There was a problem '
        final_data = 'check your spelling'
  if city==("salman"):
    final_info = 'does not exist'
    final_data = 'better luck next time'

  label1.config(text = final_info)
  label2.config(text = final_data)


canvas = tk.Tk()
image_path=PhotoImage(file=r"C:\Users\salma\Downloads\weather-app-main\weather-app-main\landscape.png")
bg_image=tk.Label(canvas,image=image_path)
bg_image.place(relheight=1,relwidth=1)
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("ATC Elm", 30)
t = ("ATC Elm", 45)

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()