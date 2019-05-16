# coding:utf-8
from selenium import webdriver
import time
import threading

#主要是做浏览器兼容测试，不完善，日后研究
def startBrowser(br_name):
    '''打开浏览器函数，firefox、chrome、ie'''
    try:
        if br_name == "firefox" or br_name == "Firefox":
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            return driver
        elif br_name == "chrome" or br_name == "Chrome":
            print("start browser name :Chrome")
            driver = webdriver.Chrome()
            return driver
        elif br_name == "ie" or br_name == "Ie":
            print("start browser name :Ie")
            driver = webdriver.Ie()
            return driver
        else:
            print("Not found this browser,You can use 'firefox', 'chrome'or 'ie'")
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

def run_case(br_name):
    driver = startBrowser(br_name)
    driver.get("https://www.haodf.com/")
    time.sleep(3)
    print(driver.title)
    driver.quit()
    #写成类，供其他用例多进程，日后研究

def thread_br():
    # 创建线程数组
    threads = []
    # 创建线程t1，并添加到线程数组
    t1 = threading.Thread(target=run_case, args=('Firefox',))
    threads.append(t1)
    # 创建线程t2，并添加到线程数组
    t2 = threading.Thread(target=run_case, args=('Chrome',))
    threads.append(t2)
    # # 创建线程t2，并添加到线程数组
    # t3 = threading.Thread(target=run_case, args=('Ie',))
    # threads.append(t3)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    thread_br()
    while True:
        time.sleep(10)

