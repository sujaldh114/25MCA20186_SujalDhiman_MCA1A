import sys
input = sys.stdin.readline

maxn = 400000
prime = [True] * (maxn + 1)
prime[0] = prime[1] = False

for i in range(2, int(maxn**0.5) + 1):
    if prime[i]:
        for j in range(i*i, maxn+1, i):
            prime[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    
    if n <= 3:
        print(-1)
        continue
    
    odd = []
    even = []
    
    for i in range(1, n+1):
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    
    ans = []
    
    ans.append(1)
    odd.remove(1)
    
    for x in odd:
        ans.append(x)
    
    last = ans[-1]
    pos = -1
    
    for i in range(len(even)):
        if prime[last + even[i]] == False:
            pos = i
            break
    
    ans.append(even[pos])
    even.pop(pos)
    
    for x in even:
        ans.append(x)
    
    print(*ans)
