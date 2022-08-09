
import sys
sys.stdin = open('input1288.txt', "r")

T = int(input())
for test_case in range(1,T+1): 
    # input가져오기(첫번째 값 -> 1)
    N = int(input())
    N1 = N
    numbers = set()
    #while 반복 : set 길이가 10이 될 때까지
    while True:
    # while len(numbers) < 10:
        #10이 되면 false가 되면서 끝남.
    # for 반복 : 숫자를 문자로 
        for n in str(N): #문자로 바꾼 N
            # numbers set 추가. 10이 될 때까지.
            numbers.add(n)
        if len(numbers) == 10:
            break
            # print(n, numbers)
        N += N1
        #N을 증가 시켰을 때 어떤 식으로 써볼까? 
    print(f'#{test_case} {N}')

#N*cnt도 ok!
#굳이? 그러느니 5180에서 끊어!