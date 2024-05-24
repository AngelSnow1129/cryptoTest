#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： snow
# datetime： 2021/9/26 15:37 
# ide： PyCharm
import numpy as np

key = ''
message = ''
words=[]
for i in range(0,26):
    words.append(chr(ord('A')+i))

# 制作5*5的密码表
def create_table(key):
    key = key.replace('i', 'j').replace('I', 'j')
    specialChars = "!#$%^&*()"
    for specialChar in specialChars:
        key = key.replace(specialChar, '')
    # print(key)                  # 输出替换过后的key
    strings = ''.join(Unique_strings(key.upper()))
    # print(strings)                    # 输出大写的表格
    strings = strings.replace('I', '');

    word = np.array(list(strings))
    table_box = np.reshape(word, (5, 5))

    return table_box
# 去除生成密码本时的重复的字符串
def Unique_strings(string):
    listl = list(string)
    string=listl+words
    listl = list(string)
    lists = list(set(listl))
    lists.sort(key=listl.index)
    return ''.join(lists)
# 将输入的明文进行处理
def get_input(string_list):
    for i in range(len(string_list)):
        if (i % 2 == 1):  # 列表中的第d奇数个
            if (string_list[i] == string_list[i - 1]):  # 第奇数个与前一个(偶数)是否相同
                string_list.insert(i, "X")  # 有重复明文字母则插入一个填充字母Z 并且退出循环
                break
    return string_list
# 将输入的明文进行处理2
def input_progress(message):
    specialChars = "!#$%^&*()";
    flag=1
    i=0
    message=message.replace('I','J').replace('i','J')
    while(flag==1):
        if i+1>=len(message):
            break;
        if (message[i] not in specialChars )& (message[i]==message[i+1]):
            list_mes=list(message)
            list_mes.insert(i+1,'X')
            message=''.join(list_mes)
            i=i+2
        else:
            i=i+2

    # print(message.upper())
    # print("len:",len(message))
    if len(message)%2==1:
        list_mes = list(message)
        list_mes.append('X')
        message = ''.join(list_mes)

    return message

# 加密
def encrpto(string,table_box):
    encrpto_message=''
    string=string.upper()
    for index in range(0, len(string), 2):
        x=string[index]
        y=string[index + 1]
        posx=np.argwhere(table_box==x)
        posy=np.argwhere(table_box==y)
        if posx[0][0] == posy[0][0]  :
            # x 横坐标,同一行
            posx[0][1]=(posx[0][1]+1)%5
            posy[0][1] = (posy[0][1] + 1) % 5
        elif posx[0][1] == posy[0][1]  :
            posx[0][0]=(posx[0][0]+1)%5
            posy[0][0] = (posy[0][0] + 1) % 5
        else:
            posx[0][1],posy[0][1] = posy[0][1],posx[0][1]

        # print(posx[0][1],posy[0][1])
        # x1=posx[0][0];x2=posy[0][0];y1=posx[0][1];y2=posy[0][1];
        encrpto_message+=table_box[posx[0][0],posx[0][1]]
        encrpto_message += table_box[posy[0][0], posy[0][1]]
    #     encrpto_message+=table_box(x1,y1)
    #     encrpto_message += table_box(x2,y2)

    return encrpto_message

# decrypto 解密

def decrypto(string,table_box):
    encrpto_message=''
    string=string.upper()
    for index in range(0, len(string), 2):
        x=string[index]
        y=string[index + 1]
        posx=np.argwhere(table_box==x)
        posy=np.argwhere(table_box==y)
        if posx[0][0] == posy[0][0]  :                 # x 横坐标,同一行
            posx[0][1]=(posx[0][1]-1)%5
            posy[0][1] = (posy[0][1] - 1) % 5
        elif posx[0][1] == posy[0][1]  :
            posx[0][0]=(posx[0][0]-1)%5
            posy[0][0] = (posy[0][0] - 1) % 5
        else:
            posx[0][1],posy[0][1] = posy[0][1],posx[0][1]

        # print(posx[0][1],posy[0][1])
        x1=posx[0][0];x2=posy[0][0];y1=posx[0][1];y2=posy[0][1];
        encrpto_message+=table_box[posx[0][0],posx[0][1]]
        encrpto_message += table_box[posy[0][0], posy[0][1]]
    #     encrpto_message+=table_box(x1,y1)
    #     encrpto_message += table_box(x2,y2)

    return encrpto_message

# 输出
def output_progress(message):
    flag = 1
    i = 0
    listtable = []
    while (flag == 1):
        String1=""

        if i + 1 >= len(message):
            break;
        # if i==0:
        #     continue;
        # el
        if i<len(message)-2:
            if (message[i+1]=='X') & (message[i]==message[i+2]):
                listtable.append(i+1);
                # list_mes=list(message)
                # # list_mes.insert(i+1,'X')
                # del list_mes[i+1]
                # message=''.join(list_mes)

        i = i + 2
    list_mes=list(message)
    listtable.sort( reverse=True)
    for i in listtable:
        list_mes.pop(i)
        # del list_mes[list1]
    message=''.join(list_mes)
    # print(message.upper())
    print("len:", len(message))
    if (len(message) % 2 == 0)&(message[-1]=='X'):
        list_mes = list(message)
        list_mes.pop()
        message = ''.join(list_mes)

    return message

# def test(menu):
#     # 秘钥以及置换表生成
#     key=''
#     message=''
#     if menu==1:
#         key = "playfairI"
#         message = "I LOVE SNOW!"
#     elif menu==2:
#         key = input("请输入秘钥：\n\r");
#         message = input("请输入加密字符串：\n\r")
#
#     table_box=create_table(key)
#     # message="I LOVE SNOW!"
#     # message="teeeessste"
#
#     # 输入加密，输出密文
#     message=input_progress(message)
#     encrypto_message=encrpto(message,table_box)
#     print("encrypto message:",encrypto_message)
#
#     # 输出解密，输出解密结果
#     decrypto_message=decrypto(encrypto_message,table_box)
#     print("Decrypto:")
#     # print(decrypto_message)
#
#     output_message=output_progress(decrypto_message)
#     print("res:",output_message)
#     print(output_message[-1])
#
#     return
if __name__ == '__main__':
    menu=0
    while((menu==0)):
        menu = int(input("请输入运行方式：\n\r 1.默认明文密码演示.\n\r 2.自定义明文密文演示.\n\r"))
        if (menu!=1)&(menu!=2):
            menu=0
        print("请输入正确的运行方式！")
    # 秘钥以及置换表生成
    key = ''
    message = ''
    if menu == 1:
        key = "playfairI"
        message = "ILOVESNOW"
    elif menu == 2:
        key = input("请输入秘钥：\n\r");
        message = input("请输入加密字符串：\n\r")
    # key=Unique_strings(key)
    table_box = create_table(key)
    print("Message:",message)
    # message="I LOVE SNOW!"
    # message="teeeessste"

    # 输入加密，输出密文
    message = input_progress(message)
    encrypto_message = encrpto(message, table_box)
    print("encrypto message:", encrypto_message)

    # 输出解密，输出解密结果
    decrypto_message = decrypto(encrypto_message, table_box)
    print("Decrypto:",decrypto_message)
    # print(decrypto_message)

    output_message = output_progress(decrypto_message)
    print("res:", output_message)

    print("End~")
