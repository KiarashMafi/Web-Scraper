import re
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
next_hours_temps = list(upcoming_5hour_table.find("tr", class_="h2 soft").text)

# next_hours_temps = next_hours_temps.decode("utf-8")
# next_hours_temps = re.findall(r"\d+", next_hours_temps)

print(next_hours_temps)



# Result: ['3', '0', '\xa0', '°', 'C', '3', '0', '\xa0', '°', 'C', '2', '8', '\xa0', '°', 'C', '2', '8', '\xa0', '°', 'C', '2', '6', '\xa0', '°', 'C', '2', '6', '\xa0', '°', 'C']
# Access Token: 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

