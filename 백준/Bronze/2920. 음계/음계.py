numbers = list(map(int, input().split()))

ascending = list(range(1, 9))
descending = list(range(8, 0, -1))

if numbers == ascending:
    print("ascending")
elif numbers == descending:
    print("descending")
else:
    print("mixed")