#a와 b 입력을 받고, 불 값으로 변환하여 저장해줍니다.
#a와 b가 모두 0(False)일 때만 1(True)이기 때문에, 
#if 조건문에 a == False and b == False 를 조건으로 걸어줍니다.
#조건이 참이면 True를, 조건이 맞지 않으면 False를 출력합니다.

a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( not (c or d) )
