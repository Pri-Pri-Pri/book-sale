import requests
from bs4 import BeautifulSoup

request = requests.get("http://shop.nplusonemag.com/collections/featured/products/social-medium-artists-writing-2000-2015")
content = request.content
soup = BeautifulSoup(content, "html.parser")

def get_book_price():
    '''Find out when the book you want to buy is on sale.'''
    
    # <h1 class="title" itemprop="name">Social Medium: Artists Writing, 2000–2015</h1>
    book_title = soup.find("h1", {"class": "title", "itemprop": "name"})
    string_title = book_title.text.strip()

    # <h2 class="price" id="price-preview">$28.00</h2>
    book_price = soup.find("h2", {"class": "price", "id": "price-preview"})
    string_price = book_price.text.strip() # "$28.00"

    price_without_sign = string_price[1:] # "28.00"
    price = (float(price_without_sign))

    if price < 22:
        print("Hey, *{}* is on sale!".format(string_title))
        print("It's now {}.".format(string_price))
    else:
        print("Sit tight, *{}* isn't on sale yet.".format(string_title))
        print("It's still {}.".format(string_price))

get_book_price()
