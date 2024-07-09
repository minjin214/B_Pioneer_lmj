x = input()
count = 0

while int(x) >= 10:
    y = 0
    for i in x:
        y += int(i)
    x = str(y)
    count += 1

print(count)

if (int(x)%3 == 0):
    print("YES")
else:
    print("NO")