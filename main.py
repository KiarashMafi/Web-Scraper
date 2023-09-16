import requests
import numpy as np
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
print(len(next_hours_temps), len(next_hours))

next_hours_table = {}
for i in range(6):
    next_hours_table = {next_hours[i][0]: next_hours_temps[i][0]}

# Access Token: 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

