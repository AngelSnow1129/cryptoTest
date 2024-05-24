#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/11/24 15:32 
# ide： PyCharm

# os模块

import  os

print (os.getcwd()) #获取当前工作目录路径
print (os.path.abspath('.')) #获取当前工作目录路径
print (os.path.abspath('test.txt')) #获取当前目录文件下的工作目录路径
print (os.path.abspath('..')) #获取当前工作的父目录 ！注意是父目录路径
print (os.path.abspath(os.curdir)) #获取当前工作目录路径

