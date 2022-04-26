x,y,z=map(int,input().split())
b=sorted(list(map(int,input().split())))[::-1]
c=sorted(list(map(int,input().split())))[::-1]
d=sorted(list(map(int,input().split())))[::-1]
print(sum(b+c+d))
result = 0
m=min(x,y,z)
for i,j,k in zip(b,c,d):
    result+=(i+j+k)*0.9
result+=sum(b[m::])+sum(c[m::])+sum(d[m::])
print(int(result))