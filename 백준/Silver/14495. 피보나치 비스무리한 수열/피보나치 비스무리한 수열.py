n = int(input())
f = [1]*(n+1)
for i in range(4,n+1):
    f[i] = f[i-3] + f[i-1]
    
print(f[n])