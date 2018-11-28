# Print HTML if you want
print(soup.prettify())
# Write HTML to file if you want
with open("index.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# Old requests attempts
r = requests.get('https://shop.saveonfoods.com/store/AC5D1198#/category/589,732/chips%20%26%20pretzels')
r = requests.get('https://www.realcanadiansuperstore.ca/Food/Pantry/Chips-%26-Salty-Snacks/Potato-Chips/plp/RCSS001008010001?filters=&sort=popularity')

# Old wget attempts
filename = wget.download(url)
soup = BeautifulSoup(filename, 'html.parser')

# Parse HTML from local file
# with open("chips.html", "r", encoding="utf-8") as file:
with open("chips.html", "r", encoding="utf-8") as file:
    # Create BeautifulSoup object from HTML
    soup = BeautifulSoup(file, 'html.parser')
