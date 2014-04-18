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
    https://projecteuler.net/problem=8

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

def p10():
    """
    Sum the primes up to 2,000,000
    https://projecteuler.net/problem=10

    """
    from primes import Primes
    return sum(Primes(2000000))

def p11():
    """
    Find the largest 4-in-a-row product in the grid
    https://projecteuler.net/problem=11

    """

    def product(nums):
        import sys
        from operator import mul
        from functools import reduce

        return reduce(mul, nums)

    grid = """
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """.split("\n    ")[1:-1]

    grid = [[int(num) for num in row.split(" ")] for row in grid]

    across    = lambda x, y: [grid[y][x + n] for n in range(4)]
    down      = lambda x, y: [grid[y + n][x] for n in range(4)]
    downright = lambda x, y: [grid[y + n][x + n] for n in range(4)]
    downleft  = lambda x, y: [grid[y + n][x - n] for n in range(4)]

    maxproduct = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if x <= len(grid) - 4:
                maxproduct = max(maxproduct, product(across(x, y)))
            if y <= len(grid) - 4:
                maxproduct = max(maxproduct, product(down(x, y)))

                if x <= len(grid) - 4:
                    maxproduct = max(maxproduct, product(downright(x, y)))
                if x >= 4:
                    maxproduct = max(maxproduct, product(downleft(x, y)))

    return maxproduct
