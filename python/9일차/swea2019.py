import sys
sys.stdin = open("input2019.txt", "r")

T =int(input())

for i in range(0, T+1):
    i = 2**i
    print(i, end = ' ')

# 이렇게 간단한거였구나, i에다가 0부터 넣어놓고 2승씩 곱해서 print
# 문제를 잘 읽어봐야 함. 제목이 버블버블이었는데, 
# 2를 횟수만큼 곱하는 줄 알고 풀이가 막혔음. 횟수<<이건 제곱. 
# 수학 공부해라...