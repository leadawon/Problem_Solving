'''
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
출처
Olympiad > International Olympiad in Informatics > IOI 1994 > Day 1 1번

문제의 오타를 찾은 사람: apjw6112, Martian, paranocean
잘못된 조건을 찾은 사람: djm03178
데이터를 추가한 사람: eunhyekim1223, hwangtmdals
잘못된 데이터를 찾은 사람: thanatos0128
'''
import sys
sys.stdin = open("testcase.txt","r")
n= int(sys.stdin.readline().rstrip())

arr = []

arr.append([int(sys.stdin.readline().rstrip())])

for i in range(n-1):
    arr.append(list(map(int,sys.stdin.readline().split())))
dp = [[0]*k for k in range(1,n+1)]

dp[0][0] = arr[0][0] # 0층부터 세는 n층은 n+1개의 원소가 있음.
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + arr[i][j]
        elif j==i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + arr[i][j]

sys.stdout.write(f"{max(dp[n-1])}")




'''
주의! 트리구조가 아님!

0층의 0번째 원소가 삼각형의 마지막 원소일때 구하고
이 값을 이용해서 1층의 0번째 원소 1층의 1번째 원소가 마지막 원소일때 최댓값을 구한다.
이런식으로 쭉 이어나가면 dp로 풀린다.
앞선 문제보다는 쉬운듯?
'''
