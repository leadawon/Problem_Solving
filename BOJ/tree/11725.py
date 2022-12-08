'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
출처
문제를 만든 사람: baekjoon
잘못된 조건을 찾은 사람: jh05013
'''
import sys
from collections import defaultdict
sys.stdin = open("testcase.txt","r")

dic = defaultdict(lambda : [])
n = int(sys.stdin.readline().rstrip())
par_dic = {}
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
    par_dic[a] = 0
    par_dic[b] = 0

used = [0] * 100001
used[1] = 2
par = [1]
flag = True
while par:
    parent = par.pop()
    for i in dic[parent]:
        if not used[i]:
            par_dic[i] = parent
            used[i]=1
            par.append(i)
for i,v in enumerate(used):
    if v==1:
        sys.stdout.write(f"{par_dic[i]}\n")
'''
트리문제지만 트리로 안풀었다.
defaultdict와 dfs로 풀었다.
'''
