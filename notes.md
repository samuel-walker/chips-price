# Notes

# Reflection

My ultimate goal was to create a script to pull live chip data and calculate unit prices, then let the user rate them, then plot the results to show the best value based on taste. This ended up being too much, for a number of reasons. The main one was scraping the grocery sites, which used AJAX and JS and iframes, was too annoying.

So in the end I skipped the scraping and downloaded an extract instead. Then I just

# HTTP Calls to Real Canadian Superstore

data-ajax-url="/plp/RCSS001008010001?loadMore=true&sort=popularity&filters="

https://www.realcanadiansuperstore.ca/Food/Pantry/Chips-%26-Salty-Snacks/Potato-Chips/plp/RCSS001008010001?loadMore=true&sort=popularity

**First 60**

**60-119**
https://www.realcanadiansuperstore.ca/plp/RCSS001008010001?loadMore=true&sort=popularity&filters=&itemsLoadedonPage=60&_=1543385773997

**120-180**
https://www.realcanadiansuperstore.ca/plp/RCSS001008010001?loadMore=true&sort=popularity&filters=&itemsLoadedonPage=120&_=1543385773997

So itemsLoadedonPage says how many are already loaded on the page, this returns the next 60.
So if I grab the total using bs on the first request, I can figure out how many subsequent ones to make. If <60 on page it just returns the remaining ones.
Then do that
Combine them
Etc.

# Improvements

- Create functions
  - Could do one for formatting that sends the ResultSet and type to determine how it is formatted

# Save On

## Second approach

Again some cookie/js/ajax issues.

Try directly querying API for JSON, e.g.
https://shop.saveonfoods.com/api/product/v7/products/category/996/store/B1801094?sort=Brand&skip=0&take=20&userId=ec3e9292-8c1d-4ea9-99c6-e9af7ef40f3a
https://shop.saveonfoods.com/api/product/v7/products/category/996/store/AC5D1198?sort=Brand&skip=0&take=20&userId=b5f9afe1-68d2-4ca5-a1ec-597e5892b62e

## First approach

Get # pages from last a (or li) in nav.paging
Iterate on pages after potato/n

photo = li.productList__product img
name = li.productList__product h3
size = span.productInfo__size (contains "6 pack" etc.)
price = span.priceInfo__price priceInfo__price--current

https://shop.saveonfoods.com/store/B1801094#/category/589,732,996/chips%20-%20potato/1?queries=sort%3DBrand
https://shop.saveonfoods.com/store/B1801094#/category/589,732,996/chips%20-%20potato/2?queries=sort%3DBrand

https://automatetheboringstuff.com/chapter11/
http://chromedriver.chromium.org/getting-started
https://stackoverflow.com/questions/13960326/how-can-i-parse-a-website-using-selenium-and-beautifulsoup-in-python
