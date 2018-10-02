from Crypto.Cipher import AES

key_file=open("key.txt","rb")
encrypt_key=key_file.read()
key_file.close()

print("encrypt_key",encrypt_key)
length=len(encrypt_key)
print(length)

name=input("復号したいファイル名を入力してください:")
file=open(name,"rb")
encrypt_data=file.read()
file.close()

KEY2=input("password:")
print("password長",len(KEY2))
crypto=AES.new(KEY2)
print(crypto)
original_key=crypto.decrypt(encrypt_key)

print("original_key",original_key)

crypto=AES.new(original_key)
original_data=crypto.decrypt(encrypt_data)
original_data=original_data.decode("utf-8")
original_data=original_data.rstrip(" ")
print("復号:",original_data)
print(len(original_data))
file=open(name,"w")
file.write(original_data)
file.close()