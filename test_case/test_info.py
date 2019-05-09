#介绍页：从登录页进入
from selenium import webdriver
import unittest
from pages.info_page import InfoPage
from pages.login_page import Login_DuoBY

class Info(unittest.TestCase):
    '''
    介绍页用例
    '''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.aa = InfoPage(self.driver)
        self.driver.get("http://www.duobeiyun.com/")

    def test01(self):
        '''专网通跳转'''
        self.aa.zhuanwangtong()
        h = self.driver.window_handles
        self.driver.switch_to.window(h[1])
        t = self.driver.current_url
        print(t)
        self.assertTrue(t=="https://www.zhuanwangtong.com/")

    def test02(self):
        '''社群课跳转'''
        self.aa.shequnke()
        h = self.driver.window_handles
        self.driver.switch_to.window(h[1])
        t = self.driver.current_url
        print(t)
        self.assertTrue(t=="http://www.shequnke.com/")

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
