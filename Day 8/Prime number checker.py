def isPrime(num):
    if num == 0:
        print(f"{num} is not prime.")
        return
    elif num == 1:
        print(f"{num} is not prime.")
        return
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not prime.")
                return
    print(f"{num} is prime.")

n=int(input("Check is the number prime or not: "))
isPrime(num=n)
