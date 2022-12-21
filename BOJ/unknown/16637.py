'''
<https://www.acmicpc.net/problem/16637>
문제
길이가 N인 수식이 있다. 수식은 0보다 크거나 같고, 9보다 작거나 같은 정수와 연산자(+, -, ×)로 이루어져 있다. 연산자 우선순위는 모두 동일하기 때문에, 수식을 계산할 때는 왼쪽에서부터 순서대로 계산해야 한다. 예를 들어, 3+8×7-9×2의 결과는 136이다.

수식에 괄호를 추가하면, 괄호 안에 들어있는 식은 먼저 계산해야 한다. 단, 괄호 안에는 연산자가 하나만 들어 있어야 한다. 예를 들어, 3+8×7-9×2에 괄호를 3+(8×7)-(9×2)와 같이 추가했으면, 식의 결과는 41이 된다. 하지만, 중첩된 괄호는 사용할 수 없다. 즉, 3+((8×7)-9)×2, 3+((8×7)-(9×2))은 모두 괄호 안에 괄호가 있기 때문에, 올바른 식이 아니다.

수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하시오. 추가하는 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.

입력
첫째 줄에 수식의 길이 N(1 ≤ N ≤ 19)가 주어진다. 둘째 줄에는 수식이 주어진다. 수식에 포함된 정수는 모두 0보다 크거나 같고, 9보다 작거나 같다. 문자열은 정수로 시작하고, 연산자와 정수가 번갈아가면서 나온다. 연산자는 +, -, * 중 하나이다. 여기서 *는 곱하기 연산을 나타내는 × 연산이다. 항상 올바른 수식만 주어지기 때문에, N은 홀수이다.

출력
첫째 줄에 괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값을 출력한다. 정답은 231보다 작고, -231보다 크다.

예제 입력 1 
9
3+8*7-9*2
예제 출력 1 
136
예제 입력 2 
5
8*3+5
예제 출력 2 
64
예제 입력 3 
7
8*3+5+2
예제 출력 3 
66
예제 입력 4 
19
1*2+3*4*5-6*7*8*9*0
예제 출력 4 
0
예제 입력 5 
19
1*2+3*4*5-6*7*8*9*9
예제 출력 5 
426384
예제 입력 6 
19
1-9-1-9-1-9-1-9-1-9
예제 출력 6 
24
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: rlgns9999
'''
import sys
#sys.stdin = open("testcase.txt")
num : int = int(sys.stdin.readline().rstrip())
sen : str = sys.stdin.readline().rstrip()
operands : list = []
operaters : list = []

def calc(a:int,b:int,s:str):
    if s=="+":
        return a+b
    elif s=="-":
        return a-b
    else:
        return a*b

for ind,token in enumerate(sen):
    if ind%2==0:
        operands.append(int(token))
    else:
        operaters.append(token)
maxdp = [0]*len(operands)
mindp = [0]*len(operands)

maxdp[0] = operands[0]
mindp[0] = operands[0]

if num>1:
    if operaters[0] == "+":
        maxdp[1] = operands[0] + operands[1]
        mindp[1] = operands[0] + operands[1]
    elif operaters[0] == "-":
        maxdp[1] = operands[0] - operands[1]
        mindp[1] = operands[0] - operands[1]
    elif operaters[0] == "*":
        maxdp[1] = operands[0] * operands[1]
        mindp[1] = operands[0] * operands[1]

    for idx in range(2,len(operands)):
        maxdp[idx]=max(calc(maxdp[idx-1],operands[idx],operaters[idx-1]),calc(maxdp[idx-2],calc(operands[idx-1],\
                        operands[idx],operaters[idx-1]),operaters[idx-2]),\
                        calc(mindp[idx-2],calc(operands[idx-1],operands[idx],operaters[idx-1]),operaters[idx-2]))
        mindp[idx]= min(calc(mindp[idx-1],operands[idx],operaters[idx-1]),calc(maxdp[idx-2],calc(operands[idx-1],\
                        operands[idx],operaters[idx-1]),operaters[idx-2]),\
                        calc(mindp[idx-2],calc(operands[idx-1],operands[idx],operaters[idx-1]),operaters[idx-2]))
print(maxdp[-1])
'''
maxdp mindp
maxdp는 
1. index-1에서의 maxdp값과 index에서의 operand를 idx-1번째 operater로 연산한값
2. index-2에서의 maxdp값과 index-1,index에서의 operands를 idx-1번째 operater로 연산하고 이 값을 idx-2번째 operater로 연산한 값
3. index-2에서의 mindp값과 index-1,index에서의 operands를 idx-1번째 operater로 연산하고 이 값을 idx-2번째 operater로 연산한 값
이 셋중 max값을 선택하면 된다.
'''
