import unittest
from selenium import webdriver
from pages.example_zentao_login_page import Login_page
from pages.example_zentao_addbug import AddBug
'''
以上登录页和add bug页分别调用，好维护，按每个页面来写方法
'''

class Test_Add_Bug(unittest.TestCase):
	@classmethod

	def setUpClass(cls):
		cls.driver=webdriver.Firefox()
		cls.zen = Login_page(cls.driver)
		cls.ad = AddBug(cls.driver)
		cls.zen.login_zentao()

	def test_add_bug(self):
		title ='测试提交bug'
		self.ad.add_bug(title)
		r = self.ad.is_add_bug_sucess(title)
		print(r)
		self.assertTrue(r)
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main()