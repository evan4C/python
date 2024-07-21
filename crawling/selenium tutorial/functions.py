import time


def login(url, driver):
    driver.get(url)
    time.sleep(10)
    username = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/input')
    username.send_keys('o0lifan0o@qq.com')
    time.sleep(1)
    ps = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/form/div[2]/div/div/input')
    ps.send_keys('o0lifan0o')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/button').click()
    return driver.current_url


def get_page_source(url, driver):
    driver.get(url)
    try:
        print(driver.page_source)  # 输出网页源码
    except Exception as e:
        print(str(e))
