'''
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

예제 입력 1 
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1 
7
힌트
예제의 경우 {1 5 2 1 4 3 4 5 2 1}이 가장 긴 바이토닉 부분 수열이다.

출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: gmldk728
문제의 오타를 찾은 사람: mwy3055
'''
import sys
#sys.stdin = open("testcase.txt","r")
n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
dprv = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            dprv[i] = max(dprv[i], dprv[j] + 1)

maxsum1 = 0

for i in range(n):
    if dp[i] + dprv[i] > maxsum1:
        maxsum1 = dp[i] + dprv[i]

sys.stdout.write((f"{maxsum1 - 1}"))
'''
핵심 아이디어는 11053.py에 있다.
회문구조로 생각해서 거꾸로도 구해보았다.
'''
