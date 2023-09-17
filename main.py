import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


location = "iran tehran"
location = location.split(" ")

URL = requests.get(f"https://www.timeanddate.com/weather/{location[0]}/{location[1]}")

webpage = BeautifulSoup(URL.content, "html.parser")

temp_div = webpage.find("div", class_="h2")
temperature = temp_div.text

upcoming_5hour_table = webpage.find("table", id="wt-5hr")
next_hours = np.array(upcoming_5hour_table.find("tr", class_=("h2")))
next_hours_temps = np.array(upcoming_5hour_table.find("tr", class_="h2 soft"))

next_hours_table = {}
for i in range(6):
    next_hours_table[next_hours[i][0]] = next_hours_temps[i][0].replace("\xa0", " ")

print(next_hours_table)

# Access Token: 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
# {'Now': '30 °C', '15:00': '30 °C', '16:00': '31 °C', '17:00': '31 °C', '18:00': '29 °C', '19:00': '28 °C'}
