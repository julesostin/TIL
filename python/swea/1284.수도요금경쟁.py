# A사는 1리터당 P의 돈이 지불/ A : W*P
# B사는 기본요금(Q)을 먼저 누적한 후 R리터보다 많은 양을 사용한 경우
# 초과량(W-R)에 대해 1리터당 S요금을 부과.
# if문으로 반복하면 될거같음.

import sys

sys.stdin = open("input1284.txt")
T = int(input())

for i in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    a_company = 0
    b_company = 0
    a_company += W*P
    b_company += Q
    if W > R :
        b_company += (W-R)*S

    print('#%d %d' % (i, min(a_company, b_company)))







    
