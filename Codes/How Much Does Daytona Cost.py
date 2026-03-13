import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) 
index += 1

for _ in range(t):
	n = int(data[index])
	k = int(data[index + 1]) 
	index += 2

	a = list(map(int, data[index:index + n])) 
	index += n

	number_is_present = False

	for i in range(n):
		if a[i] == k:
			number_is_present = True 
			break 

	if number_is_present:
		print("YES")
	else:
		print("NO")