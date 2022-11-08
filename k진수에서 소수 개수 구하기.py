import math

def trans(n,k):
    result = ""
    while(n>k):
        result += str(n%k)
        n = n//k
    result += str(n)
    result = result[::-1]
    return result

def is_prime(n):
    can_divine = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i == 0:
            can_divine += 1
    if can_divine == 0:
        return True
    else:
        return False

def solution(n, k):
    primes = []
    answer = 0

    trans_n = trans(n,k)

    numbers = trans_n.split('0')

    for i in numbers:
        if i == '2':
            answer += 1
        elif i != '1' and i != '' and is_prime(int(i)):
            answer += 1

    return answer