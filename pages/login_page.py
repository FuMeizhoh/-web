#coding:utf-8
from common.base import Base
from selenium import webdriver
import time

class Login_Hdf(Base):
	loc_user = ('id','tel')
	loc_pwd =('id','pass')
	loc_login=('xpath','.//div[@class="fl w290"]/a')
	loc_forget=('link text','忘记密码？')
	loc_name= ('id','username')



	def login_fuc(self,username='13011068815',psw='Ljf123'):
		'''登录网站好大夫在线'''
		self.sendKeys(self.loc_user,username)
		self.sendKeys(self.loc_pwd,psw)
		self.click(self.loc_login)

	def username(self,user):
		self.sendKeys(self.loc_user,user)

	def password(self,pwd):
		self.sendKeys(self.loc_pwd,pwd)

	def click_login(self):
		'''登录按钮'''
		self.click(self.loc_login)

	def forget_pwd(self):
		'''忘记密码'''
		self.click(self.loc_forget)

	def is_logined(self):
		'''
		判断登录是否成功，获取登录后用户名
		'''
		try:
			a = self.get_text(self.loc_name)
			return a
		except:
			print('登陆失败，未获取登录用户名内容')
			return ""

if __name__=='__main__':
	driver = webdriver.Chrome()
	by = Login_Hdf(driver)
	driver.get("https://passport.haodf.com/user/showlogin")
	by.click_login()
	time.sleep(3)


