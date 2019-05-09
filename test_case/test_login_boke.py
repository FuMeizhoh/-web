import time
import unittest

from selenium import webdriver

from pages.boke_login_page import LoginBokeYuan


class BoKeYuan(unittest.TestCase):
	'''
	登录博客园
	'''

	def setUp(self):                    #千万注意大小写
		self.driver = webdriver.Firefox()
		self.driver.get('https://www.cnblogs.com/')
		self.driver.implicitly_wait(30)
		self.bb = LoginBokeYuan(self.driver)            #封装的登录类，先实例化

	def test_bo(self):
		'''
		登录博客园
		:return:
		'''
		self.bb.login_page()
		time.sleep(1)
		self.bb.yzm()
		time.sleep(1)
		self.bb.is_username()
		# self.assertTrue()

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	unittest.main()