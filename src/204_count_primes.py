#Sieve of Eratosthenes
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            primes = [1] * n
            primes[0] = primes[1] = 0
            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
            return sum(primes)
