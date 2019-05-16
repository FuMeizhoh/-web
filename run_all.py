import unittest
from common import HTMLTestRunner_cn
import time
#查找用例的路径
casePath = r'D:\\Git_Project\\any_web\\test_case'
#用例的匹配规则，查找case
rule = 'test*.py'

#discover方法加载多个用例集合
discover = unittest.defaultTestLoader.discover(start_dir=casePath,
                                               pattern = rule,
                                               top_level_dir=None)
# print(discover)
#系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
reportPath = "D:\Git_Project\any_web\\report\\"+now+" result.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                         title='好大夫在线---自动化测试报告',
                                         description='用例执行情况',
                                         retry=1)   #失败case重跑一次
runner.run(discover)
#关闭，回收内存，不然影响性能
fp.close()