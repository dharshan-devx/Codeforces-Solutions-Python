t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')

    for i in range(n-1):
        if a[i] > a[i+1]:
            ans = 0
            break
        diff = a[i+1] - a[i]
        ans = min(ans, diff//2 + 1)

    print(ans)