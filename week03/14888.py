from itertools import permutations, combinations
import sys
input = sys.stdin.readline

def cal(l, op):
    if op == '//' and int(l[0]) < 0: # 나누기이면서 음수
        temp = -(abs(int(l[0]))//int(l[1]))
    else:
        temp = eval(l[0]+op+l[1]) #아니면 그냥 계산
    del l[:2] # 앞에 두수부터 계산하고 삭제
    l.insert(0, str(temp)) # 계산하고 첫번째에 다시 넣기
    return l

n = int(input())
types = ['+','-','*','//']
nums = list(input().split())
input_oper = list(map(int, input().split()))
#연산자 갯수만큼 리스트에 연산자를 담아서 순열 (숫자는 그대로 이므로)
operators = list(set(permutations([types[i] for i in range(4) for _ in range(input_oper[i])])))
answer= []

# 경우의 수만큼 계산
for i in operators:
    temp = nums[:]
    for j in i:
        temp = cal(temp,j)
    answer.append(int(temp[0]))
        
        
print(max(answer))
print(min(answer))