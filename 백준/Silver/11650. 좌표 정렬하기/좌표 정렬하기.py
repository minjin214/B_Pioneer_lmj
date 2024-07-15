n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

xy.sort()

for i in range(n):
    print(xy[i][0], xy[i][1])