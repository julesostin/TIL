t = int(input())

for case in range(1,t+1):
    a, b = map(int,input().split())
    print(case, a//b, a%b, sep =" ")