
import timeit

def primes():
    n = 20000
    for p in range(2, n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            print p

print timeit.timeit(primes, number=1), "seconds"
