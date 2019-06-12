'''
    作用：二次封装 session_requests;
    Usage:
        1、直接调用本文件下的函数 request_session（）；
'''

import unittest
import requests
import sys
# 获取项目根目录
sys.path.append("../")
from data.urls import *


def request_session():
    req_session = requests.session()
    header = data_headers["headers"]
    login_data = data_params["login_params"]
    url_login = data_urls["login_url"]
    login_res = req_session.post(url_login, data=login_data, headers=header)

    return req_session

'''
# 仅用了来调试

class Shopping(unittest.TestCase):
    def setUp(self) -> None:
        self.response = []
        self.url = data_urls["shopping_url"]
        self.payload = data_params["shopping_params"]
        self.headers = data_headers["headers"]
        self.session = request_session()

        # self.session = requests.session()
        # self.headers = data_headers["headers"]
        # login_data = data_params["login_params"]
        # url_login = data_urls["login_url"]
        # login_res = self.session.post(url_login, data=login_data, headers=self.headers)
        
    def tearDown(self) -> None:
        print("test ending....")

    def test_shopping_success(self):
        real_res = self.session.post(self.url, data=self.payload, headers=self.headers)
        # self.response.append(real_res.json())
        real_status = real_res.status_code
        # expect_msg = real_res.json()["success"]
        # real_msg = True
        self.assertEqual(real_status, 200, "响应正文不一致！")

if __name__ == "__main__":
    unittest.main()
'''