'''''
H, W = [int(i) for i in input().split()]
a = [list(input()) for i in range(H)]

for i in range(W):
    for m in range(H):
        if a[1][0:] == '.':
            del a[i][m:]
            break

print(a)
'''''

h, w = map(int, input().split())
a = [''] * h
for i in range(h):
    a[i] = input()

print(a)
row = [False] * h
col = [False] * w
print(row)
print(col)

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            row[i] = True
            col[j] = True

print(row)
print(col)

for i in range(h):
    if row[i]:
        for j in range(w):
            if col[j]:
                print(a[i][j], end='')
        print()