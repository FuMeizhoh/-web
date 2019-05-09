#coding:utf-8
from common.base import Base

class Login_DuoBY(Base):
	loc_user = ('name','username')
	loc_pwd =('name','password')
	loc_login=('xpath','.//button[@type="submit"]')
	loc_register=('link text','马上注册')
	loc_forget=('link text','忘记密码')
	loc_jump=('link text','多贝云')
	loc_admin=('id','login_name')

	def login_fuc(self,username='admin',psw='12345'):    
		'''登录网站多贝云'''
		self.sendKeys(self.loc_user,username)
		self.sendKeys(self.loc_pwd,psw)
		self.click(self.loc_login)


	def douby_jump(self):
		'''点击“多贝云”跳转'''
		self.click(self.loc_jump)

	def username(self,user):
		self.sendKeys(self.loc_user,user)

	def password(self,pwd):
		self.sendKeys(self.loc_pwd,pwd)

	def click_login(self):
		'''登录按钮'''
		self.click(self.loc_login)

	def register(self):
		'''注册'''
		self.click(self.loc_register)

	def forget_pwd(self):
		'''忘记密码'''
		self.click(self.loc_forget)

	def is_logined(self):
		'''
		判断登录是否成功，获取登录后的用户名一致性
		'''
		try:
			a = self.get_text(self.loc_admin)
			return a.text
		except:
			print('登陆失败，未获取到用户名：%s'%a.text)
			return ""

if __name__=='__main__':
	by = Login_DuoBY()
