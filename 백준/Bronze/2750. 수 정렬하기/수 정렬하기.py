N = int(input())
n = [int(input()) for _ in range(N)]
temp = ""
for i in range(N-1):
    for i in range(0, N-1-i):
        if n[i] > n[i+1]:
            temp = n[i]
            n[i] = n[i+1]
            n[i+1] = temp
for i in range(N):
    print(n[i])