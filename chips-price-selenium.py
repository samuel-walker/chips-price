import time
from selenium import webdriver

driver = webdriver.Chrome('D:\\Dropbox\\Coding\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.realcanadiansuperstore.ca');
time.sleep(5) # Let the user actually see something!

# Select province
try:
    elem = driver.find_element_by_css_selector('[data-province-code="CA-BC"]')
    print('Found <%s> element for province button!' % (elem.tag_name))
    type(elem)
    elem.click()
    time.sleep(5)
    print("Navigated!")
except:
    print('Was not able to find province button.')

# Select food category
try:
    elem = driver.find_element_by_css_selector('[data-auid="food"] a')
    print('Found <%s> element for food category!' % (elem.tag_name))
    type(elem)
    elem.click()
    time.sleep(1)
    print("Navigated!")
except:
    print('Was not able to find food category link.')

# Select food category
try:
    elem = driver.find_element_by_css_selector('[data-auid="pantry"] a')
    print('Found <%s> element for pantry category!' % (elem.tag_name))
    type(elem)
    elem.click()
    time.sleep(1)
    print("Navigated!")
except:
    print('Was not able to find pantry category link.')

# Select chips category
try:
    elem = driver.find_element_by_css_selector('[data-category-code="RCSS001008011000"] a')
    print('Found <%s> element for chips category!' % (elem.tag_name))
    type(elem)
    elem.click()
    time.sleep(5)
    print("Navigated!")
except:
    print('Was not able to find chip category link.')

# Select potato chips category
try:
    elem = driver.find_element_by_css_selector('[data-category-code="RCSS001008010001"] a')
    print('Found <%s> element for potato chips category!' % (elem.tag_name))
    type(elem)
    elem.click()
    time.sleep(5)
    print("Navigated!")
except:
    print('Was not able to find potato chip category link.')

# Sort by popular
try:
    elem = driver.find_element_by_link_text('RCSS001008010001?filters=&sort=popularity')
    print('Found <%s> element for sorting!' % (elem.tag_name))
    type(elem)
    elem.click()
    time.sleep(5)
    print("Navigated!")
except:
    print('Was not able to find popularity sort link.')

print("Quitting")
driver.quit()


# steps
https://www.realcanadiansuperstore.ca
button
<button class="select-province btn btn-primary" data-province-code="CA-BC" data-store-id="1520">British Columbia</button>


# orig
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()
