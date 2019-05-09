from selenium import webdriver
from common.base import Base
'''
步骤1、先定个类
步骤2、把元素定位全写出来
步骤3、每个大步骤封装方法
步骤4、断言
步骤5、写用例
'''
#全局变量放在类的外面
login_url= 'http://127.0.0.1:81/zentao/user-login.html'

class Login_page(Base):

	#定位元素
	loc_user=('id','account')
	loc_pwd=('xpath','//input[@name="password"]')
	loc_login=('id','submit')
	loc_keep =('id','keepLoginon')
	loc_forget=('link text','忘记密码')
	loc_loginname=('xpath','.//a[@data-toggle="dropdown"]')
	loc_reset=('xpath','.//div[@class="alert alert-info"]/h5')

	def login_zentao(self,user='admin',pwd='123456',keeplogin=False):
		self.driver.get(login_url)
		self.sendKeys(self.loc_user,user)
		self.sendKeys(self.loc_pwd,pwd)
		if keeplogin:self.keep_login()          #保存登录，加个开关，默认不勾选（映射过去）
		self.click(self.loc_login)

#登录页更多的元素封装

	def user_name(self,text):
		self.sendKeys(self.loc_user,text)

	def pass_word(self,text):
		self.sendKeys(self.loc_pwd,text)

	def keep_login(self):
		self.click(self.loc_keep)

	def click_login(self):
		self.click(self.loc_login)

	def forget_pwd(self):
		self.click(self.loc_forget)

	#断言
	def is_logined(self):
		try:
			title = self.get_text(self.loc_loginname)
			return title
		except:
			print('登录跳转页失败')
			return ''

	#忘记密码重置页
	def is_reset(self):
		t = self.get_text(self.loc_reset)
		return t


#这才是最后的第五步，写用例
if __name__=='__main__':
	driver = webdriver.Firefox()
	zen =Login_page(driver)
	zen.login_zentao(keeplogin=True)        #勾选保存登录
	r=zen.is_logined()
	assert r=='admi'


	# timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
