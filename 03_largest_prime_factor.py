# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
from functools import reduce

number = 600851475143


def get_prime_factors(number):
    n = number
    # является ли число натуральным
    is_prime = lambda x: all(x % i for i in range(2, x // 2 + 1))
    processing = True
    # простые множители
    prime_factors = []
    # генератор простых чисел
    prime_gen = (i for i in range(1, n) if is_prime(i))
    while processing:  
        num = prime_gen.__next__()
        if not(n % num):
            prime_factors.append(num)
            n = n / num
            if n == 1:
                processing = False
    return prime_factors    


def main():
    print(max(get_prime_factors(number)))


if __name__ == '__main__':
    main()