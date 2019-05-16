#coding:utf-8
from common.base import Base
from selenium import webdriver
from pages.login_page import Login_Hdf
import time

class Register_Page(Base):
    '''挂号页'''
    loc_gua=('link text','预约挂号')
    loc_jibing=('link text','按疾病')
    loc_yiyuan=('link text','按医院')
    loc_zhuanke=('link text','按专科')
    loc_erkexue=('link text','儿科学')
    loc_xiaoerhuxi=('link text','小儿呼吸科')
    loc_xiaoerfeiyan=('link text','小儿肺炎')
    loc_city1=('link text','北京')
    loc_doctorlist=('link text','刘晓红')
    loc_kanbing=('link text','去看病')
    loc_guahao=('link text','去挂号')

    loc_weikaitong=('xpath','.//a[class="r-c-i-btn grey-btn"]')  #暂未开通
    loc_shenqing=('xpath','.//div[@class="submit-btn js-submit-btn"]') #立即申请

    loc_city2=('link text','上海')
    loc_town=('link text','松江')
    loc_hospital=('link text','九亭医院')
    loc_pifuke=('link text','皮肤科')
    loc_zixun=('link text','立即咨询本科室大夫')
    loc_zixunwo=('xpath','.//td[@class="tde"]/li[2]/a')  #咨询我
    loc_call_tel=('link text','电话咨询')     #可通电话


    def jibing_kanbing(self):
        '''按疾病-去看病'''
        self.click(self.loc_gua)
        h = self.driver.window_handles
        self.switch_handle(h[1])
        self.click(self.loc_jibing)
        self.click(self.loc_erkexue)
        self.click(self.loc_xiaoerhuxi)
        self.click(self.loc_xiaoerfeiyan)
        h1 = self.driver.window_handles
        self.switch_handle(h1[2])
        self.move_to_element(self.loc_city1)
        time.sleep(3)
        self.click(self.loc_doctorlist)
        h2 = self.driver.window_handles
        self.switch_handle(h2[3])
        self.click(self.loc_kanbing)


    def jibing_guahao(self):
        '''按疾病-去挂号'''
        self.click(self.loc_gua)
        h = self.driver.window_handles
        self.switch_handle(h[1])
        self.click(self.loc_jibing)
        self.click(self.loc_erkexue)
        self.click(self.loc_xiaoerhuxi)
        self.click(self.loc_xiaoerfeiyan)
        h1 = self.driver.window_handles
        self.switch_handle(h1[2])
        self.move_to_element(self.loc_city1)
        time.sleep(3)
        self.click(self.loc_doctorlist)
        h2 = self.driver.window_handles
        self.switch_handle(h2[3])
        self.click(self.loc_guahao)

    def wei_kaitong(self):
        '''预约挂号-暂未开通'''
        t = self.get_text(self.loc_weikaitong)
        return t

    def shenqing(self):
        '''预约挂号开通-立即申请'''
        t = self.get_text(self.loc_shenqing)
        return t

    def hospital_zixun(self):
        '''按医院-咨询我'''
        self.click(self.loc_gua)
        h1 = self.driver.window_handles
        self.switch_handle(h1[1])
        self.click(self.loc_yiyuan)
        self.click(self.loc_city2)
        self.click(self.loc_town)
        self.click(self.loc_hospital)
        h2 = self.driver.window_handles
        self.switch_handle(h2[2])
        self.js_focus_element(self.loc_pifuke)
        self.click(self.loc_pifuke)
        self.click(self.loc_zixun)
        h3 = self.driver.window_handles
        self.switch_handle(h3[3])
        self.click(self.loc_zixunwo)

    def hospital_tel(self):
        '''按医院-可通电话'''
        self.click(self.loc_gua)
        h1 = self.driver.window_handles
        self.switch_handle(h1[1])
        self.click(self.loc_yiyuan)
        self.click(self.loc_city2)
        self.click(self.loc_town)
        self.click(self.loc_hospital)
        h2 = self.driver.window_handles
        self.switch_handle(h2[2])
        self.js_focus_element(self.loc_pifuke)
        self.click(self.loc_pifuke)
        self.click(self.loc_zixun)
        h3 = self.driver.window_handles
        self.switch_handle(h3[3])
        self.click(self.loc_call_tel)
        print(self.driver.current_url)           #页面跳转随机？






if __name__=='__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    kk = Login_Hdf(driver)
    driver.get("https://passport.haodf.com/user/showlogin")
    kk.login_fuc()
    gg = Register_Page(driver)
    gg.hospital_tel()



