import requests
from bs4 import BeautifulSoup


def main_site():
    print("This is your BookScraper.")
    print("Searching ALL pages...\n")

    try:
        low_price = float(input("Enter the starting price (ex: 5): "))
        high_price = float(input("Enter the ending price (ex: 20): "))
    except ValueError:
        print("Please enter numbers only.")
        return

    page = 1
    found = False

    while True:
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)

        # stop when pages run out
        if response.status_code != 200:
            break

        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]

            price_text = book.find("p", class_="price_color").text
            price = float(price_text.replace("£", "").replace("Â", "").strip())

            rating = book.p["class"][1]

            if low_price <= price <= high_price and rating == "Five":
                print(title, "-", price)
                found = True

        page += 1

    if not found:
        print("No matching books found.")


main_site()