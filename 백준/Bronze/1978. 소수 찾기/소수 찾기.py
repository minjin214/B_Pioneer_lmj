case = int(input())
N = list(map(int, input().split()))
n = []
for i in range(case):
    num = True
    if N[i] < 2:
        num = False
    else:
        for j in range(2, N[i]):
            if N[i]%j == 0:
                num = False
                break
    if num==True:
        n.append(N[i])
    
print(len(n))