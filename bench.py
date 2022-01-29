import time

def isPrime(n):
    i = 2
    while i<=n/2:
        if not (n%i):
            return 0
        i+=1
    return 1

def main():
    t = time.time()

    limit = 250001
    numPrimes = 0
    for i in range(2,limit+1):
        numPrimes+=isPrime(i)
    t = time.time()-t;
    print("\n"+str(numPrimes)+" primes found <"+str(limit)+" in "+str(t)+" sec using Python \n\n") 

if __name__ == "__main__":
    main()