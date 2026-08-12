t = int(input())

for _ in range(t):

    n, q = map(int, input().split())

    arr = list(map(int, input().split()))

    pref = [0] * (n + 1)

    for i in range(n):
        pref[i + 1] = pref[i] + arr[i]

    total = pref[n]

    for _ in range(q):

        l, r, k = map(int, input().split())

        old = pref[r] - pref[l - 1]

        length = r - l + 1

        new_total = total - old + length * k

        if new_total % 2:
            print("YES")
        else:
            print("NO")