import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def get_current_temp(webpage):

    temp_div = webpage.find("div", class_="h2")
    temperature = temp_div.text

    return temperature


def get_next_hours_temp(webpage):

    upcoming_5hour_table = webpage.find("table", id="wt-5hr")
    next_hours = np.array(upcoming_5hour_table.find("tr", class_=("h2")))
    next_hours_temps = np.array(upcoming_5hour_table.find("tr", class_="h2 soft"))

    next_hours_table = {}
    for i in range(6):
        next_hours_table[next_hours[i][0]] = next_hours_temps[i][0].replace("\xa0", " ")

    next_hours_df = pd.DataFrame(next_hours_table, index=[""])

    return next_hours_df


location = str(input("Enter your location(Suitable format: 'Country City'): "))
location = location.split(" ")

URL = requests.get(f"https://www.timeanddate.com/weather/{location[0]}/{location[1]}")

websitepage = BeautifulSoup(URL.content, "html.parser")

current_temp = get_current_temp(websitepage)
upcoming_hours_df = get_next_hours_temp(websitepage)

print(f"\nCurrent temperature for {location[1]}, {location[0]}: {current_temp} \n \nUpcoming 5 hours: \n {upcoming_hours_df}")


# Access Token: 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
