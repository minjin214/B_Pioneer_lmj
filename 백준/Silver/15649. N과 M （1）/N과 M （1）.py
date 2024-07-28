stack = []

def permu():
    if len(stack) == m: 
        print(*stack)
    
    for i in range(1, n+1):
        if vis[i]:
            continue 
        vis[i] = True
        stack.append(i)
        permu()
        stack.pop() 
        vis[i] = False 
    
n, m = map(int, input().split())    
vis = [False] * (n+1) 
permu()