def factorial(n):
    print("factorial called ", str(1))
    if n < 2:
        print("returning 1")
        return 1
    return n * factorial(n-1)

factorial(5)
