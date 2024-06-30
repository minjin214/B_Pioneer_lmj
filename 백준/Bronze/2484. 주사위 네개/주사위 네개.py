def calculate_prize(dice):
    dice_count = {i: dice.count(i) for i in range(1, 7)}
    count_values = list(dice_count.values())

    if 4 in count_values:
        number = count_values.index(4) + 1
        return 50000 + number * 5000
    elif 3 in count_values:
        number = count_values.index(3) + 1
        return 10000 + number * 1000
    elif count_values.count(2) == 2:
        pairs = [i + 1 for i, v in enumerate(count_values) if v == 2]
        return 2000 + sum(pair * 500 for pair in pairs)
    elif 2 in count_values:
        number = count_values.index(2) + 1
        return 1000 + number * 100
    else:
        return max(dice) * 100

n = int(input())
max_prize = 0

for _ in range(n):
    dice = list(map(int, input().split()))
    prize = calculate_prize(dice)
    if prize > max_prize:
        max_prize = prize

print(max_prize)
