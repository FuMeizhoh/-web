from common.read_excel import ExcelUtil
import unittest
from selenium import webdriver
from pages.example_zentao_login_page import Login_page
import os
import ddt

'''
1、输入admin ,输入123456 点登录   期望结果：登陆后用户名一致
2、输入admin ,输入 空，点登录  期望结果：登录失败
3、输入admin，输入123456，点记住登录 ，点登录    期望结果：
4、点忘记密码

'''
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#os.path.realpath(__file__)获取模块所在当前绝对路径,os.path.dirname为了获取上一层路径
filepath = os.path.join(curpath,"common","datas.xlsx")
print(filepath)
data = ExcelUtil(filepath)
testdatas = data.dict_data()
print(testdatas)

#跟把数据放在脚本里是一样的
# 测试数据
# testdatas = [
# 			{"user":"admin","pwd":"123456","expect":"admin"},
# 			{"user":"admin","pwd":"","expect":""}
# ]

@ddt.ddt             #ddt也要加个修饰
class LoginChandao(unittest.TestCase):  #类命名是大驼峰

	@classmethod   #必须写这个修饰，用的是类方法
	def setUpClass(cls):
		#用例前，只执行一次
		cls.driver= webdriver.Firefox()
		cls.lg = Login_page(cls.driver)#登录类的调用

	def setUp(self):
		#每个用例执行之前，先执行一次
		self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
		self.driver.delete_all_cookies()
		self.driver.refresh()
		print('打开登录页')

	def login_case(self,user,pwd,expect):
		self.lg.user_name(user)
		self.lg.pass_word(pwd)
		self.lg.click_login()
		login_name = self.lg.is_logined()
		self.assertTrue(login_name==expect)

	@ddt.data(*testdatas)
	def test_01(self,data):   #每个用例必须要以test开头，小驼峰
		'''输入admin ,输入 123456，点登录'''
		print('--------------开始测试 test_01---------')
		print('测试数据%s'% data)
		self.login_case(data['user'],data['pwd'],data['expect'])
		print('--------------结束测试 pass---------')


	def test_03(self):
		''' 输入admin，输入123456，勾选记住登录 ，点登录'''
		self.lg.user_name('admin')
		self.lg.pass_word('123456')
		self.lg.keep_login()
		loc_keep =('id','keepLoginon')
		s = self.lg.isSelect(loc_keep)
		print('保持登录是否勾选：%s'%s)
		self.lg.click_login()
		login_name = self.lg.is_logined()
		print(login_name)
		self.assertTrue(login_name=='admin')

	def test_04(self):
		'''忘记密码 '''
		self.lg.forget_pwd()
		t = self.lg.is_reset()
		print(t)
		self.assertTrue(t=='普通用户请联系管理员重置密码')


	# def tearDown(self):
	# 	#is_alert(self.driver)   或者放在这里
	# 	# self.driver.delete_all_cookies() #退出登录，
	# 	# self.driver.refresh()           #再刷新一下，就可以输入下个用户名密码
	# 	self.driver.quit()

	@classmethod
	def tearDownClass(cls):
		#用例后，只调用一次
		cls.driver.quit()
		print('关闭浏览器')
if __name__=='__main__':
	unittest.main()
