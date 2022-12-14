def sieve(n):
    candidates= list(range(2,n+1))
    primes = [1]
    while len(candidates) > 0:
        nextPrime = candidates.pop(0)
        primes.append(nextPrime)
        idx = 0
        while idx < len(candidates):
            if candidates[idx]%nextPrime==0:
                candidates.pop(idx)
            else:
                idx += 1
    return primes

def main():
    print("sieve of eratosthenes\n")
    n = int(input("enter limit "))
    primes =sieve(n)
    print(primes)

if __name__ == '__main__':
    main()