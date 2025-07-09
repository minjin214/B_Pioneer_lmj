plate = list(input())
h = 10
for i in range(0,len(plate)-1):
    if plate[i+1] == plate[i]:
        h += 5
    else:
        h += 10
print(h)