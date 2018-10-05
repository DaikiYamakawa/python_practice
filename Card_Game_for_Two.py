Alice = 0
Bob = 0

N = int(input())
a = sorted([int(i) for i in input().split()], reverse=False)

for i in range(N):
    a_length = len(a)
    if a_length == 1:
        Alice += a.pop()
        break
    if a_length == 0:
        break
#    if N <= i+1:
#        break
    Alice += a.pop()
    Bob += a.pop()

ans = Alice - Bob
#print('Alice:{}'.format(Alice))
#print('Bob:{}'.format(Bob))
print(ans)

