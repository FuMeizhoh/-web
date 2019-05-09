from selenium import webdriver
from common.base import Base

'''
步骤1、先定个类
步骤2、把元素定位全写出来
步骤3、每个大步骤封装方法
步骤4、断言
步骤5、写用例
'''
class AddBug(Base):     #继承了就不用实例化了

	#定位add_bug
	loc1 = ('link text','测试')
	loc2 = ('link text','Bug')
	loc3 = ('xpath','//a[@class="btn btn-primary"]')
	loc4 = ('id','title')
	loc_trunk=('xpath','//ul[@class="chosen-choices"]')
	loc_trunk_cli= ('xpath','.//*[@id="openedBuild_chosen"]/div/ul/li')
	#切换到iframe
	loc_frame=('xpath','.//iframe[@class="ke-edit-iframe"]')        #xpath定位要写成 .// 写成//有时会找不到
	loc_text=('xpath','.//body[@class="article-content"]')
	loc_save = ('id','submit')

	#断言
	xinzen = ('xpath','.//*[@id="bugList"]/tbody/tr[1]/td[4]')


	def add_bug(self,title):
		self.click(self.loc1)
		self.click(self.loc2)
		#新增bug
		self.click(self.loc3)
		self.sendKeys(self.loc4,title)                  #加个时间戳，每次就不一样了
		#trunk版本
		self.click(self.loc_trunk)
		self.click(self.loc_trunk_cli)
		#切换frame
		frame = self.findElement(self.loc_frame)
		self.driver.switch_to.frame(frame)

		self.sendKeys(self.loc_text,'操作不走位')
		#记得返回主页面上，不然停留在frame
		self.driver.switch_to_default_content()
		self.click(self.loc_save)

	def is_add_bug_sucess(self,text):
		return self.is_text_in_element(self.xinzen,text)

if __name__=='__main__':
	driver = webdriver.Firefox()