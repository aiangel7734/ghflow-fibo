from math import sqrt

# binet
def binet(n):
    phi1 = (1+sqrt(5)) / 2
    phi2 = (1-sqrt(5)) / 2
    return round((phi1**n - phi2**n) / sqrt(5))

if __name__ == '__main__':
    fibo(6)
