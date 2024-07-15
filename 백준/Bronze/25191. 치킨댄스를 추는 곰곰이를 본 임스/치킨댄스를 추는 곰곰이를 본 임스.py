N = int(input())
A,B = map(int, input().split())

if N < (A//2+B):
    print(N)
else:
    print(A//2+B)