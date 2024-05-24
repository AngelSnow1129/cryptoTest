#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/10/10 4:19 
# ide： PyCharm

str="string"
for index in range(0,len(str),2):
    print(str[index],str[index+1])

a=1
b=2

a,b=b,a
print(a,b)