masu = []
count = 0
masu = input()
length = len(masu)

for i in range(length):
    #print(i)
    if masu[i] == '1':
        count+=1

print(count)
