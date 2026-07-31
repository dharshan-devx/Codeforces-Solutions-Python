import sys
input = sys.stdin.readline

def dhxrshxn():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    kth_score = arr[k - 1]
    cnt = 0

    for score in arr:
        if score >= kth_score and score > 0:
            cnt += 1

    print(cnt)

dhxrshxn()