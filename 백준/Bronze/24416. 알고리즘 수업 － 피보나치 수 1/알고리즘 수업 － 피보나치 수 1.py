n = int(input())

def fib(n):
    f = [1]*(n+1)
    for i in range(3,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

def fibonacci(n):
    return n-2

print(fib(n), fibonacci(n))
