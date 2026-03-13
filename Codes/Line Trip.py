for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    max_need = a[0]
    for i in range(1,n):
        max_need = max(max_need, a[i] - a[i-1])
    max_need = max(max_need, 2 * (x - a[-1]))
    print(max_need)