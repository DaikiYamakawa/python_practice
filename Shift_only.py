import numpy as np

def detector(list, size):
    for i in range(size):
        if list[i]%2 == 1:
            return 1

count_inputnumber = int(input())
inputnumber = np.array([int(i) for i in input().split()])
ans = 0

while True:
    finish_detector = detector(inputnumber, count_inputnumber)
    if finish_detector == 1:
        break
    inputnumber= inputnumber/ 2
    ans+=1

print(ans)
