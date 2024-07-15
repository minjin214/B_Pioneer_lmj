a = []
b = []
for i in range(28):
    num = int(input())
    a.append(num)
for j in range(1,31):
    if j not in a:
        b.append(j)
print(min(b))
print(max(b))