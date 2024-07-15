hat = [int(input()) for _ in range(9)]

sum_hat = sum(hat)

for i in range(8):
    for j in range(i+1, 9):
        if sum_hat - (hat[i] + hat[j]) == 100:
            a = hat[i]
            b = hat[j]
            break

hat.remove(a)
hat.remove(b)
hat.sort()

for i in hat:
    print(i)