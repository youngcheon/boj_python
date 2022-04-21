import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
#입력받을 원소 리스트
num_list=[]
while True:
    try:
        num=int(input())
        num_list.append(num)
    except:
        break

def postorder(left,right):
    #순서 역전시 종료
    if left>right:
        return
    else:
        mid=right+1        #분할 기준
        for i in range(left+1,right+1):
            #해당 원소가 현재 노드보다 크다면 그 전까지는 왼쪽 서브 트리,
            #해당 원소 이후는 오른쪽 서브 트리이다.
            if num_list[left]<num_list[i]:
                mid=i
                break
        postorder(left+1,mid-1)
        postorder(mid,right)
        print(num_list[left])

postorder(0,len(num_list)-1)