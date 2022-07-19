#시분초 입력받아 분'만 출력하기.
# 입력받는 거니까 a=input()
# : <<세미클론을 어떻게 입력할지

#시:분:초 형식으로 시간이 입력될때 분만 출력함** how to make it?
# h:hours, m:minute, s:seconds...그리고 split 함수.


h,m,s=input().split(':')
print(m)
