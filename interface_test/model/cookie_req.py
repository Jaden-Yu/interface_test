'''
    作    用：      1、获取登录后的cookie值
    使用场景：
                    1、接口需要进行登录认证；
                    2、需要使用cookie 值跳过登录过程；
    Usage   ：
                    1、直接调用cookie_request() 函数

'''

import requests

def cookie_request():
    '''登录账号，获取对应的cookie 值'''
    login_url = ''
    login_params =""
    headers = ""
    req = requests.post(url=login_url,data=login_params,headers=headers,**kwargs)

    return req.cookies