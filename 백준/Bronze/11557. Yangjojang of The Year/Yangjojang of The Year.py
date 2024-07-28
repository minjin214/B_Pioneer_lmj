case = int(input())

for i in range(0,case):
    n = int(input())
    max = 0
    NAME = ""
    for i in range(0,n):
        name, bottle = input().split()
        bottle = int(bottle)
        if bottle > max:
            max = bottle
            NAME = name
    print(NAME)
    