# Not working because I can't figure out how to get the right store to load.

# Import requests, which we will use to get the raw HTML
import requests
# Import BeautifulSoup 4, which we will use to parse the HTML
from bs4 import BeautifulSoup
# Import csv module for writing data
import csv

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# Request HTML
# Could add category request here
# url = "https://www.realcanadiansuperstore.ca/plp/RCSS001008010001?filters=&sort=popularity"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

url = "https://www.realcanadiansuperstore.ca/plp/RCSS001008010001?sort=popularity&filters=&itemsLoadedonPage=60&_=1543385773997"

r = requests.get(url, headers=headers, allow_redirects=True)
open('chips.html', 'wb').write(r.content)

# Issue is it is just not loading the right HTML.

# Turn HTML into BS object
html = r.content
soup = BeautifulSoup(html, 'html.parser')

# Get chip attributes from HTML
# Get brand
brand = soup.find_all("span", "js-product-entry-brand")
# Format brand
for i, item in enumerate(brand):
    # Remove () and g, strip
    brand[i] = item.string[:-1]

# Get name
name = soup.find_all("span", "js-product-entry-name")
# Format name
for i, item in enumerate(name):
    # Remove () and g, strip
    name[i] = item.string

# Get size
size = soup.find_all("span", "js-product-entry-size-detail")
# Format size
for i, item in enumerate(size):
    # Remove () and g, strip
    size[i] = item.string[1:-1].replace('g','').strip()
    # Check if it's a multipack, if so, multiply to get total weight
    if 'x' in size[i]:
        pair = size[i].split('x')
        size[i] = int(pair[0])*int(pair[1])
    else:
        size[i] = int(size[i])

# Get price
price = soup.find_all("span", "reg-price-text")
# Format price
for i, item in enumerate(price):
    # Remove () and g, strip
    price[i] = float(item.string.replace('$','').strip())

# Get unit price (could try with list comprehension)
unit_price = []
for i in range(len(price)):
    unit_price.append((size[i]/100)*price[i])

# Get total number of items
length = len(name)

# div row row-currently-showing = contains total items in a <p>

# Open CSV for writing
with open('chips.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["brand","name","size(g)","price","unit_price"])
    # Scrape product data
    for i in range(length):
        writer.writerow([brand[i],name[i],size[i],price[i],unit_price[i]])

csvFile.close()

x = []
y = []
label = []

with open('chips.csv', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    next(csvFile, None)
    for row in plots:
        print(row)
        x.append(int(row[2]))
        y.append(float(row[3]))
        label.append(str(row[1]))

plt.plot(x,y, 'o')
plt.xlabel('Size (g)')
plt.ylabel('Price (CAD)')
plt.title('Chip price per gram')

for i, label in enumerate(label):
    plt.annotate(label, (x[i], y[i]))

plt.show()
