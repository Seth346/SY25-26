import requests
from bs4 import BeautifulSoup


def main_site():
    print("This is your BookScraper.")
    print("What price of book are you looking for?\n")

    try:
        low_price = float(input("Enter the starting price (ex: 5): "))
        high_price = float(input("Enter the ending price (ex: 20): "))
    except ValueError:
        print("Please enter numbers only.")
        return

    url = "http://books.toscrape.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    print("\nBooks in your price range:\n")

    found = False

    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        price = float(price_text[1:])

        if low_price <= price <= high_price:
            print(title, "-", price)
            found = True

    if not found:
        print("No books found in that range.")


main_site()