from selenium.webdriver import Safari
from functions import login, get_page_source

url = "https://www.itjuzi.com/login"

with Safari() as driver:
    new_url = login(url, driver)
    get_page_source(new_url, driver)
