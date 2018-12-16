# Just manually downloaded the HTML

# Import BeautifulSoup 4, which we will use to parse the HTML
from bs4 import BeautifulSoup
# Import csv module for writing data
import csv

# Import matplotlib for plotting
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# Open manually-downloaded HTML
html = open('chips.html', 'r')
# Turn HTML into BS object
soup = BeautifulSoup(html, 'html.parser')

# NEW APPROACH

# To do: turn into dict
# Define empty lists
brands = []
names = []
prices = []
sizes = []
unit_prices = []
# Search through each product and add data to lists
for product in soup.find_all("div", "product-info"):
    # Get brand
    brand = product.find("span", "js-product-entry-brand")
    # Format brand
    if not brand:
        brand = ''
    else:
        brand = brand.string[:-1]
    brands.append(brand)
    # Get name
    name = product.find("span", "js-product-entry-name")
    # Format name
    name = name.string
    names.append(name)
    # Get price
    price = product.find("span", "reg-price-text")
    # Format price
    price = float(price.string.replace('$','').strip())
    prices.append(price)
    # Get size
    size = product.find("span", "js-product-entry-size-detail")
    # Format size
    size = size.string[1:-1].replace('g','').strip()
    # Check if it's a multipack, if so, multiply to get total weight
    if 'x' in size:
        pair = size.split('x')
        size = int(pair[0])*int(pair[1])
    else:
        size = int(size)
    sizes.append(size)
    unit_prices.append((price/size)*100)

# Get total number of items
length = len(names)

# Open CSV for writing
with open('chips.csv', 'w', newline='') as csvFile:
    # Create new writer object
    writer = csv.writer(csvFile)
    # Write header row
    writer.writerow(["brand","name","size(g)","price","unit_price"])
    # Write product data
    for i in range(length):
        writer.writerow([brands[i],names[i],sizes[i],prices[i],unit_prices[i]])

csvFile.close()

# Plot 1

x = []
y = []
scale = []
label = []

with open('chips - sam - 100.csv', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    next(csvFile, None)
    for row in plots:
        print(row)
        x.append(float(row[4]))
        y.append(float(row[5]))
        scale.append(int(row[5]) ** 3)
        label.append(str(row[0]) + " " + str(row[1]))

x = np.asarray(x)
y = np.asarray(y)

plt.scatter(x, y, alpha=0.3)
plt.xlabel('Price per 100 g (CAD)')
plt.ylabel('Subjective Rating 1-10')
plt.title('Chip price per 100 g versus subjective taste rating, top 100 best-selling chips, \nReal Canadian Superstore, December 16, 2018')

plt.savefig('chart.png', dpi=300)
plt.show()
