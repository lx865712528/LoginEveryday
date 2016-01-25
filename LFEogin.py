# -*- coding: utf-8 -*-

r'''
Project Login Everyday, code name LFE
'''

__author__ = 'LiuXiao'

import time
import LFEutils as me


def Main():
    username = input('Please input your username: ')
    passwd = input('Please input your passwd: ')
    if not me.test_account(username, passwd):
        print('Wrong account info, you may try again.')
        return
    else:
        print()
    while True:
        if not me.am_I_online():
            me.login(username, passwd)
        # sleep the whole day
        time.sleep(86400)


if __name__ == '__main__':
    Main()
