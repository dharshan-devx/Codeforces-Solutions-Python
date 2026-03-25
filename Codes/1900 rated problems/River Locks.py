import sys
from bisect import bisect_right

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(input_data[idx]); idx += 1
    v = [int(input_data[idx+i]) for i in range(n)]; idx += n
    q = int(input_data[idx]); idx += 1
    queries = [int(input_data[idx+i]) for i in range(q)]; idx += q
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + v[i]
    
    max_v = max(v)
    total = prefix[n]
    
    LOG = 18
    
    results = []
    
    for t in queries:
        if t < max_v:
            results.append(-1)
            continue
        
        nxt = [0] * (n + 1)
        for i in range(n):
            target = prefix[i] + t
            j = bisect_right(prefix, target) - 1
            nxt[i] = j
        nxt[n] = n
        
        up = [nxt[:]]
        for k in range(1, LOG):
            prev = up[k-1]
            cur = [prev[prev[i]] for i in range(n+1)]
            up.append(cur)
        
        pos = 0
        ans = 0
        for k in range(LOG-1, -1, -1):
            if up[k][pos] < n:
                pos = up[k][pos]
                ans += (1 << k)
        
        if pos < n:
            pos = nxt[pos]
            ans += 1
        
        if pos >= n:
            results.append(ans)
        else:
            results.append(-1)
    
    print('\n'.join(map(str, results)))

solve()