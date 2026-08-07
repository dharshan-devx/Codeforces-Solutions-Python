import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        
        arr.sort()
        curr = 1
        best = 1
        for i in range(1,n):
            if arr[i] - arr[i-1] <= k:
                curr += 1
            else:
                best = max(curr, best)
                curr = 1
        best = max(best, curr)
        print(n-best)
            
            
            
            
dhxrshxn()