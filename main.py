import requests
from bs4 import BeautifulSoup


location = "iran tehran"
location = location.split(" ")
URL = requests.get(f"https://www.timeanddate.com/weather/{location[0]}/{location[1]}")














# Access Token: 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

