#  Write a Python code snippet to extract all the hyperlinks (anchor tags) from a sample HTML webpage using Beautiful Soup. Explain how you would filter out external links from the extracted list.

from bs4 import BeautifulSoup 
import requests


url = "https://www.amazon.in/ref=nav_logo"
response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content,"html.parser")


all_links = soup.find_all('a')

for link in all_links:
    href = link.get('href')
    print(href)