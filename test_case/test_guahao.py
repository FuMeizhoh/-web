from selenium import webdriver
import unittest
from pages.guahao_page import Register_Page
from pages.login_page import Login_Hdf

class Info(unittest.TestCase):
    '''预约挂号'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.aa = Register_Page(self.driver)
        self.bb = Login_Hdf(self.driver)
        self.driver.get("https://passport.haodf.com/user/showlogin")
        self.bb.login_fuc()

    def test01(self):
        '''预约挂号-按疾病-去看病'''
        self.aa.jibing_kanbing()
        t = self.aa.shenqing()
        print(t)
        self.assertTrue(t=="立即申请")

    def test02(self):
        '''预约挂号-按疾病-去挂号'''
        self.aa.jibing_guahao()
        t = self.aa.wei_kaitong()
        print(t)
        self.assertTrue(t=="暂未开通")

    def test03(self):
        '''预约挂号-按医院-点咨询'''
        self.aa.hospital_zixun()
        t = self.aa.shenqing()
        print(t)
        self.assertTrue(t=="立即申请")

    def test04(self):
        '''预约挂号-按医院-点可通电话'''
        self.aa.hospital_tel()
        t = self.aa.shenqing()
        print(t)
        self.assertTrue(t=="立即申请")

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
