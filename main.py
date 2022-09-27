#!/usr/bin/env python

"""
A simple script to learn web scraping
Grab every 5-star book on the first 50 pages
"""

import requests
import bs4

source_site = "https://books.toscrape.com/catalogue/page-{}.html"
current_page = 1
input_pages = 0
current_book = 1
input_stars = 0
tot_stars = ""
book_list = []

while not 1 <= input_pages <= 50:
    input_pages = int(input("How many pages do you want to scrape? Enter 1-50: "))

while not 1 <= input_stars <= 5:
    input_stars = int(input("Filter by how many stars? Enter 1-5: "))
    if input_stars == 1:
        tot_stars = ".star-rating.One"
    if input_stars == 2:
        tot_stars = ".star-rating.Two"
    if input_stars == 3:
        tot_stars = ".star-rating.Three"
    if input_stars == 4:
        tot_stars = ".star-rating.Four"
    if input_stars == 5:
        tot_stars = ".star-rating.Five"

while 1 <= current_page <= input_pages:
    res = requests.get(source_site.format(current_page))
    soup = bs4.BeautifulSoup(res.text, "lxml")
    products = soup.select(".product_pod")

    while 0 <= current_book <= 19:
        this_book = products[current_book]
        if not this_book.select(tot_stars):
            pass
        else:
            found_book = str(this_book.select("a")[1]["title"])
            book_list.append(found_book)
            print(f"Found a 5-star book on page {current_page}! This title: {found_book}.")
        current_book += 1

    current_book = 0
    current_page += 1

print("\n".join(book_list))
