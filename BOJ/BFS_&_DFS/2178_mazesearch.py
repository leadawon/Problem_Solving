'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13

'''
import sys
from collections import defaultdict
from collections import deque


sys.stdin = open("testcase.txt","r")

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))

maps = defaultdict(lambda: [])

qu = deque()
# loc x  , loc y  ,  count
qu.append((0, 0, 1))
visited = [[0] * m for _ in range(n)]
cnt = 1

visited[0][0] = 1

while qu:
    item = qu.popleft()
    if item[0] == n - 1 and item[1] == m - 1:
        cnt = item[2]
        break

    if item[0] > 0 and arr[item[0] - 1][item[1]] and not visited[item[0] - 1][item[1]]:
        qu.append((item[0] - 1, item[1], item[2] + 1))
        visited[item[0] - 1][item[1]] = 1

    if item[1] < m - 1 and arr[item[0]][item[1] + 1] and not visited[item[0]][item[1] + 1]:
        qu.append((item[0], item[1] + 1, item[2] + 1))
        visited[item[0]][item[1] + 1] = 1

    if item[0] < n - 1 and arr[item[0] + 1][item[1]] and not visited[item[0] + 1][item[1]]:
        qu.append((item[0] + 1, item[1], item[2] + 1))
        visited[item[0] + 1][item[1]] = 1

    if item[1] > 0 and arr[item[0]][item[1] - 1] and not visited[item[0]][item[1] - 1]:
        qu.append((item[0], item[1] - 1, item[2] + 1))
        visited[item[0]][item[1] - 1] = 1

sys.stdout.write(f"{cnt}")





'''
전형적인 bfs 문제이다.
'''
