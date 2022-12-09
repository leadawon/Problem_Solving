import sys
n,m = map(int,sys.stdin.readline().split())
dp=[0]*(m+1)

dp[1]=0
dp[2]=1
for i in range(3,m+1):
	if i%2==0:
		dp[i] = dp[i//2] + 1
	else:
		dp[i]= dp[(i+1)//2] + 2
sum1 = 0
for i in range(n,m+1):
	sum1 += dp[i]
if n==1:
	sum1 += 1
sys.stdout.write(f"{sum1}")
###### ####### #######
import sys
from collections import defaultdict,deque
sys.stdin = open("testcase.txt","r")
n,k,m = map(int,sys.stdin.readline().split()) #n은 남은 대기자 #k는 현재층수 #m은 엘베 남은 정원
dic = defaultdict(lambda : deque())

for i in range(n):
    pre,post = map(int,sys.stdin.readline().split())
    dic[pre].append(post)
prek = k
k=1
elevater = defaultdict(int)
cnt = 0
while n:
        while n and k!=prek: #up
            if elevater[k]: #내리기
                m += elevater[k]
                n -= elevater[k]
                elevater[k] = 0


            while m and dic[k]: #태우기
                elevater[dic[k].popleft()] += 1
                m -= 1
            k += 1
            cnt += 1
        while n and k!=1: #down
            if elevater[k]:  # 내리기
                m += elevater[k]
                n -= elevater[k]
                elevater[k] = 0

            while m and dic[k]:  # 태우기
                elevater[dic[k].popleft()] += 1
                m -= 1
            k -= 1
            cnt += 1
sys.stdout.write(f"{cnt-1}")


