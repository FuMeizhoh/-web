from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
time.sleep(2)
driver.find_element_by_link_text('新闻').click()

print(driver.current_url)