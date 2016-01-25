# -*- coding= utf-8 -*-

r'''
uiilities for Project LFE
'''

__author__ = 'LiuXiao'

import os
import subprocess
from selenium import webdriver


def get_connection():
    wd = webdriver.PhantomJS()
    return wd


def logout(username, passwd):
    wd = get_connection()
    wd.get('10.0.0.55')
    UI_username = wd.find_element_by_id('loginname')
    UI_passwd = wd.find_element_by_id('password')
    UI_username.clear()
    UI_username.send_keys(username)
    UI_passwd.clear()
    UI_passwd.send_keys(passwd)
    UI_logout = wd.find_element_by_link_text('注销')
    # UI_logout = (wd.find_elements_by_class_name('a_demo_two'))[1]
    UI_logout.click()
    # check javascript confirm window
    UI_confirm = wd.switch_to().alert
    UI_confirm.accept()
    UI_confirm = wd.switch_to().alert
    result = False
    if UI_confirm.text == '注销成功，请等1分钟后登录。':
        result = True
    UI_confirm.accept()
    wd.quit()
    return result


def login(username, passwd):
    wd = get_connection()
    wd.get('10.0.0.55')
    UI_username = wd.find_element_by_id('loginname')
    UI_passwd = wd.find_element_by_id('password')
    UI_username.clear()
    UI_username.send_keys(username)
    UI_passwd.clear()
    UI_passwd.send_keys(passwd)
    UI_login = wd.find_elements_by_id('button')
    UI_login.click()
    wd.quit()


def test_account(username, passwd):
    if logout(username, passwd):
        return True
    else:
        return False


def am_I_online():
    fnull = open(os.devnull, 'w')
    result = subprocess.call('ping fanyi.youdao.com', shell=True, stdout=fnull, stderr=fnull)
    fnull.close()
    if result:
        return False
    else:
        return True


if __name__ == '__main__':
    print(am_I_online())
