import math

def fill_sieve(sieve, n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

def display_primes(sieve):
    primes = [str(i) for i in range(2, len(sieve)) if sieve[i]]
    print("Liczby pierwsze z przedziału 2..100")
    print(", ".join(primes))

def main():
    n = 100
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    fill_sieve(sieve,n)
    display_primes(sieve)

if __name__ == "__main__":
    main()