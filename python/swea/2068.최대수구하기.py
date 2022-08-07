import sys
sys.stdin = open("input2068.txt","r")

N = int(input())

# for i in range(0,N+1):
#     number_list=[]
#     b = number_list
#     for j in range(0,):
#         j.sort()
# print(j)

# 나의 의도는. number_list라는 리스트를 만들어서 i를 리스트에 넣어서 
# 오름차순 정리를해서 첫번째 값 출력. 이었는데, 맙소사. NameError: name 'j' is not defined
# 오류값 찾다보니 내가 list(split())을 전혀 이해하지 못하고 있었다는 사실도 깨달음.

for test_case in range(1, N+1):
    
# 최대값을 구하려면 max()함수를 쓰는게 맞고, 리스트로 각 숫자를 담고 그 담은 리스트에
# max값을 취하는게 편리하다. 따라서 이 문제는 나열된 숫자를 리스트화 하는 게 가장 중요한.

# input을 보면 한줄로 나열되어있다. 그걸 input().split()함수를 사용해서 띄어쓰기를 기준으로 
# 각 숫자를 나누어 담아야 한다. 이때 list(input().split())으로 입력을 띄어쓰기 기준으로 나누고,
# 리스트화 하면 '문자열'의 숫자가 담겨진 리스트가 만들어진다.
    
    number_list=list(map(int,input().split()))
    max_=max(number_list)
    print("#{} {}".format(test_case, max_))
    
 
#우리가 원하는 것은 정수화된 값이므로, list(map(int,input().split()))을 사용하면 정수화 된 숫자를
#담은 리스트를 구할 수 있다.

