# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)


# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.
# input값 3 
# 3 17 1 39 8 41 2 32 99 2

import sys
sys.stdin = open("input2071.txt", "r")
T = int(input())


for test_case in range(1, T + 1):
    
    number = map(int, input().split())
    average = round(sum(number) / 10)
    # 여기까지는 이해가 된다만... 
    print("#{} {}".format(test_case, average))
