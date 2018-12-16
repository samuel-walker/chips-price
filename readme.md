# chips-price

So ages ago I mentioned to my friends that to be a real chip connoisseur, you have to weigh taste versus unit price. This is a better way to do it than worrying about how much air there is in the bag. So, after way too much time, I figured out how to get chip price and weight data from the Real Canadian Superstore website, rated the top 100, and then made this chart!

My ultimate goal was to create a script to pull live chip data and calculate unit prices, then let the user rate them, then plot the results to show the best value based on taste. This ended up being too much, for a number of reasons. The main one was scraping the grocery sites, which used AJAX and JS and iframes, was too annoying.

So in the end I skipped the scraping and downloaded an extract instead. Then I did some manual data wrangling in Excel and then used matplotlib to create the chart.

If I have time in the future, I'll clean this up and use plot.ly or a similar service to make it more interactive.
