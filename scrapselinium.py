import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
driver.get(url)

devicename = []
descriptionslist = []
ratingslist = []
priceslist = []

device_names = driver.find_elements(By.CLASS_NAME, 'title')
for device in device_names:
    devicename.append(device.text)

device_descriptions = driver.find_elements(By.CLASS_NAME, 'description')
for description in device_descriptions:
    descriptionslist.append(description.text)

ratings = driver.find_elements(By.XPATH, "//p[@data-rating]")
for rating in ratings:
    ratingslist.append(rating.get_attribute('data-rating'))

prices = driver.find_elements(By.CLASS_NAME, 'price')
for price in prices:
    priceslist.append(price.text)

driver.quit()

data = {
    'Device Name': devicename,
    'Description': descriptionslist,
    'Rating': ratingslist,
    'Price': priceslist
}

df = pd.DataFrame(data)

df.to_csv('laptops_data.csv', index=True)

print("Data has been saved to laptops_data.csv")
