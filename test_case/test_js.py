# import time
# from selenium import webdriver
# from common.base import Base
#
# driver = webdriver.Firefox()
# driver.get('https://www.bilibili.com/')
# bil = Base(driver)
# bil.js_scroll_end()         #滚动到底部
# time.sleep(1)
# bil.js_scroll_top()         #滚动到顶部
#
# loc = ('link text','国创')
# bil.js_focus_element(loc)   #聚焦到 元素 上
# bil.click(loc)