from selenium import webdriver
from common.base import Base


driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
baidu = Base(driver)

loc = ('link text','设置')
baidu.move_to_element(loc)

a = ['1','as','ss']

b = ['ss']
c = [m+n for m in a for n in b]
print(c)



