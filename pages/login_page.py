#coding:utf-8
import time
from common.base import Base

class Login():      #继承了base类，就不用写__init__了
	def __init__(self,driver):
		self.driver =driver             #类的初始化,都要传driver这个参数

	def login_fuc(self,username='admin',psw='12345'):     #driver 是形参，万一换浏览器岂不是扎了
		'''                                 #打3个点，回车，自动补全
		登录网站
		:param driver:
		:param username:用户名
		:param psw:密码
		:return:
		'''
		self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
		time.sleep(2)
		self.driver.find_element_by_id('account').send_keys(username)
		self.driver.find_element_by_name('password').send_keys(psw)
		self.driver.find_element_by_id('submit').click()


	def get_username(self):
		'''
		获取登录成功后的用户名信息
		:param self:
		:return:
		'''
		try:
			t = self.driver.find_element_by_xpath('.//a[@data-toggle="dropdown"]').text
			print('获取到登录名:%s'%t)
			return t
		except:
			return ""

	def is_alert(self):
		'''
		登录失败是否有alert弹窗
		:param self:
		:return:
		'''
		try:
			a = self.driver.switch_to.alert
			time.sleep(1)
			print(a.text)
			a.accept()
		except:
			return ""

# if __name__=='__main__':
# 	from selenium import webdriver
# 	driver = webdriver.Firefox()
# 	zentao = LoginZenTao(driver)
# 	zentao.login_fuc()
