import math

def make_prime_list(num):
    if num < 2:
        return []

    prime_list = [i for i in range(num+1)]
    prime_list[1] = 0
    num_sqrt = math.sqrt(num)

    #素数ではないものを0にしていく
    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2*prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]

N = int(input())
count = 0
prime_lis = []
if N%2 == 0:
    print('0')
    exit()

prime_list = make_prime_list(N)
print(prime_list)


for prime in prime_list:
    prime_list = prime
    while N%prime == 0:
        N = N / prime
        prime_lis.append(prime)
        count+=1

print(count)
print(prime_lis)
