'''
    interface: demo_test
    Usage:
        1. 从data文件夹获取待测试的api 及其对应参数；
        2. 从model 中调用 session 请求，保持会话登录；
        3. 在本文件中构造测试用例；
        4. 在根目录下，运行run.py ；
        5. 在report 中查看测试报告

'''

import requests
import unittest
import sys
# 获取项目根目录
sys.path.append("../")
from data.urls import *


class Shopping(unittest.TestCase):
    def setUp(self) -> None:
        self.response = []

        # 获取测试的api 参数
        self.url = data_urls["shopping_url"]
        self.payload = data_params["shopping_params"]

        # 构造请求头
        self.headers = data_headers["headers"]
        self.session = request_session()

    def tearDown(self) -> None:
        print(self.response)

    def test_shopping_success(self):
        real_res = self.session.post(self.url, data=self.payload, headers=self.headers)

        # 储存响应正文
        self.response.append(real_res.json())

        real_result = ""        # 实际结果
        expect_result = ""      # 预期结果

        # 获取响应状态码
        real_status = real_res.status_code

        # 断言
        self.assertEqual(real_result, expect_result, "实际结果与预期结果不一致!")


if __name__ == "__main__":
    unittest.mian()

