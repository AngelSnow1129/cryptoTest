#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/11/24 15:07 
# ide： PyCharm

import hashlib
import sys
import os
# print (sys.argv[0])

def Check_Md5(picture_path):
    m = hashlib.md5()
    with open(picture_path, 'rb') as f:
    # with open(r'./as.jpg','rb') as f:
        for line in f:
            m.update(line)

    return m.hexdigest()
    # print(m.hexdigest())

path1=r'as.jpg'
path2=r'as -2.jpg'
path3=r'as - 副本.jpg'

# print (os.path.abspath('.')) #获取当前工作目录路径
print('读取路径为:'+os.path.abspath(path1))
print(Check_Md5(path1))
print('读取路径为:'+os.path.abspath(path3))
print(Check_Md5(path3))
if Check_Md5(path3)!=Check_Md5(path1):
    print("文件已经被修改！")
else:
    print("文件未被修改！")
