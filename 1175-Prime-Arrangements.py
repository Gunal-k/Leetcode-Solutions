class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Count primes from 1 to n
        prime_count = 0

        for num in range(2, n + 1):
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_count += 1

        # Number of non-primes
        non_prime_count = n - prime_count

        # k! * (n-k)!
        prime_arrangements = 1
        non_prime_arrangements = 1

        for i in range(2, prime_count + 1):
            prime_arrangements = (prime_arrangements * i) % MOD

        for i in range(2, non_prime_count + 1):
            non_prime_arrangements = (non_prime_arrangements * i) % MOD

        return (prime_arrangements * non_prime_arrangements) % MOD
