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
