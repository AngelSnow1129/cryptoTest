import random

message="I Love You"
encrypt_message=""
decrypt_message=[];

# encrypt
number=random.randint(1,26);
# number=3;
# print(number)
# def encrpt(message,number):
print("message:"+message)
for index in message:
    calc=0;
    if 64 < ord(index) < 91:
        calc = (ord(index) - 65 + number) % 26 + 65;
        # continue;
    elif 96 < ord(index) < 123:
        calc = (ord(index) - 97 + number) % 26 + 97;
    else:
        encrypt_message += index;
        continue;
    encrypt_message += chr(calc);

# decrypto
# def decrpt(encrypt_message,number):
print("encrypt_message:"+encrypt_message)
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
    if "Love" in i:print("Suceess!\nMessage:"+i)



