# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in total:
#     total += number
# count += 1

# print(total // count)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = 0
for i in number_list:
    result += i

print(result / len(number_list))

# 그냥 다 뜯어고쳤음 / 이렇게 넘버리스트에 있는 값들을 하나하나 for반복문
#을 통해서 돌면서 값을 더하고 더한 값들을 넘버리스트의 갯수로 나눠서 평균 
# 구하는..처음 해봤습니다.