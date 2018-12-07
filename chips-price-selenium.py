import time
from selenium import webdriver

def find_css(css):
    try:
        elem = driver.find_element_by_css_selector(css)
        print('Found <%s> element' % (elem.tag_name))
        type(elem)
        elem.click()
        time.sleep(10)
        print("Navigated!")
    except:
        print('Was not able to find <%s> element' % (elem.tag_name))

# not working
def find_iframe_css(css):
    try:
        iframe = driver.find_element_by_xpath("//iframe[@class='sl-frame']")
        driver.switch_to.frame(iframe)
        elem = driver.find_element_by_css_selector(css)
        print('Found <%s> element' % (elem.tag_name))
        type(elem)
        elem.click()
        time.sleep(10)
        print("Navigated!")
        driver.switch_to.default_content()
        print("Back to default frame")
    except:
        print('Was not able to find <%s> element' % (elem.tag_name))

def find_link_text(text):
    try:
        elem = driver.find_element_by_link_text(text)
        print('Found <%s> element' % (elem.tag_name))
        type(elem)
        elem.click()
        time.sleep(10)
        print("Navigated!")
    except:
        print('Was not able to find element')

driver = webdriver.Chrome('D:\\Dropbox\\Coding\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.realcanadiansuperstore.ca');
time.sleep(6) # Let the user actually see something!

# Select province
find_css('[data-province-code="CA-BC"]')
# Close modal
find_iframe_css('#closeButton')
# Select food category
find_css('[data-auid="food"] button')
# Select pantry category
find_css('[data-auid="pantry"] a')
# Select chips category
find_css('[data-category-code="RCSS001008011000"] a')
# Select potato chips category
find_css('[data-category-code="RCSS001008010001"] a')
# Select sort
find_css('li.item.btn-sort')
# Sort by popular
find_link_text('Top Sellers')

# Load pages
elem = driver.find_element_by_css_selector('div.row.row-currently-showing p')
total = elem.text[-3:]
print('Total items = ' + total)

# Fix types here
pages = int(total)/60
print('Pages = ' + pages)
page = 0
while page < pages:
    find_css('Load more')
print('Done loading')

# print("Quitting")
# driver.quit()

# steps
# https://www.realcanadiansuperstore.ca
# button
<# button class="select-province btn btn-primary" data-province-code="CA-BC" data-store-id="1520">British Columbia</button>


# orig
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()
