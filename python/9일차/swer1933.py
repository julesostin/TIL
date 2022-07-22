
# # 표준 입력 예제
# a = int(input())                        정수형 변수 1개 입력 받는 예제
# b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
# d = float(input())                      실수형 변수 1개 입력 받는 예제
# e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
# h = input()                             문자열 변수 1개 입력 받는 예제
# 약수란 n을 나누었을 때 나머지가 0인 것.


import sys
sys.stdin = open("input1933.txt", "r")

T =int(input())

for i in range(1, T+1):
    if not T % i:
        print(i, end=' ')