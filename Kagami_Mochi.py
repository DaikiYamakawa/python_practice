N = int(input())
d = []
e = []
count_flag = 0
count = 0
for i in range(N):
    d.append(int(input()))
    e.append(d[i])
    flag = 0
    for m in range(i):
#        print('e[{}]:{} == d[{}]:{}'.format(m,e[m],i,d[i]))
        if e[m] == d[i]:
            flag = 1
            count_flag+=1
#            print('d[{}]:{}'.format(i,d[i]))
#            print('count_flag:{}'.format(count_flag))
            break
#        else:
#            print('elsed[{}]:{}'.format(i,d[i]))
#            break
    if i == 0:
        count+=1
        Max_mochi = d[i]
        Min_mochi = d[i]
    elif Min_mochi > d[i]:
        Min_mochi = d[i]
        count+=1
#        print('Min_mochi:{}'.format(Min_mochi))
    elif Max_mochi < d[i]:
        Max_mochi = d[i]
        count+=1
#       print('Max_mochi:{}'.format(Max_mochi))
    elif flag == 1:
        continue
    else:
        count+=1
#    print('ans:{}'.format(count))

#print(d)
#print(e)
#print(count_flag)
print(count)
