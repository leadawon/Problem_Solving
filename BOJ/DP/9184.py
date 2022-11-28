'''
문제
재귀 호출만 생각하면 신이 난다! 아닌가요?

다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

제한
-50 ≤ a, b, c ≤ 50
예제 입력 1 
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
예제 출력 1 
w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1
출처
ICPC > Regionals > North America > Pacific Northwest Regional > 1999 Pacific Northwest Region Programming Contest C번

문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: jh05013
데이터를 추가한 사람: mrseos
'''
import sys
from collections import defaultdict

dic = defaultdict(lambda:"init")

def makedic(tp):
    if dic[tp] != "init":
        return dic[tp]
    if tp[0] <= 0 or tp[1] <= 0 or tp[2] <= 0:
        dic[(0,0,0)]=1
        return dic[(0,0,0)]
    
    if tp[0] > 20 or tp[1]> 20 or tp[2] > 20:
        dic[(tp[0],tp[1],tp[2])] = makedic((20, 20, 20))
        return dic[(tp[0],tp[1],tp[2])]

    if tp[0] < tp[1] and tp[1]< tp[2]:
        dic[(tp[0],tp[1],tp[2])] = makedic((tp[0], tp[1], tp[2]-1))\
                                   + makedic((tp[0], tp[1]-1, tp[2]-1)) - makedic((tp[0], tp[1]-1, tp[2]))
        return dic[(tp[0],tp[1],tp[2])]

    else:
        dic[(tp[0],tp[1],tp[2])] = makedic((tp[0]-1, tp[1], tp[2])) + makedic((tp[0]-1, tp[1]-1, tp[2])) +\
               makedic((tp[0]-1, tp[1], tp[2]-1)) - makedic((tp[0]-1, tp[1]-1, tp[2]-1))
        return dic[(tp[0],tp[1],tp[2])]

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    sys.stdout.write(f"w({a}, {b}, {c}) = {makedic((a,b,c))}\n")
    
    
'''
dic은 재귀를 돌때마다. 해당 튜플에 값을 기억한다.
makedic 함수는 초장에 a,b,c 튜플에 해당하는 dic의 값이 있을때 값을 반환
없을때는 조건에 따라서 dic에 값을 할당하면서 답을 찾아간다.
'''
    


