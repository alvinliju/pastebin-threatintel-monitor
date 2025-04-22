import requests
from bs4 import BeautifulSoup
import re

url = "https://pastebin.com/archive"


response = requests.get(url)

html_content = response.text;

soup = BeautifulSoup(html_content, "html.parser");
all_the_hrefs = soup.find_all("a", class_=False)
i=0
for href in all_the_hrefs:
     if href['href'] == '/': break 	
     i += 1
     if i>3: print(href)
		


