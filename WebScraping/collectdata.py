
import requests
from bs4 import BeautifulSoup

page = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
soup = BeautifulSoup(page.content,"html.parser")

#print(soup.prettify())
header2 = (soup.find_all("h2"))

print(header2[0].text)
