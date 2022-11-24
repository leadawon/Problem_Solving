'''
문제
챔피언스 리그 결승전을 앞두고 있는 맨체스터 유나이티드의 명장 퍼거슨 감독은 이번 경기에 4-4-2 다이아몬드 전술을 사용하려고 한다.

오늘 결승전에 뛸 선발 선수 11명은 미리 골라두었지만, 어떤 선수를 어느 포지션에 배치해야 할지 아직 결정하지 못했다.

수석코치 마이크 펠란은 11명의 선수가 각각의 포지션에서의 능력을 0부터 100까지의 정수로 수치화 했다. 0은 그 선수가 그 포지션에 적합하지 않다는 뜻이다.

이때, 모든 선수의 포지션을 정하는 프로그램을 작성하시오. 모든 포지션에 선수를 배치해야 하고, 각 선수는 능력치가 0인 포지션에 배치될 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 첫째 줄에는 테스트 케이스의 개수 C가 주어진다. 각각의 케이스는 11줄로 이루어져 있고, i번 줄은 0과 100사이의 11개의 정수 sij를 포함하고 있다. sij는 i번선수가 j번 포지션에서 뛸 때의 능력이다. 모든 선수에게 적합한 포지션의 수는 최대 5개이다. (능력치가 0보다 크다)

출력
각각의 테스트 케이스에 대해서, 모든 포지션의 선수를 채웠을 때, 능력치의 합의 최댓값을 한 줄에 하나씩 출력한다. 항상 하나 이상의 올바른 라인업을 만들 수 있다.

예제 입력 1 
1
100 0 0 0 0 0 0 0 0 0 0
0 80 70 70 60 0 0 0 0 0 0
0 40 90 90 40 0 0 0 0 0 0
0 40 85 85 33 0 0 0 0 0 0
0 70 60 60 85 0 0 0 0 0 0
0 0 0 0 0 95 70 60 60 0 0
0 45 0 0 0 80 90 50 70 0 0
0 0 0 0 0 40 90 90 40 70 0
0 0 0 0 0 0 50 70 85 50 0
0 0 0 0 0 0 66 60 0 80 80
0 0 0 0 0 0 50 50 0 90 88
예제 출력 1 
970

'''
import sys
sys.stdin = open("testcase.txt","r")

def solution(level, visited, arr, sum1, maxsum1):
    if level == 11:
        if maxsum1 < sum1:
            maxsum1 = sum1
        return maxsum1
    for i in range(11):
        if visited[i] or not arr[level][i]:
            continue
        last_sum1 = sum1
        sum1 += arr[level][i]
        visited[i] = 1
        maxsum1 = solution(level + 1, visited, arr, sum1, maxsum1)
        visited[i] = 0
        sum1 = last_sum1
    return maxsum1


t = int(sys.stdin.readline().rstrip())
for i in range(t):
    arr = []
    visited = [0] * 11
    sum1 = 0
    maxsum1 = 0
    for j in range(11):
        arr.append(list(map(int, sys.stdin.readline().split())))
    sys.stdout.write(str(solution(0, visited, arr, sum1, maxsum1)))
    sys.stdout.write("\n")

'''
포지션별 점수가 0이거나 이미 차있는 포지션이면 return하는 가지치기를 통해서 빠르게 순회한다.
visited는 포지션을 나타낸다.
'''
