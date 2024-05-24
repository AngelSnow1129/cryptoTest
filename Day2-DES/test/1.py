list=[56, 21, 124, 1, 47, 4, 2, 62, 74, 4, 18, 20, 22, 61, 246, 89, 3, 11, 11, 96, 17, 42, 96, 83, 247, 124, 96, 84, 21, 33, 23, 86]
print(len(list))
# flag=[0]*32
a=32
# for i in range(a):
#     tmp[i] = ord(tmp[i]) - 9
#     tmp[i]^=0x33
#     # 51
#     temp[i]+=8
#     if i % 7 == 1:
#         tmp[i] ^ 119
#
# for i in range(a,2,-3):
#     tmp1=tmp[i-3]
#     tmp2 = tmp[i - 2]
#     tmp3 = tmp[i - 1]
#     print(tmp3,tmp2,tmp1)

# de

out=[0]*34
# print(out)
# for i in range(31,2,-3):
    # out[i-3]=list[31 - (i - 1)]
    # out[i-2]=list[31-(i-2)]
    # out[i - 1] = list[31-(i-3)]

out=list[::-1]
# for i in range(3,32,3):
#     out[i-3]=list[31 - (i - 1)]
#     out[i-2]=list[31-(i-2)]
#     out[i - 1] = list[31-(i-3)]
#
# print(out)
for i in range(a):
    if i % 7 == 1:
        out[i] ^ 119
    out[i] -= 8
    out[i]^=0x33 # 51
    out[i] = chr(out[i] + 9)

print(out)
# print(''.join(out))
list[-2] -= 8
list[-2] ^= 51  # 0x33 # 51
list[-2] = chr(list[-2] + 9)
temp=list[-2]
print("1",temp)

