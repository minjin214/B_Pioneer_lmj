N, k = map(int, input().split())
x = list(map(int, input().split()))
tmp = ""
for i in range(N-1):
    for i in range(0, N-1-i):
        if x[i] < x[i+1]:
            tmp = x[i]
            x[i] = x[i+1]
            x[i+1] = tmp
print(x[k-1])