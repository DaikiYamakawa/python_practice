fivehundred_count = int(input())
hundred_count = int(input())
fifty_count = int(input())
sum_coins = int(input())
ans = 0

for i in range(fivehundred_count+1):
#    print('i:{}'.format(i))
    for m in range(hundred_count+1):
#        print('m:{}'.format(m))
        for n in range(fifty_count+1):
#            print('n:{}'.format(n))
            sumcoins = 500*i+100*m+50*n
#            print('sumcoins:{}'.format(sumcoins))
            if sum_coins == 500*i+100*m+50*n:
                ans+=1
#                print('ans:{}'.format(ans))
                break

print(ans)



