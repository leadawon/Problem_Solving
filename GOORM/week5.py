
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n = int(sys.stdin.readline().rstrip())

left= n-1
down = 0
right = 0
top = n-1

for i in range(n):
	for ind,item in enumerate(sys.stdin.readline().split()):
		if item == "1":
			if left > ind:
				left = ind
			if down < i:
				down = i
			if right < ind:
				right = ind
			if top > i:
				top = i
if left > right:
	sys.stdout.write("0")
else:
	sys.stdout.write(f"{(right-left + 1) * (down - top + 1)}")

################################################################
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n,k = map(int,sys.stdin.readline().split())

arr = [0] * (n+1)
arr[0]=1000002
for i in map(int,sys.stdin.readline().split()):
	arr[i] += 1

min1 = 1000001
indlst = []
for ind,item in enumerate(arr):
	if item == min1:
		indlst.append(ind)
	elif item < min1:
		indlst = []
		indlst.append(ind)
		min1 = item

sys.stdout.write(f"{sum(indlst)}")


'''
<https://k-digital.goorm.io/apply/assessment/31383/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9C%84%ED%81%B4%EB%A6%AC>
'''
