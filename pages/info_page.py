#coding:utf-8
from common.base import Base
from selenium import webdriver
url = 'http://www.duobeiyun.com/'


class InfoPage(Base):
    '''展示页'''
    loc1 = ('link text','专网通')
    loc2 = ('link text','社群课')
    # driver = webdriver.Firefox()

    def zhuanwangtong(self):
        '''专网通跳转'''
        self.click(self.loc1)

    def shequnke(self):
        '''社群课跳转'''
        self.click(self.loc2)


if __name__=='__main__':
    IN = InfoPage()

