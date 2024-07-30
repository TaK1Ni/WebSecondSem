import time 

def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n-1)

def fact_it(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result


