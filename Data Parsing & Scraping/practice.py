# import requests 
# from bs4 import BeautifulSoup

# url = "https://webscraper.io/test-sites/e-commerce/allinone"

# r=requests.get(url)
# # print(r.text)

# soup = BeautifulSoup(r.text,"xml")
# print(soup)


# import requests 
# from bs4 import BeautifulSoup

# url = "https://webscraper.io/test-sites/e-commerce/allinone"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")

# product_titles = soup.select(".title")
# product_prices = soup.select(".price")

# with open("output.txt", "w", encoding="utf-8") as file:

#     for title, price in zip(product_titles, product_prices):

#         file.write(f"{title.text.strip()} - {price.text.strip()}\n")

# print("Data has been scraped and saved to 'output.txt'.")



