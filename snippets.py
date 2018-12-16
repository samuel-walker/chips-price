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


for i in range(length):
    writer.writerow([brand[i].string[:-1],
                    name[i].string,
                    int(size[i].string[1:-3]),
                    float(int(size[i].string[1:-3])/100*float(unit_price[i].contents[2].strip()[1:5])),
                    float(unit_price[i].contents[2].strip()[1:5])]


# Optional interactive ratings
# ratings = []
# # Loop through all chips
# for i, item in enumerate(name):
#     rating = input("Enter rating 1-10 for " + item + ": ")
#     print("Rating for " + item + ": " + rating)
#     ratings.append(rating)


# Plot 2

x = []
y = []
scale = []
label = []

with open('chips - sam.csv', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    next(csvFile, None)
    for row in plots:
        print(row)
        x.append(int(row[2]))
        y.append(float(row[3]))
        scale.append(int(row[5]) ** 3)
        label.append(str(row[0]) + " " + str(row[1]))

plt.scatter(x, y, s=scale, alpha=0.3)
plt.xlabel('Size (g)')
plt.ylabel('Price (CAD)')
plt.title('Chip price per gram')

plt.show()

# for i, label in enumerate(label):
#     plt.annotate(label, (x[i], y[i]))

plt.show()

# Plot 3

import mpld3

x = []
y = []
scale = []
label = []

fig, ax = plt.subplots()

with open('chips - sam.csv', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    next(csvFile, None)
    for row in plots:
        print(row)
        x.append(int(row[2]))
        y.append(float(row[3]))
        scale.append(int(row[5])*10)
        label.append(str(row[0]) + " " + str(row[1]))

scatter = ax.scatter(x, y, alpha=0.3, cmap=plt.cm.jet)
ax.grid(color='white', linestyle='solid')

ax.set_title("Scatter Plot (with tooltips!)", size=20)

tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=label)
mpld3.plugins.connect(fig, tooltip)

mpld3.show()

# Plot 4

import plotly.plotly as py

x = []
y = []
scale = []
label = []

py.sign_in('samuel-walker', 'Y7wwYrtAalINUBMfsgLR')

with open('chips - sam.csv', 'r') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')
    next(csvFile, None)
    for row in plots:
        print(row)
        x.append(float(row[4]))
        y.append(float(row[5]))
        scale.append(int(row[5]) ** 3)
        label.append(str(row[0]) + " " + str(row[1]))

area_scale, width_scale = 500, 5

fig, ax = plt.subplots()
sc = plt.scatter(x, y, s=scale, alpha=0.3)
plt.xlabel('Price per 100 g (CAD)')
plt.ylabel('Subjective Rating 1-10')
plt.title('Chip price per 100 g versus subjective taste rating, top 100-best selling chips, \nReal Canadian Superstore, December, 2018')

ax.grid()

plot_url = py.plot_mpl(fig)

# Using adjustText to move labels

# texts = [plt.text(x[i], y[i], label[i], fontsize=5) for i in range(len(x))]

# from adjustText import adjust_text
# adjust_text(texts)
# adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))
