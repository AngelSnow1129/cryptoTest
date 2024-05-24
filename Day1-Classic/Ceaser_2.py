import random

# message='''
# Don’t cry because it is over, smile because it happened.
# Don’t try so hard, the best things come when you least expect them to.
# To the world you may be one person, but to one person you may be the world.
# Don’t waste your time on a man/woman, who isn’t willing to waste their time on you.
# Just because someone doesn’t love you the way you want them to, doesn’t mean they don’t love you with all they have.
# I love you not because of who you are, but because of who I am when I am with you.
# No man or woman is worth your tears, and the one who is,won’t make you cry.
# The worst way to miss someone is to be sitting right beside them knowing you can’t have them.
# Never frown, even when you are sad, because you never know who is falling in love with your smile.
# Maybe God wants us to meet a few wrong people before meeting the right one, so that when we finally meet the person, we will know how to be grateful.
# '''

message="I love you not because of who you are, but because of who I am when I am with you."

# encrypt part
def encrpt(message,number):
    encrypt_message=""
    for index in message:
        calc=0;
        change=""
        if 64 < ord(index) < 91:
            calc = (ord(index) - 65 + number) % 26 + 65;

            # change= index.lower();
            # continue;
        elif 96 < ord(index) < 123:
            calc = (ord(index) - 97 + number) % 26 + 97;
            # change = index.upper();
        else:
            encrypt_message += index;
            continue;
        encrypt_message += chr(calc);

    return encrypt_message

# decrypt part
def decrpt(encrypt_message,decrypt_message):
    # decrypt_message=""
    for i in range(0,26):
        decrypt_message_temp="";
        for index in encrypt_message:
            temp=0;
            calc=ord(index);
            if 64<calc<91 :
                calc=(calc-65+i)%26+65;
                # continue;
            elif 96<calc<123 :
                calc=(calc-97+i)%26+97;
            else:
                decrypt_message_temp +=index;
                continue;
            decrypt_message_temp+=chr(calc);
        decrypt_message.append(decrypt_message_temp);

    for i in decrypt_message:
        if "love"  in i:print("Suceess!\n解密结果如下：\n"+i);decrypt_message_get=i;

    return decrypt_message_get,decrypt_message

if __name__ == '__main__':
    # message = input("Please Input the message to encryt:\n");
    # message = "I love snow"
    encrypt_message = ""
    decrypt_message = [];
    number = random.randint(1, 26);                     # use the random bunber to encrypt.
    # number=3;                                         # typical ceaser mima.
    # number=input("加密的偏移设置(1-25)：\n")
    # print(number)
    encrypt_message=encrpt(message, number);            # encrypt the message
    print("获取到的密文如下：\n"+encrypt_message+"\n开始解密：");
    decrypt_message,Baopo_table=decrpt(encrypt_message,decrypt_message);            # decrypto the message
    print("解密结束！",end="")
    if(decrypt_message==message):print("解密成功!");
    else:print("解密失败~");


