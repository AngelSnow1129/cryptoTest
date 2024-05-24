#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/9/26 15:36 
# ide： PyCharm

"""
仿射密码，加密y=k1*x+k2；解密为x=k1‘(y-k2)
"""

message="""
I love you not because of who you are, but because of who I am when I am with you.
"""

kk='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

E_key=[7,3]
D_key=[15,3]
goodkey=[1,3,5,7,9,11,15,17,19,21,23,25]        #12个和26互素的整数

# encrypt part
def E(k1,k2,text):       #加密函数
    tep=''
    for c in text:
        if c.upper() in kk:                     #upper()表示字母大写
            i=kk.index(c.upper())               #kk.index返回某个字母的位置
            j= (k1*i+k2) % 26
            if ord(c)>96:
                tep=tep+kk[j].lower()           #lower()表示小写,ord(c)>96说明是小写字母
            else:
                tep=tep+kk[j]
        else:
            tep=tep+c
    return tep

# decrpt part
def D(k1,k2,text):       #解密函数
    tep=''
    for c in text:
        if c.upper() in kk:                     #upper()表示字母大写
            i=kk.index(c.upper())
            j= k1*(i-k2) % 26
            if 123>ord(c)>96:
                tep=tep+kk[j].lower()           #lower()表示小写
            else:
                tep=tep+kk[j]
        else:
            tep=tep+c
    return tep

# judge the keys
def gcd(k1,k2):
    t = 0
    while (k2!=0):
        t = k2
        k2 = k1%k2
        k1 = t
    return k1


if __name__=="__main__":
    # 获取密钥
    print ("开始访射加密...密钥有2个参数")
    # key1=0
    # while (key1 not in goodkey):
    #     key1 = int(input('请输入第一个密钥，和26互素:\n'))
    # key2 = int(input('请输入第二个密钥:\n '))
    key1, key2 = map(int, input('请输入两个加密密钥(以空格隔开)：\n').split())
    while (gcd(key1, 26) & gcd(key2, 26 & gcd(key1,key2)))!= 1:
        key1, key1 = map(int, input('存在不互素的密钥，请重新输入密钥：\n').split())
    E_key[0]=key1
    E_key[1]=key2

    tmp=E(E_key[0],E_key[1],message)
    print ("密文为:",tmp)

    D_key[0]=key1**11 % 26                  #快速求逆，这里用了欧拉定理求逆
    D_key[1]=key2

    print ("明文为:",D(D_key[0],D_key[1],tmp))
