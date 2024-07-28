score = [int(input()) for j in range(10)]
i = 0
scores = 0
while i<len(score):
    scores += score[i]
    if scores == 100:
        break
    elif scores > 100:
        if scores - 100 <= 100 - (scores-score[i]):
            break
        else:
            scores = scores - score[i]
        break
    i += 1
print(scores)