n = [int(input()) for _ in range(5)]
mean = sum(n)//5
temp = ""
for i in range(4):
    for i in range(0,4-i):
        if n[i] > n[i+1]:
            temp = n[i]
            n[i] = n[i+1]
            n[i+1] = temp
print(mean)
print(n[2])