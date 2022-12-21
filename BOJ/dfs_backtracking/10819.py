'''
<https://www.acmicpc.net/problem/10819>
문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

예제 입력 1 
6
20 1 15 8 4 10
예제 출력 1 
62
출처
문제를 만든 사람: baekjoon
'''
import sys
from itertools import permutations as pm
sys.stdin = open("testcase.txt","r")
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))
maxsuma =0
for tp in pm(arr,n):
    prev = tp[0]
    suma = 0
    for val in tp:
        suma += abs(prev-val)
        prev = val
    if suma > maxsuma:
        maxsuma = suma
print(maxsuma)
'''
중복이 있는 순열을 구현한 라이브러리를 찾지 못했다.
직접 구현해볼까...?
'''
