#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/9/29 15:54 
# ide： PyCharm
import zipfile
import string
import binascii


def CrackCrc(crc):
    for i in dic:
        for j in dic:
            for p in dic:
                # for q in dic:
                s = i + j + p
                if crc == (binascii.crc32(s)):
                    # 在 Python 2.x 的版本中，binascii.crc32 所计算出來的 CRC 值域为[-2^31, 2^31-1] 之间的有符号整数，为了要与一般CRC结果作比对，需要将其转为无符号整数，所以加上& 0xffffffff来进行转换。如果是 Python 3.x 的版本，其计算结果为 [0, 2^32-1] 间的无符号整数，因此不需额外加上& 0xffffffff
                    # print s
                    f.write(s)
                    return


def CrackZip():
    for I in range(36):
        file = 'flag' + str(I) + '.zip'
        f = zipfile.ZipFile(file, 'r')
        GetCrc = f.getinfo('flag.txt')
        crc = GetCrc.CRC
        # 以上3行为获取压缩包CRC32值的步骤
        # print hex(crc)
        CrackCrc(crc)

def CrackZip2():
    # for I in range(36):
        file = '43.zip'
        f = zipfile.ZipFile(file, 'r')
        GetCrc = f.getinfo('e.txt')
        crc = GetCrc.CRC
        # 以上3行为获取压缩包CRC32值的步骤
        # print hex(crc)
        CrackCrc(crc)

dic = string.ascii_letters + string.digits + '+/='

f = open('out.txt', 'w')
CrackZip2()
f.close()
