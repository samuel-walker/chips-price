# Import requests, which we will use to get the raw HTML
import requests
import wget
# Import BeautifulSoup 4, which we will use to parse the HTML
from bs4 import BeautifulSoup
# Import csv module for writing data
import csv

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# Request HTML
url = "https://www.realcanadiansuperstore.ca/plp/RCSS001008010001?filters=&sort=popularity"
r = requests.get(url)

# Parse HTML
html = r.content
soup = BeautifulSoup(html, 'html.parser')
filename = wget.download(url)
soup = BeautifulSoup(filename, 'html.parser')

# Parse HTML
# with open("chips.html", "r", encoding="utf-8") as file:
with open("chips.html", "r", encoding="utf-8") as file:
    # Create BeautifulSoup object from HTML
    soup = BeautifulSoup(file, 'html.parser')

# Close HTML
file.close()

brand = soup.find_all("span", "js-product-entry-brand")

size = soup.find_all("span", "js-product-entry-size-detail")
unit_price = soup.find_all("span", "sale-qty")

length = len(name)

# Open CSV for writing
with open('chips.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["brand","name","size(g)","price","unit_price"])
    # Scrape product data
    for i in range(length):
        writer.writerow([brand[i].string[:-1],
                        name[i].string,
                        int(size[i].string[1:-3]),
                        float(int(size[i].string[1:-3])/100*float(unit_price[i].contents[2].strip()[1:5])),
                        float(unit_price[i].contents[2].strip()[1:5])])

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
