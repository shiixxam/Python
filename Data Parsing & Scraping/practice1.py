

import requests

def fetch_and_save_to_file(url,file_path ):
    r = requests.get(url)
    if r.encoding != 'UTF-8':
        r.encoding = 'UTF-8'  

    with open(file_path, "w", encoding='utf-8') as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/"
file_path = r"B:\python learning\Data Parsing & Scraping\times.html"

fetch_and_save_to_file(url, file_path)
