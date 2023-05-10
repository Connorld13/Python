import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    # URL of the webpage
    url = 'http://books.toscrape.com/'

    # Sending a GET request
    response = requests.get(url)
    # Parsing the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding all book containers
    book_containers = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    # Lists to store scraped data
    titles = []
    prices = []
    availabilities = []
    ratings = []

    # Iterating over each book container
    for container in book_containers:
        # Scraping the book title
        title = container.h3.a['title']
        titles.append(title)

        # Scraping the book price
        price = container.find('p', class_='price_color').text
        prices.append(price)

        # Scraping the book availability
        availability = container.find('p', class_='instock availability').text.strip()
        availabilities.append(availability)

        # Scraping the book rating
        rating = 'Not rated'
        if container.p:
            rating = container.p['class'][1]
        ratings.append(rating)

    # Creating a pandas DataFrame
    books_df = pd.DataFrame({
        'Title': titles,
        'Price': prices,
        'Availability': availabilities,
        'Rating': ratings
    })

    # Printing the DataFrame
    print(books_df)

if __name__ == "__main__":
    scrape_books()
