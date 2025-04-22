import requests
from bs4 import BeautifulSoup


url = "https://pastebin.com/archive"


response = requests.get(url)

html_content = response.text;

soup = BeautifulSoup(html_content, "html.parser");
all_the_hrefs = soup.find_all("a")

print(all_the_hrefs)

