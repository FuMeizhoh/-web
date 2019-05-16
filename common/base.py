from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *        #所有异常
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Base():
	'''selenium简单再封装（基础操作的方法）---by LIU JF'''
	def __init__(self,driver:webdriver.Firefox):
		self.driver = driver
		self.timeout=10
		self.t = 0.5

	def findElementNew(self, locator):
		'''定位到元素，返回元素对象，没定位到，Timeout异常'''
		if not isinstance(locator, tuple):
			print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')		#打印注释一下，加深记忆
		else:
			print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
			ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
			return ele

	def findElement(self, locator):
		if not isinstance(locator, tuple):
			print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
		else:
			print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
			ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
			return ele

	def findElements(self, locator):
		if not isinstance(locator, tuple):
			print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
		else:
			try:
				print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
				eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
				return eles
			except:
				return []

	def sendKeys(self,locator,text='',is_clear_first=False):
		'''is_clear_first默认为False,不清空 '''
		ele = self.findElement(locator)
		if is_clear_first:
			ele.clear()        #is_clear_first 为True的时候执行
		ele.send_keys(text)

	def clear(self,locator):
		''' 清空输入框'''
		ele = self.findElement(locator)
		ele.clear()

	def click(self,locator):
		'''点击事件'''
		ele = self.findElementNew(locator)
		ele.click()

	def isSelect(self,locator):
		''' 判断元素是否被选中，返回布尔值'''
		ele = self.findElement(locator)
		r = ele.is_selected()
		return r

	def isDisplayed(self,locator):
		''' 判断元素是否显示，返回布尔值'''
		ele = self.findElement(locator)
		r = ele.is_displayed()
		return r

	def isElementExist(self,locator):
		try:
			self.findElement(locator)
			return True
		except:
			return False

	def isElementExist2(self,locator):
		'''判断多个元素是否存在'''
		eles = self.findElements(locator)
		n = len(eles)
		if n == 0:
			return False
		elif n == 1:
			return True
		else:
			print("定位到元素的个数：%s"%n)
			return  True

	def is_title(self, title):
		'''返回bool值'''
		try:
			result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
			return result
		except:
			return False

	def is_title_contains(self, title):
		'''返回bool值'''
		try:
			result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
			return result
		except:
			return False

	def is_text_in_element(self, locator, text):
		'''返回bool值'''
		if not isinstance(locator, tuple):
			print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
		try:
			result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,text))
			return result
		except:
			return False

	def is_value_in_element(self, locator, value):
		'''返回bool值, value为空字符串，返回Fasle, 例子：不是文本，是value属性值，‘百度一下’为例'''
		if not isinstance(locator, tuple):
			print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
		try:
			result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,value))
			return result
		except:
			return False

	def is_alert(self, timeout=3):
		'''判断页面是否有alert,有即返回alert，然后switch_alert函数'''
		try:
			result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
			return result
		except:
			return False

	def is_alert_exist(self):
		'''判断alert是不是存在'''
		a = self.is_alert()
		if a :
			print(a.text)
			a.accept()
		else:
			print('不存在')

	def get_title(self):
		'''获取title'''
		return self.driver.title

	def get_text(self, locator):
		'''获取文本'''
		try:
			t = self.findElement(locator).text
			return t
		except:
			print("获取text失败，返回'' ")
			return ""

	def get_attribute(self, locator, name):
		'''获取属性'''
		try:
			element = self.findElement(locator)
			return element.get_attribute(name)
		except:
			print("获取%s属性失败，返回'' "%name)
			return ""

	def js_focus_element(self, locator):
		'''聚焦元素'''
		target = self.findElement(locator)
		self.driver.execute_script("arguments[0].scrollIntoView();", target)

	def js_scroll_top(self):
		'''滚动到顶部'''
		js = "window.scrollTo(0,0)"
		self.driver.execute_script(js)

	def js_scroll_end(self,x=0):
		'''滚动到底部,若横向滚动，改参数x'''
		js = "window.scrollTo(%s,document.body.scrollHeight)"%x
		self.driver.execute_script(js)

	def select_by_index(self, locator, index=0):
		'''通过索引,index是索引第几个，从0开始，默认选第一个'''
		element = self.findElement(locator)  # 定位select这一栏
		Select(element).select_by_index(index)

	def select_by_value(self, locator, value):
		'''通过value属性'''
		element = self.findElement(locator)
		Select(element).select_by_value(value)

	def select_by_text(self, locator, text):
		'''通过文本值定位'''
		element = self.findElement(locator)
		Select(element).select_by_visible_text(text)

	def switch_iframe(self, id_index_locator):
		'''切换iframe'''
		try:
			if isinstance(id_index_locator, int):
				self.driver.switch_to.frame(id_index_locator)
			elif isinstance(id_index_locator, str):
				self.driver.switch_to.frame(id_index_locator)
			elif isinstance(id_index_locator, tuple):
				ele = self.findElement(id_index_locator)
				self.driver.switch_to.frame(ele)
		except:
			print("iframe切换异常")

	def switch_handle(self, window_name):
		self.driver.switch_to.window(window_name)

	def switch_alert(self):
		r = self.is_alert()
		if not r:
			print("alert不存在")
		else:
			return r

	def move_to_element(self, locator):
		'''鼠标悬停操作'''
		try:
			ele = self.findElement(locator)
		except TimeoutException:
			print("element not found:%s"%locator)
		else:
			ActionChains(self.driver).move_to_element(ele).perform()

if __name__=='__main__':
	driver = webdriver.Firefox()
	driver.get('http://www.baidu.com')
	deng = Base(driver)
	# loc1 = (By.ID,'kw')
	# loc2 = (By.ID,'su')
	loc1 = ('id','kw')
	loc2 = ('id','su')
	deng.sendKeys(loc1,'sass')
	deng.click(loc2)