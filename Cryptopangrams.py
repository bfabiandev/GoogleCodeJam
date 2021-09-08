from math import gcd
from string import ascii_uppercase

T = int(input())
for i in range(1, T + 1):
    _, L = [int(k) for k in input().strip().split(' ')]
    numbers = [int(k) for k in input().strip().split(' ')]

    primes = [0] * (L + 1)

    primes[1] = gcd(numbers[0], numbers[1])
    for j in range(1, L):
        primes[j+1] = numbers[j] // primes[j]

    primes[0] = numbers[0] // primes[1]

    all_primes = sorted(list(set(primes)))
    pangram = [ascii_uppercase[all_primes.index(prime)] for prime in primes]
    pangram = ''.join(pangram)

    print('Case #{}: {}'.format(i, pangram))
