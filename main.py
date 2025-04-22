import requests
from bs4 import BeautifulSoup
import re
import json


def check_post(atag):
        id = atag['href']
        url = f'https://pastebin.com/{id}'
        response = requests.get(url)
        raw_content = response.text;
        is_there_anything_valuable(raw_content, atag)



def is_there_anything_valuable(raw_content, atag):
        pattern = "[^@]+@[^@]+\.[^@]+"
        x = re.search(pattern, raw_content)

        if x:
          print(f"YES! We have a match!, {atag['href']}")
        else:
          print("No match")




url = "https://pastebin.com/archive"


response = requests.get(url)

html_content = response.text;

parsed_atags = []


soup = BeautifulSoup(html_content, "html.parser");
all_the_atags = soup.find_all("a", class_=False)
i=0
for atag in all_the_atags:
     if atag['href'] == '/': break 	
     i += 1
     if i>3: check_post(atag)



