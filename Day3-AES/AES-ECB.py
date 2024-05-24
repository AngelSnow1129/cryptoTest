#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/10/27 14:36 
# ide： PyCharm

"""
ECB没有偏移量
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

# b2a_hex     字符串 --> 十六进制
#
# a2b_hex     十六进制 -->字符串

# 不足十六位填充到16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)

    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    e = encrypt("Hello Winter!")  # 加密
    d = decrypt(e)  # 解密
    print("加密:", e)
    print("解密:", d)