# sum every degit
def sum_degit(x):
    sum = 0
    if x < 10:
        return x
    for i in range(x):
        degit = x%10
        sum += degit
        x = int(x/10)
        if x == 0:
            return sum

N,A,B = [int(i) for i in input().split()]
ans = 0

for i in range(N+1):
    detect = sum_degit(i)
    #print(detect)
    if A<= detect<= B:
        #print('roop:{}'.format(i))
        ans+=i
print(ans)

