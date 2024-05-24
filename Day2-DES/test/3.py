#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/10/13 17:56 
# ide： PyCharm

a='7e0cad17016b0>?45?f7c>0>4a>1c3a0'
for x in a:
    print(chr(ord(x) ^ 7), end='')
