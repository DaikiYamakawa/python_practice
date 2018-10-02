from Crypto.Cipher import AES
import secrets

random=secrets.randbits(256)
random=str(random)
KEY=secrets.choice(random)
while True:
    key_length = len(KEY)
    if key_length<16:
      add_KEY=secrets.choice(random)
      KEY=KEY+add_KEY
    else:
      break

KEY2=secrets.choice(random)
while True:
    key_length = len(KEY2)
    if key_length<16:
      add_KEY=secrets.choice(random)
      KEY2=KEY2+add_KEY
    else:
      break

print("original_key",KEY)
print("password:",KEY2)

name=input("暗号化したいファイル名を入力してください:")
file=open(name,"r",encoding="utf-8")
f_data=file.read()
file.close()

length=len(f_data)
print("data")
print(f_data)
print(length)

key_size=16
pad_size=key_size-(length%key_size)
padded_data = f_data + (" "*pad_size)
padded_length=len(padded_data)
print("paded_data")
print(padded_data)
print(padded_length)

crypto=AES.new(KEY)
encrypt_data=crypto.encrypt(padded_data)

f_data=padded_data.rstrip(" ")
print("元データ長",len(f_data))

print("暗号化：",encrypt_data)
file=open(name,"wb")
file.write(encrypt_data)
file.close()

crypto=AES.new(KEY2)
encrypt_key=crypto.encrypt(KEY)
print("encrypt_key:",encrypt_key)
print(len(encrypt_key))
key_file=open("key.txt","wb")
key_file.write(encrypt_key)
key_file.close()

