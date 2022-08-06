
# # 조건식 만들기
# # 가위는 1, 바위는 2, 보는 3이면

# a,b = map(int, input().split())

# if a == 1:
#     if b == 3:
#         print('a')

# if a == 2:
#     if b == 1:
#         print('a')

# if a == 3:
#     if b == 2:
#         print('a')

# if b == 1:
#     if a == 3:
#         print('b')

# if b == 2:
#     if a == 1:
#         print('b')

# if b == 3:
#     if a == 2:
#         print('b')


a, b = map(int, input().split())
if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print('a')

else:
    print('b')