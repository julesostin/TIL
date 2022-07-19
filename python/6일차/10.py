# n아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# output : 두 번째 리스트의 최댓값이 더 큽니다.

number_list =  [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# type error / python tytor 돌려보니 max2에서 오류가 납니다. 추측하건데 6줄에 있는 max가 함수 max로 인식된 듯 하여 max1으로 바꾸니 됨..운이 좋았다.