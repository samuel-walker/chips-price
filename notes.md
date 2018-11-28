# Notes

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
