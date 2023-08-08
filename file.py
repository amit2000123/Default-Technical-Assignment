from bs4 import BeautifulSoup
import csv

# Read and parse the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

# Open the CSV file for writing
with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'Price', 'Rating'])

    for div in divs:
        # Find the title
        title_elem = div.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4')
        title = title_elem.text if title_elem else ''

        # Find the price
        price_elem = div.find('span', class_='a-price')
        price = price_elem.text if price_elem else ''

        # Find the rating
        rating_elem = div.find('div', class_='a-row a-size-small')
        rating = rating_elem.text if rating_elem else ''

        # Write the data to the CSV file
        csvwriter.writerow([title, price, rating])

print("Data has been written to amazon_products.csv")
