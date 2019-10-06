'''
    author：JadenYu
    Date：2019-6-7
    version：Python3.6

    Function： 
        1.启动本文件，运行接口测试；

'''

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

# 加载测试集
test_case = unittest.defaultTestLoader.discover("./test_case","**test.py")
suite = unittest.TestSuite()
suite.addTest(test_case)

# 获取当前时间
now = time.strftime("%Y-%m-%d %H_%M_%S")

# 引入测试报告
file_path = "./reports/" + "test_report" + now + ".html"    # 确定测试报告的存放路径

title = "xxx 测试报告"
descr = "xxx 的接口测试"

with open (file_path,"wb") as f:
    runner = HTMLTestRunner(stream=f,title=title,description=descr)
    runner.run(suite)
    f.close()
