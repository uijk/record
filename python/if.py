#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import *

user_name = raw_input('请输入用户名：')
user_code = getpass("请输入密码:")


if user_name == 'a' and user_code == '123':
	print 'welcome ' + user_name
else:
	print 'login failed!'
