"""Python之禅：kk产生26个大写字母的字符串；
testOnekey函数测试26个可能的密钥。"""

s1="""Jxu Pud ev Fojxed, ro Jyc Fujuhi
Ruqkjyvkb yi rujjuh jxqd kwbo.
Unfbysyj yi rujjuh jxqd ycfbysyj.
Iycfbu yi rujjuh jxqd secfbun.
Secfbun yi rujjuh jxqd secfbysqjut.
Vbqj yi rujjuh jxqd duijut.
Ifqhiu yi rujjuh jxqd tudiu.
Huqtqrybyjo sekdji.
Ifusyqb sqiui qhud'j ifusyqb udekwx je rhuqa jxu hkbui.
Qbjxekwx fhqsjysqbyjo ruqji fkhyjo.
Uhhehi ixekbt duluh fqii iybudjbo.
Kdbuii unfbysyjbo iybudsut.
Yd jxu vqsu ev qcrywkyjo, huvkiu jxu jucfjqjyed je wkuii.
Jxuhu ixekbt ru edu-- qdt fhuvuhqrbo edbo edu --erlyeki mqo je te yj.
Qbjxekwx jxqj mqo cqo dej ru erlyeki qj vyhij kdbuii oek'hu Tkjsx.
Dem yi rujjuh jxqd duluh.
Qbjxekwx duluh yi evjud rujjuh jxqd *hywxj* dem.
Yv jxu ycfbucudjqjyed yi xqht je unfbqyd, yj'i q rqt ytuq.
Yv jxu ycfbucudjqjyed yi uqio je unfbqyd, yj cqo ru q weet ytuq.
Dqcuifqsui qhu edu xedaydw whuqj ytuq -- buj'i te cehu ev jxeiu!"""

kk=""
for i in range(26):
    kk=kk+chr(i+65)  #chr产生一个字母，A~Z从65-90，a~z从97-122

def testOnekey(i):
    tep=''
    for c in s1:
        if c.upper() in kk:                     #upper()表示字母大写
            j=(kk.index(c.upper())+i) % 26      #kk.index返回某个字母的位置
            if ord(c)>96:
                tep=tep+kk[j].lower()           #lower()表示小写
            else:
                tep=tep+kk[j]
        else:
            tep=tep+c
    return tep

goodkey=0
for i in range(26):
    tmpstr=""
    tmpstr=testOnekey(i)
    if "Zen" in tmpstr:
        goodstr=tmpstr
        goodkey=i

print("goodkey is",goodkey)
print(30*"#","\n",goodstr)

