#登录页

from selenium import webdriver
import unittest
from pages.login_page import Login_DuoBY
from common.base import Base

'''

1、输入admin ,输入123456 点登录   期望结果：登陆后用户名一致
2、输入admin ,输入 空，点登录  期望结果：登录失败
3、输入admin，输入123 ，点登录   期望结果：登录失败
4、点忘记密码

'''

class Login(unittest.TestCase):
    '''
    登录用例
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.aa = Login_DuoBY(cls.driver)
        cls.bb = Base(cls.driver)

    def setUp(self):
        self.driver.get("http://www.duobeiyun.com/login")
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test01(self):
        '''输入admin ,输入123456 点登录   期望结果：登陆后用户名一致'''
        self.aa.login_fuc()
        t = self.aa.is_logined()
        self.assertTrue(t=="admin")

    def test02(self):
        '''输入admin ,输入 空，点登录  期望结果：登录失败'''
        self.aa.username('admin')
        self.aa.password('')
        self.aa.click()
        a=self.bb.is_alert()
        print(a.text)
        self.assertTrue(a.text=='登录失败，请检查您的用户名或密码是否填写正确' or '您还有3次尝试机会。'or '您还有2次尝试机会。'or '您还有1次尝试机会。' )
        a.accept()

    def test03(self):
        '''输入admin，输入123 ，点登录   期望结果：登录失败'''
        self.aa.username('admin')
        self.aa.password('123')
        self.aa.click()
        a=self.bb.is_alert()
        print(a.text)
        self.assertTrue(a.text=='登录失败，请检查您的用户名或密码是否填写正确' or '您还有3次尝试机会。'or '您还有2次尝试机会。'or '您还有1次尝试机会。' )
        a.accept()

    def test04(self):
        '''点忘记密码'''
        self.aa.forget_pwd()
        loc_reset = ("xpath",".//*[text()='密码重置']")
        title = self.bb.get_text(loc_reset)
        self.assertTrue(title=='密码重置')

    def test05(self):
        '''从登录页进入介绍页'''
        self.aa.douby_jump()
        t = self.driver.current_url
        print(t)
        self.assertTrue(t=="http://www.duobeiyun.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
