case = 1
while True:
    L, P, V = map(int,input().split())
    if L+P+V == 0:
        break
    print(f"Case {case}:",(V//P)*L+min(V%P,L))
    case += 1