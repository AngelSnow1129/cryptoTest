#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/11/10 15:21 
# ide： PyCharm


# 中国剩余定理

def ex_euclid(a, b):  # a*x = 1 mod b ,求逆元x
    x1 = 1;
    x2 = 0;
    x3 = b
    y1 = 0;
    y2 = 1;
    y3 = a

    while y3 != 1:
        if y3 == 0:
            return 0  # 没有逆元
        Q = x3 / y3
        t1 = x1 - Q * y1;
        t2 = x2 - Q * y2;
        t3 = x3 - Q * y3
        x1 = y1;
        x2 = y2;
        x3 = y3
        y1 = t1;
        y2 = t2;
        y3 = t3
    return y2 % b  # 如果结果为负数，必须求模返回一个正数


# """求最大公约数"""
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def getnum(step=0):  # step为1不用判断输入数是否互质
    list1 = [1, ]
    while 1:
        # a = raw_input("请输入(以'.'字符结束):")
        a = input("请输入(以'.'字符结束):")
        if a == '.': break
        flag = 0
        for x in list1:
            if gcd(x, eval(a))!=1:
                flag = 1
        if flag == 0 or step == 1:
            list1.append(eval(a))
        else:
            print(            "不是互质的数，请接着输入...")
    return list1[1:]

def chinasy():
    print("开始中国剩余计算，第一步输入互质的模数m:")
    m = getnum(step=0)
    print(    "模数序列m为:", m)
    print("\n第二步输入求模的余数b:")
    b = getnum(step=1)
    print(    "余数序列b为:", b)

    M_all = 1
    for x in m:
        M_all = M_all * x
    c = [M_all / x for x in m]
    print   ("模积序列Mi为:", c)

    y = map(lambda x, y: ex_euclid(x, y), c, m)
    print (   "逆元序列y为:", y)

    end = []
    for i in range(len(m)):
        end.append(b[i] * c[i] * y[i])

    x = reduce((lambda x, y: x + y), end) % M_all
    print(    "结果为:", x)
    return x


if __name__ == "__main__":
    chinasy()

