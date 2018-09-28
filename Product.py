def Odd_Even_determination(i):
    if i%2 == 1:
        print('Odd')
    else:
        print('Even')

a, b = [int(i) for i in input().split()]
multi = a*b
Odd_Even_determination(multi)

