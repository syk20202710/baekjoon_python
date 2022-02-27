'''x, y =map(int,input().split()) # 현재 시각
z= int(input()) # 걸리는 시간
a= y+z//60 #몫
b = y+z%60 #나머지

if y+z >60 and x== 23:
    print(x-23+a, b)
elif y+z > 60:
    print(x+a,y+b)
else:
    print(x, y+z)
'''
H,M = map(int,input().split())
L=int(input())

a=(M+L)//60 #몫
b=(M+L)%60 #시간


if M+L>60:
    print(H+a,b)
elif M+L>60 and H+a>24:
    print(H+a-24, b)
else:
    print(H, M+L)
