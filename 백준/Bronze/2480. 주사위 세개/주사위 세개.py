dice = list(map(int, input().split()))

a, b, c = dice[0], dice[1], dice[2]

if a == b == c:
    prize = 10000 + a * 1000

elif a == b or a == c:
    prize = 1000 + a * 100

elif b == c:
    prize = 1000 + b * 100

else:
    prize = max(a, b, c) * 100

print(prize)