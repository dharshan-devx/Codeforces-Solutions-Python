import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        ttl = arr.count(2)
        left = 0
        found = False
        for i in range(n-1):
            if arr[i] == 2:
                left += 1 
            right = ttl - left 
            if left == right:
                print(i+1)
                found = True
                break
        if not found:
            print(-1)
dhxrshxn()