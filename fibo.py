from math import sqrt

#Recursion
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
      
# binet
def binet(n):
    phi1 = (1+sqrt(5)) / 2
    phi2 = (1-sqrt(5)) / 2
    return round((phi1**n - phi2**n) / sqrt(5))

if __name__ == '__main__':
    fibo(6)
