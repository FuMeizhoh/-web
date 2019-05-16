#登录页
from selenium import webdriver
import unittest
from pages.login_page import Login_Hdf
from common.base import Base

class Login(unittest.TestCase):
    '''登录页面case'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.aa = Login_Hdf(cls.driver)
        cls.bb = Base(cls.driver)

    def setUp(self):
        self.driver.get("https://passport.haodf.com/user/showlogin")
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test01(self):
        '''用户名：hdfnfs35rta 密码：Ljf123 点击登录，期望结果：登录成功 '''
        self.aa.login_fuc(username='hdfnfs35rta',psw='Ljf123')
        t = self.aa.is_logined()
        self.assertTrue(t=="hdfnfs35rta")

    def test02(self):
        '''手机号:13011068815 密码：Ljf123 点击登录，期望结果：登录成功'''
        self.aa.login_fuc(username='13011068815',psw='Ljf123')
        t = self.aa.is_logined()
        self.assertTrue(t=="hdfnfs35rta")

    def test03(self):
        '''手机号:13011068814 密码：Ljf123 点击登录，期望结果：用户名不存在'''
        self.aa.username('13011068814')
        self.aa.password('Ljf123')
        self.aa.click_login()
        loc = ('xpath','.//*[text()="用户名不存在"]')
        text= self.aa.get_text(loc)
        self.assertTrue(text=='用户名不存在')

    def test04(self):
        '''手机号:13011068814 密码：空  点击登录，期望结果：用户名或密码错误'''
        self.aa.username('13011068814')
        self.aa.password('')
        self.aa.click_login()
        loc = ('xpath','.//*[text()="用户名或密码错误"]')
        text= self.aa.get_text(loc)
        self.assertTrue(text=='用户名或密码错误')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
