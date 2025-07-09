N = int(input())
n = int(input())
num = [int(input()) for i in range(0,N-1)]

cnt = 0

while True:
    if N==1:
        break
    num.sort()
    if (num[N-2] < n):
        break
    else:
        num[N-2] -= 1
        n += 1
        cnt += 1
print(cnt)