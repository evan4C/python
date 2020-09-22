# Simple assignment
from selenium.webdriver import Safari

# url = "https://www.itjuzi.com/login"
url = "https://www.example.com"

with Safari() as driver:
    driver.get(url)
    elements = driver.find_elements_by_tag_name('p')
    for e in elements:
        print(e.text)
