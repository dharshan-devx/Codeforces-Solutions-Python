import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) 
index += 1

for _ in range(t): 
	n = int(data[index]) 
	index += 1

	a = [] 
	for i in range(n - 1): 
		a.append(int(data[index])) 
		index += 1

	sum_efficiency = sum(a) 

	print(-1 * sum_efficiency) 