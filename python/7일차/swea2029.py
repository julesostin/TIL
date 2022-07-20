# a = int(input())                        정수형 변수 1개 입력 받는 예제
# b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
# d = float(input())                      실수형 변수 1개 입력 받는 예제
# e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
# h = input()                             문자열 변수 1개 입력 받는 예제

import sys
sys.stdin = open("input2029.txt", "r")

T = int(input())

for i in range(0, T):
    a, b = map(int, input().split())
    print("#%d" % (i+1), end=' ')
    print(int(a/b), a%b)