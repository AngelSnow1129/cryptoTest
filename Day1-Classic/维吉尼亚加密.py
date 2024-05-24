#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/9/26 15:37 
# ide： PyCharm

def vigenere_shift(message, key, operation):
    key_list = []
    letter = 0
    ciphertext = ""

    key = key.lower()
    for byte in key:
        key_list.append(ord(byte))

    for i in range(len(key_list)):
        if operation == 'e':
            key_list[i] = (key_list[i] - 97) % 26
        else:
            key_list[i] = -(key_list[i] - 97) % 26

    print("密钥为:", key_list)
    for m in message:
        chr_enc = shiftOnekey(m, key_list[letter])
        ciphertext = ciphertext + chr_enc
        letter += 1
        if letter == len(key):
            letter = 0
    final = ''.join(ciphertext)
    return final


def shiftOnekey(c, key):
    tep = ''
    kk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if c.upper() in kk:  # upper()表示字母大写
        j = (kk.index(c.upper()) + key) % 26  # kk.index返回某个字母的位置
        if ord(c) > 96:
            tep = tep + kk[j].lower()  # lower()表示小写
        else:
            tep = tep + kk[j]
    else:
        tep = tep + c
    return tep


if __name__ == "__main__":
    print("维吉尼亚加密")
    # message = input('Enter Message: \n')
    # key = input('Enter Key: \n')

    message="I love snow!"
    key="I love spring!"
    operation = input('请输入加密还是解密：(D)ecrypt or (E)ncrypt: \n')
    final = vigenere_shift(message, key, operation)
    print(final)
    message=final
    operation = input('(D)ecrypt or (E)ncrypt: \n')
    final = vigenere_shift(message, key, operation)
    print(final)
