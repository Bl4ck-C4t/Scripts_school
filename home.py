def isPrime(x):
    Prime = True
    c = 2
    if x == c:
        Prime = False
    while x > c:
        if x % c == 0:
            Prime = False
            break
        else:
            c += 1
    return Prime
    
def PrimeGen(N):
    number = 1
    while number < N:
        if isPrime(number):
            print(number)
        number += 1
    


def smallest(ls):
    small = ls[0]
    for x in ls:
        small = min(small,x)
    return small

            
def list_sort(ls):
    sorted_ls = []
    while len(ls) > 0:
        sorted_ls.append(smallest(ls))
        ls.remove(smallest(ls))
    return sorted_ls


def fibonacci(N):
    a = 0
    b = 1
    print(a)
    print(b)
    while b + a < N:
        a,b = b,a + b
        print(b)
        
