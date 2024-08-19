N = int(input())
n = list(map(int, input().split()))
n.sort()
result = 0
time = 0
for i in range(0,N):
    time += n[i]
    result += time
print(result)
        