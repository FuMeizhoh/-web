#coding:utf-8
import time
class LoginBokeYuan():

	def __init__(self,driver):
		self.driver = driver

	def yzm(self):
		'''
		判断是否需要输验证码
		:return:
		'''
		try:
			a = self.driver.find_element_by_class_name('geetest_radar_tip')
			print('验证吗输入：%s'%a.text)
			a.click()
			return a.text
		except:
			pass

	def is_username(self):
		'''
		判断用户：大大大泡泡糖 是否登录成功
		:return:
		'''
		try:
			t = self.driver.find_element_by_link_text('大大大泡泡糖').text
			print(t)
			if t=='大大大泡泡糖':
				pass
			return t
		except:
			return ''

	def login_page(self):
		self.driver.find_element_by_link_text('登录').click()
		time.sleep(1)
		self.driver.find_element_by_id('input1').send_keys('工作一年半')
		self.driver.find_element_by_id('input2').send_keys('@@LJF@ljf123')
		self.driver.find_element_by_id('signin').click()
		# self.assertTrue()

#这个是为了验证封装的类是否写对了
if __name__=='__main__':
	from selenium import webdriver
	driver = webdriver.Firefox()
	driver.get('https://www.cnblogs.com/')
	bok = LoginBokeYuan(driver)
	bok.login_page()
