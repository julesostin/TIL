# a = int(input())                        정수형 변수 1개 입력 받는 예제
# b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
# d = float(input())                      실수형 변수 1개 입력 받는 예제
# e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
# h = input()                             문자열 변수 1개 입력 받는 예제

import sys
sys.stdin = open("input1545.txt", "r")

number=int(input())

for i in range(number,-1,-1):
    print(i, end = ' ')

# range(stop) , range(number(input값))은 0,1,2,3,4,5,6,...숫자를 생성한다
# 마지막 숫자는 포함되지 않으니 -1로 해야하고 거꾸로 출력해야 하니 -1
# range(start,stop,step) // range(20,0,-2):20부터1까지 2개의스텝으로 거꾸로.