import requests
import json
from win32com.client import Dispatch
import time


city = input("Enter the name of the city: \n")

url = f"http://api.weatherapi.com/v1/current.json?key=e3ce6503bdf24f2a9e701950230104&q={city}"


r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

time.sleep(3)
speak = Dispatch("SAPI.SpVoice").Speak
speak(f"say 'THe current weather in {city} is {w} degrees'")






