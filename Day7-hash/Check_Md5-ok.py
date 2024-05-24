#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/11/24 15:39 
# ide： PyCharm

import hashlib
import os

def Check_Md5(picture_path):
    m = hashlib.md5()
    with open(picture_path, 'rb') as f:
        for line in f:
            m.update(line)

    return m.hexdigest()

path1=r'as.jpg'
path3=r'as - 副本.jpg'

print('读取路径为:'+os.path.abspath(path1))
print(Check_Md5(path1))
print('读取路径为:'+os.path.abspath(path3))
print(Check_Md5(path3))
if Check_Md5(path3)!=Check_Md5(path1):
    print("文件已经被修改！")
else:
    print("文件未被修改！")
