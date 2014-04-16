#!/usr/bin/env python3
"""
My solutions to the Project Euler problems

Jack Wearden, 2014

"""

def p1():
    """
    Sum all of the multiples of 3 or 5 up to 1000
    https://projecteuler.net/problem=1

    """

    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

def p2():
    """
    Sum all of the evens in the fibonacci series 1, 2 -> 1000
    https://projecteuler.net/problem=2

    """
    def fib(a, b, stop):
        yield a
        yield b
        while a < stop:
            a, b = b, a+b
            yield b

    return sum(i for i in fib(1, 2, 4000000) if i % 2 == 0)

def p3():
    """
    Give the largest prime factor of 600851475143
    https://projecteuler.net/problem=3

    """
    def is_prime(n):
        return not any(n % i == 0 for i in range(3, int(n**0.5) + 1))

    def factorise(n):
        for i in range(3, int(n**0.5) + 1):
            if n % i == 0:
                return i, (n / i)

    factors = {600851475143}
    while any(not is_prime(n) for n in factors):
        new_factors = set()
        for n in factors:
            f = factorise(n)
            if f != None:
                new_factors.update(set(f))
        factors = new_factors
    return max(factors)

def p4():
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    https://projecteuler.net/problem=4

    """
    def is_palindrome(n):
        s = str(n)
        return s[::-1] == s

    def products():
        for i in range(100, 1000):
            for j in range(100, 1000):
                yield i * j

    return max(n for n in products() if is_palindrome(n))

def p5():
    """
    Find the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20
    https://projecteuler.net/problem=5

    """
    from itertools import count
    def divisible(n):
        return all(n % i == 0 for i in range(1, 21))
    return next(filter(divisible, count(20, 20)))

def p6():
    """
    Find the difference between the sum of squares and square of
    the sum of numbers from 1 to 100
    https://projecteuler.net/problem=6

    """

    sumsq = sum(i**2 for i in range(101))
    sqsum = sum(range(101))**2

    return sqsum - sumsq

def p7():
    """
    Print the 10001st Prime number
    https://projecteuler.net/problem=7

    """

    from primes import Primes

    primes = iter(Primes())

    for i in range(10000):
        next(primes)

    return next(primes)

def p8():
    """
    [Python 3 only - had trouble with reduce I couldn't fix cleanly]
    Print the largest product of 5 consecutive numbers in the string
    https://rojecteuler.net/problem=8

    """

    bignum = """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    """.replace("\n    ", "")

    def products():
        import sys
        from operator import mul
        from functools import reduce
        for i in range(0, len(bignum) - 5):
            yield reduce(mul, (int(n) for n in bignum[i:i+5]))

    return max(products())

def p9():
    """
    Find a*b*c where a+b+c == 1000 and a**2 + b**2 == c**2
    https://projecteuler.net/problem=9

    """
    for c in range(1, 1000):
        for b in range(1, c):
            for a in range(1, b):
                if a+b+c == 1000:
                    if a*a + b*b == c*c:
                        return a*b*c
